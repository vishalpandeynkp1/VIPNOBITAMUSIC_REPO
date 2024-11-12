import os
import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")

# Get it from @Botfather in Telegram
BOT_TOKEN = getenv("BOT_TOKEN")

# Database to save your chats and stats... Get MongoDB:-  https://telegra.ph/How-To-get-Mongodb-URI-04-06
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "18000"))  # In seconds

# Custom max audio(music) duration for voice chat. Set DURATION_LIMIT in minutes.
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "3000"))  # In minutes

EXTRA_PLUGINS = getenv("EXTRA_PLUGINS", "True")  # Set to True to load extra plugins
EXTRA_PLUGINS_REPO = getenv("EXTRA_PLUGINS_REPO", "https://github.com/vishalpandeynkp1/NOBITA-EXTRA-PLUGIN")
EXTRA_PLUGINS_FOLDER = getenv("EXTRA_PLUGINS_FOLDER", "plugins")  # Folder name in your extra plugins repo

# Duration Limit for downloading Songs in MP3 or MP4 format from bot
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "1000"))  # In minutes

# Log Group Username for this.
LOG_GROUP_ID = getenv("LOG_GROUP_ID", "")

# Your User ID.
OWNER_ID = list(map(int, getenv("OWNER_ID", "6972508083").split()))  # Input type must be integer

# Privacy link for your bot
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://telegra.ph/Privacy-Policy-for-VIP-MUSIC-08-30")

# Get it from Heroku dashboard
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

# For customized or modified Repository
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/vishalpandeynkp1/VIPNOBITAMUSIC_REPO")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

# Git Token (for private repositories)
GIT_TOKEN = getenv("GIT_TOKEN", "")

# Token for Youtube songs.
TOKEN_ALLOW = os.getenv("TOKEN_ALLOW", "False")

# Auto Gcast/Broadcast Handler.
AUTO_GCAST = os.getenv("AUTO_GCAST", "off")

# Auto Broadcast Message
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/NOBITA_ALL_BOT")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/NOBITA_SUPPORT")

SUPPORT_CHAT = getenv("SUPPORT_GROUP", "https://t.me/NOBITA_SUPPORT")

# Auto-leaving assistant after a certain amount of time.
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", False)
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", 1800))  # In seconds

# Private bot mode
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", "False")

# Time sleep duration for Youtube downloader
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))

# Time sleep duration for Telegram downloader
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))

# Your Github Repo. Will be shown on /start Command
GITHUB_REPO = getenv("GITHUB_REPO", "https://github.com/vishalpandeynkp1/VIPNOBITAMUSIC_REPO")

# Spotify Client Credentials
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "409e31d3ddd64af08cfcc3b0f064fcbe")

# Video stream limit
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "999"))

# Playlist limit
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "500"))

# Playlist fetch limit
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "500"))

# Telegram audio and video file size limit
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "1073741824"))  # In bytes
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))  # In bytes

COOKIES = getenv("COOKIES", None)

# Set this to true if you want your bot to setup commands automatically in the bot's menu
SET_CMDS = getenv("SET_CMDS", "False")

# Pyrogram string sessions
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# Images
START_IMG_URL = getenv("START_IMG_URL", "https://envs.sh/ZK5.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://envs.sh/ZK5.jpg")
PLAYLIST_IMG_URL = getenv("PLAYLIST_IMG_URL", "https://envs.sh/ZK5.jpg")
GLOBAL_IMG_URL = getenv("GLOBAL_IMG_URL", "https://envs.sh/ZK5.jpg")
STATS_IMG_URL = getenv("STATS_IMG_URL", "https://envs.sh/ZK5.jpg")
TELEGRAM_AUDIO_URL = getenv("TELEGRAM_AUDIO_URL", "https://envs.sh/ZK5.jpg")
TELEGRAM_VIDEO_URL = getenv("TELEGRAM_VIDEO_URL", "https://envs.sh/ZK5.jpg")
STREAM_IMG_URL = getenv("STREAM_IMG_URL", "https://envs.sh/ZK5.jpg")
SOUNCLOUD_IMG_URL = getenv("SOUNCLOUD_IMG_URL", "https://envs.sh/ZK5.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://envs.sh/ZK5.jpg")
SPOTIFY_ARTIST_IMG_URL = getenv("SPOTIFY_ARTIST_IMG_URL", "https://envs.sh/ZK5.jpg")
SPOTIFY_ALBUM_IMG_URL = getenv("SPOTIFY_ALBUM_IMG_URL", "https://envs.sh/ZK5.jpg")
SPOTIFY_PLAYLIST_IMG_URL = getenv("SPOTIFY_PLAYLIST_IMG_URL", "https://envs.sh/ZK5.jpg")

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


