#
# Copyright (C) 2024 by THE-VIP-BOY-OP@Github, < https://github.com/THE-VIP-BOY-OP >.
#
# This file is part of < https://github.com/THE-VIP-BOY-OP/VIP-MUSIC > project,
# and is released under the MIT License.
# Please see < https://github.com/THE-VIP-BOY-OP/VIP-MUSIC/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="ᴘᴀᴜsᴇ sᴛʀᴇᴀᴍ",
            description=f"ᴘᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ sᴏɴɢ ᴏɴ ᴠᴏɪᴄᴇᴄʜᴀᴛ.",
            thumb_url="https://graph.org/file/638f56d8b53c137c20480.png",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="ʀᴇsᴜᴍᴇ sᴛʀᴇᴀᴍ",
            description=f"ʀᴇsᴜᴍᴇ ᴛʜᴇ ᴘᴀᴜsᴇᴅ sᴏɴɢ ᴏɴ ᴠᴏɪᴄᴇᴄʜᴀᴛ.",
            thumb_url="https://graph.org/file/638f56d8b53c137c20480.png",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="ᴍᴜᴛᴇ sᴛʀᴇᴀᴍ",
            description=f"ᴍᴜᴛᴇ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴏɴɢ ᴏɴ ᴠᴏɪᴄᴇᴄʜᴀᴛ",
            thumb_url="https://graph.org/file/638f56d8b53c137c20480.png",
            input_message_content=InputTextMessageContent("/vcmute"),
        ),
        InlineQueryResultArticle(
            title="ᴜɴᴍᴜᴛᴇ sᴛʀᴇᴀᴍ",
            description=f"ᴜɴᴍᴜᴛᴇ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴏɴɢ ᴏɴ ᴠᴏɪᴄᴇᴄʜᴀᴛ",
            thumb_url="https://graph.org/file/638f56d8b53c137c20480.png",
            input_message_content=InputTextMessageContent("/vcunmute"),
        ),
        InlineQueryResultArticle(
            title="sᴋɪᴘ sᴛʀᴇᴀᴍ",
            description=f"sᴋɪᴘ ᴛᴏ ɴᴇxᴛ ᴛʀᴀᴄᴋ. | sᴋɪᴘ ᴛᴏ ɴᴇxᴛ ᴛʀᴀᴄᴋ. | ғᴏʀ sᴘᴇᴄɪғɪᴄ ᴛʀᴀᴄᴋ ɴᴜᴍʙᴇʀ: /skip [number] ",
            thumb_url="https://graph.org/file/638f56d8b53c137c20480.png",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="ᴇɴᴅ sᴛʀᴇᴀᴍ",
            description="sᴛᴏᴘ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴏɴɢ ᴏɴ ɢʀᴏᴜᴘ ᴠᴏɪᴄᴇᴄʜᴀᴛ.",
            thumb_url="https://graph.org/file/638f56d8b53c137c20480.png",
            input_message_content=InputTextMessageContent("/stop"),
        ),
        InlineQueryResultArticle(
            title="sʜᴜғғʟᴇ sᴛʀᴇᴀᴍ",
            description="sʜᴜғғʟᴇ ᴛʜᴇ ǫᴜᴇᴜᴇᴅ ᴛʀᴀᴄᴋs ʟɪsᴛ.",
            thumb_url="https://graph.org/file/638f56d8b53c137c20480.png",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="sᴇᴇᴋ sᴛʀᴇᴀᴍ",
            description="sᴇᴇᴋ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴛʀᴇᴀᴍ ᴛᴏ ᴀ sᴘᴇᴄɪғɪᴄ ᴅᴜʀᴀᴛɪᴏɴ.",
            thumb_url="https://graph.org/file/638f56d8b53c137c20480.png",
            input_message_content=InputTextMessageContent("/seek 10"),
        ),
        InlineQueryResultArticle(
            title="ʟᴏᴏᴘ sᴛʀᴇᴀᴍ",
            description="ʟᴏᴏᴘ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ ᴍᴜsɪᴄ. ᴜsᴀsɢᴇ: /loop [enable|disable]",
            thumb_url="https://graph.org/file/638f56d8b53c137c20480.png",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
