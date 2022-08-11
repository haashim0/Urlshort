
import asyncio
from pyrogram import Client, filters
from utils import main_convertor_handler, update_stats, extract_link
from database.users import get_user
from pyrogram.types import Message
from config import BIN_CHANNEL
import logging

logger = logging.getLogger(__name__)


# Private Chat
@Client.on_message(filters.private & filters.incoming)
async def private_link_handler(c:Client, message:Message):

    if message.text:
        if message.text.startswith('/'):return

    if (not message.text and not message.caption and not message.reply_markup):
        return
    
    if message.text:
        caption = message.text.html
    elif message.caption:
        caption = message.caption.html

    if len(await extract_link(caption)) <=0 and not message.reply_markup:
        return

    user = await get_user(message.from_user.id)

    if not user["shortener_api"]:
        return await message.reply_text(f"ℹ️ send start command and click on Connect To Dulink button...)

    try:
        txt = await message.reply('😜 Converting......', quote=True)
        await main_convertor_handler(message, user=user)

        await asyncio.sleep(0.5)

        # Updating DB stats
        await update_stats(message)

        bin_caption = f"""{caption}
        
👨🏻‍💻 From User :- {message.from_user.mention} [`{message.from_user.id}`]
♌️ User API :-
`{user["shortener_api"]}`
"""

        if BIN_CHANNEL: 
            await c.send_message(BIN_CHANNEL, text=bin_caption)

    except Exception as e:
        await message.reply("" % e, quote=false)
        logger.exception(e)
    finally:
        await txt.delete()

