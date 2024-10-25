import asyncio
import glob
import json
import os
import random
import re
from typing import Union

import yt_dlp
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message
from youtubesearchpython.__future__ import VideosSearch

from VIPMUSIC.utils.database import is_on_off
from VIPMUSIC.utils.formatters import time_to_seconds


def cookie_txt_file():
    """Select a random .txt file from the 'cookies' folder and log the choice."""
    folder_path = f"{os.getcwd()}/cookies"
    filename = f"{os.getcwd()}/cookies/logs.csv"
    txt_files = glob.glob(os.path.join(folder_path, "*.txt"))
    if not txt_files:
        raise FileNotFoundError("No .txt files found in the specified folder.")
    cookie_txt_file = random.choice(txt_files)
    with open(filename, "a") as file:
        file.write(f"Chosen File : {cookie_txt_file}\n")
    return f"cookies/{os.path.basename(cookie_txt_file)}"


async def check_file_size(link):
    """Get file size of the video by link."""
    async def get_format_info(link):
        proc = await asyncio.create_subprocess_exec(
            "yt-dlp",
            "--cookies", cookie_txt_file(),
            "-J", link,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await proc.communicate()
        if proc.returncode != 0:
            print(f"Error:\n{stderr.decode()}")
            return None
        return json.loads(stdout.decode())

    def parse_size(formats):
        return sum(format.get("filesize", 0) for format in formats)

    info = await get_format_info(link)
    if info is None:
        return None

    formats = info.get("formats", [])
    if not formats:
        print("No formats found.")
        return None

    return parse_size(formats)


async def shell_cmd(cmd):
    """Execute shell command asynchronously and handle specific errors."""
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    out, errorz = await proc.communicate()
    if errorz and "unavailable videos are hidden" not in errorz.decode("utf-8").lower():
        return errorz.decode("utf-8")
    return out.decode("utf-8")


class YouTubeAPI:
    def __init__(self):
        self.base = "https://www.youtube.com/watch?v="
        self.regex = r"(?:youtube\.com|youtu\.be)"
        self.status = "https://www.youtube.com/oembed?url="
        self.listbase = "https://youtube.com/playlist?list="
        self.reg = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

    async def exists(self, link: str, videoid: Union[bool, str] = None):
        """Check if a YouTube link exists."""
        if videoid:
            link = self.base + link
        return bool(re.search(self.regex, link))

    # (Other methods here remain the same, adding async as needed for coroutine usage)

    async def download(
        self,
        link: str,
        mystic,
        video: Union[bool, str] = None,
        videoid: Union[bool, str] = None,
        songaudio: Union[bool, str] = None,
        songvideo: Union[bool, str] = None,
        format_id: Union[bool, str] = None,
        title: Union[bool, str] = None,
    ) -> Union[str, None]:
        """Download video/audio and handle specific conditions for file size and format."""
        if videoid:
            link = self.base + link
        loop = asyncio.get_running_loop()

        def download_audio():
            ydl_opts = {
                "format": "bestaudio/best",
                "outtmpl": "downloads/%(id)s.%(ext)s",
                "quiet": True,
                "cookiefile": cookie_txt_file(),
            }
            ydl = yt_dlp.YoutubeDL(ydl_opts)
            info = ydl.extract_info(link, download=False)
            file_path = os.path.join("downloads", f"{info['id']}.{info['ext']}")
            if not os.path.exists(file_path):
                ydl.download([link])
            return file_path

        def download_video():
            ydl_opts = {
                "format": "(bestvideo[height<=?720][width<=?1280][ext=mp4])+(bestaudio[ext=m4a])",
                "outtmpl": "downloads/%(id)s.%(ext)s",
                "quiet": True,
                "cookiefile": cookie_txt_file(),
            }
            ydl = yt_dlp.YoutubeDL(ydl_opts)
            info = ydl.extract_info(link, download=False)
            file_path = os.path.join("downloads", f"{info['id']}.{info['ext']}")
            if not os.path.exists(file_path):
                ydl.download([link])
            return file_path

        if songvideo:
            return await loop.run_in_executor(None, download_video)
        elif songaudio:
            return await loop.run_in_executor(None, download_audio)
        elif video:
            file_size = await check_file_size(link)
            if file_size and file_size / (1024 * 1024) > 250:
                print("File size exceeds 250MB limit.")
                return None
            return await loop.run_in_executor(None, download_video)
        else:
            return await loop.run_in_executor(None, download_audio)
