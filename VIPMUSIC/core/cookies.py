

import os
import requests
import config
from ..logging import LOGGER


def save_file(pastebin_url, file_path="cookies/cookies.txt"):
    try:
        response = requests.get(pastebin_url)
        response.raise_for_status()

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as file:
            file.write(response.text)
        return file_path

    except requests.exceptions.RequestException:
        pass


def save_cookies():
    full_url = str(config.COOKIES)
    paste_id = full_url.split("/")[-1]
    pastebin_url = f"https://batbin.me/raw/{paste_id}"

    file_path = save_file(pastebin_url)
    if file_path and os.path.getsize(file_path) > 0:
        LOGGER(__name__).info(f"𝗖𝗼𝗼𝗸𝗶𝗲𝘀 𝘀𝗮𝘃𝗲𝗱 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝘁𝗼 {file_path}.")
    else:
        LOGGER(__name__).error("𝘍𝘢𝘪𝘭𝘦𝘥 𝘵𝘰 𝘴𝘢𝘷𝘦 𝘤𝘰𝘰𝘬𝘪𝘦𝘴 𝘰𝘳 𝘵𝘩𝘦 𝘧𝘪𝘭𝘦 𝘪𝘴 𝘦𝘮𝘱𝘵𝘺. 🥹")