def seconds_to_time(seconds):
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return f"{minutes:02d}:{remaining_seconds:02d}"


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        print("[ERROR] - Your SUPPORT_CHANNEL URL is wrong. Please ensure it starts with https://")

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        print("[ERROR] - Your SUPPORT_GROUP URL is wrong. Please ensure it starts with https://")

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print("[ERROR] - Your UPSTREAM_REPO URL is wrong. Please ensure it starts with https://")

if GITHUB_REPO:
    if not re.match("(?:http|https)://", GITHUB_REPO):
        print("[ERROR] - Your GITHUB_REPO URL is wrong. Please ensure it starts with https://")

if PING_IMG_URL:
    if PING_IMG_URL != "https://envs.sh/ZK5.jpg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            print("[ERROR] - Your PING_IMG_URL URL is wrong. Please ensure it starts with https://")

if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "https://envs.sh/ZK5.jpg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print("[ERROR] - Your PLAYLIST_IMG_URL URL is wrong. Please ensure it starts with https://")

if GLOBAL_IMG_URL:
    if GLOBAL_IMG_URL != "https://envs.sh/ZK5.jpg":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print("[ERROR] - Your GLOBAL_IMG_URL URL is wrong. Please ensure it starts with https://")

if STATS_IMG_URL:
    if STATS_IMG_URL != "https://envs.sh/ZK5.jpg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print("[ERROR] - Your STATS_IMG_URL URL is wrong. Please ensure it starts with https://")

if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "https://envs.sh/ZK5.jpg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print("[ERROR] - Your TELEGRAM_AUDIO_URL URL is wrong. Please ensure it starts with https://")

if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "https://envs.sh/ZK5.jpg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print("[ERROR] - Your TELEGRAM_VIDEO_URL URL is wrong. Please ensure it starts with https://")

if STREAM_IMG_URL:
    if STREAM_IMG_URL != "https://envs.sh/ZK5.jpg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print("[ERROR] - Your STREAM_IMG_URL URL is wrong. Please ensure it starts with https://")

if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "https://envs.sh/ZK5.jpg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print("[ERROR] - Your SOUNCLOUD_IMG_URL URL is wrong. Please ensure it starts with https://")

if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "https://envs.sh/ZK5.jpg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print("[ERROR] - Your YOUTUBE_IMG_URL URL is wrong. Please ensure it starts with https://")

if SPOTIFY_ARTIST_IMG_URL:
    if SPOTIFY_ARTIST_IMG_URL != "https://envs.sh/ZK5.jpg":
        if not re.match("(?:http|https)://", SPOTIFY_ARTIST_IMG_URL):
            print("[ERROR] - Your SPOTIFY_ARTIST_IMG_URL URL is wrong. Please ensure it starts with https://")

if SPOTIFY_ALBUM_IMG_URL:
    if SPOTIFY_ALBUM_IMG_URL != "https://envs.sh/ZK5.jpg":
        if not re.match("(?:http|https)://", SPOTIFY_ALBUM_IMG_URL):
            print("[ERROR] - Your SPOTIFY_ALBUM_IMG_URL URL is wrong. Please ensure it starts with https://")

if SPOTIFY_PLAYLIST_IMG_URL:
    if SPOTIFY_PLAYLIST_IMG_URL != "https://envs.sh/ZK5.jpg":
        if not re.match("(?:http|https)://", SPOTIFY_PLAYLIST_IMG_URL):
            print("[ERROR] - Your SPOTIFY_PLAYLIST_IMG_URL URL is wrong. Please ensure it starts with https://")
