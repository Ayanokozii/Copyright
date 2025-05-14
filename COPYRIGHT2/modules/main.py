from pyrogram import Client, filters
import os
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters
from pyrogram.types import Message
import time
import psutil
import platform
import logging
from config import OWNER_ID, BOT_USERNAME
from config import *
from COPYRIGHT2 import COPYRIGHT2 as app

import pyrogram
from pyrogram.errors import FloodWait


# ----------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------


start_txt = """<b> 🤖 ᴄᴏᴘʏʀɪɢʜᴛ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ʙᴏᴛ 🛡 </b>

ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ʙᴏᴛ ᴡᴇ ᴀʀᴇ ʜᴇʀᴇ ʙʏ ᴛᴏ ᴘʀᴏᴛᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ ғʀᴏᴍ ᴄᴏᴘʏʀɪɢʜᴛ ɪssᴜᴇs ✅. ᴡᴇ ᴘʀᴏᴠɪᴅᴇ ʙᴇsᴛ sᴀғᴇᴛʏ ғᴇᴀᴛᴜʀᴇs ʟɪᴋᴇ ᴡᴇ ᴘʀᴏʙʜɪᴛᴇᴅ❌ [ ᴘᴏʀɴɢʀᴀᴘʜɪᴄ ᴡᴏʀᴅs ᴄᴘᴏʏʀɪɢʜᴛ ᴡᴏʀᴅs] ᴀɴᴅ ᴍᴀɴʏ ᴍᴏʀᴇ ɪᴜsᴛ ᴍᴀᴋᴇ ᴀᴅᴍɪɴ ᴏᴜʀ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ sᴇᴄᴜʀᴇ ɪᴛ ᴡɪᴛʜ ʜɪɢʜ sᴀғᴇᴛʏ🔐 """

@app.on_message(filters.command("start"))
async def start(_, msg):
    buttons = [
        
        [ 
          InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("• ʜᴀɴᴅʟᴇʀ •", callback_data="dil_back")
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://te.legra.ph/file/75f0e657402c53c23cdd1.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )


gd_buttons = [              
        [
            InlineKeyboardButton("ɢʀᴏᴜᴘ", url="https://t.me/Friend_Chat_International"),
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/acxbots"),    
        ]
        ]


# ------------------------------------------------------------------------------- #


@app.on_callback_query(filters.regex("dil_back"))
async def dil_back(_, query: CallbackQuery):
    await query.message.edit_caption(start_txt,
                                    reply_markup=InlineKeyboardMarkup(gd_buttons),)
        

# -------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------


start_time = time.time()

def time_formatter(milliseconds: float) -> str:
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"

def size_formatter(bytes: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0:
            break
        bytes /= 1024.0
    return f"{bytes:.2f} {unit}"



@app.on_message(filters.command("ping"))
async def activevc(_, message: Message):
    uptime = time_formatter((time.time() - start_time) * 1000)
    cpu = psutil.cpu_percent()
    storage = psutil.disk_usage('/')

    python_version = platform.python_version()

    reply_text = (
        f"➪ᴜᴘᴛɪᴍᴇ: {uptime}\n"
        f"➪ᴄᴘᴜ: {cpu}%\n"
        f"➪ꜱᴛᴏʀᴀɢᴇ: {size_formatter(storage.total)} [ᴛᴏᴛᴀʟ]\n"
        f"➪{size_formatter(storage.used)} [ᴜsᴇᴅ]\n"
        f"➪{size_formatter(storage.free)} [ғʀᴇᴇ]\n"
        f"➪ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ: {python_version},"
    )

    await message.reply(reply_text, quote=True)


    
# -------------------------------------------------------------------------------------



FORBIDDEN_KEYWORDS = ["porn", "xxx", "sex", "NCERT", "XII", "page", "Ans", "meiotic", "divisions", "System.in", "Scanner", "void", "nextInt"]

@app.on_message()
async def handle_message(client, message):
    if any(keyword in message.text for keyword in FORBIDDEN_KEYWORDS):
        logging.info(f"Deleting message with ID {message.id}")
        await message.delete()
      #  user_mention = from_user.mention
        await message.reply_text(f"@{message.from_user.username} 𝖣𝗈𝗇'𝗍 𝗌𝖾𝗇𝖽 𝗇𝖾𝗑𝗍 𝗍𝗂𝗆𝖾 otherwise you will be kicked!")
    elif any(keyword in message.caption for keyword in FORBIDDEN_KEYWORDS):
        logging.info(f"Deleting message with ID {message.id}")
        await message.delete()
       # user_mention = from_user.mention
        await message.reply_text(f"@{message.from_user.username} 𝖣𝗈𝗇'𝗍 𝗌𝖾𝗇𝖽 𝗇𝖾𝗑𝗍 𝗍𝗂𝗆𝖾 otherwise you will be kicked!")
        
        
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
@app.on_edited_message(filters.group & ~filters.me)
async def delete_edited_messages(client, edited_message):
    await edited_message.delete()



# ----------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
def delete_long_messages(_, m):
    return len(m.text.split()) > 50

@app.on_message(filters.group & filters.private & delete_long_messages)
async def delete_and_reply(_, msg):
    await msg.delete()
    user_mention = msg.from_user.mention
    await app.send_message(msg.chat.id, f"Hey {user_mention}, please keep your messages short!")
    

# -----------------------------------------------------------------------------------


    
@app.on_message(filters.animation | filters.audio | filters.document | filters.photo | filters.sticker | filters.video)
async def keep_reaction_message(client, message: Message):
    pass 
# -------------------------------

async def delete_pdf_files(client, message):
    if message.document and message.document.mime_type == "application/pdf":
        warning_message = f"@{message.from_user.username} ᴍᴀᴀ ᴍᴀᴛ ᴄʜᴜᴅᴀ ᴘᴅғ ʙʜᴇᴊ ᴋᴇ,\n ʙʜᴏsᴀᴅɪᴋᴇ ᴄᴏᴘʏʀɪɢʜᴛ ʟᴀɢʏᴇɢᴀ \n\n ᴅᴇʟᴇᴛᴇ ᴋᴀʀ ᴅɪʏᴀ ᴍᴀᴅᴀʀᴄʜᴏᴅ.\n\n ᴀʙ @kairnex ʙʜᴀɪ ᴋᴇ ᴅᴍ ᴍᴇ ᴀᴘɴɪ ᴍᴜᴍᴍʏ ᴋᴏ ʙʜᴇᴊ ᴅᴇ 🍌🍌🍌."
        await message.reply_text(warning_message)
        await message.delete()
    else:  
        pass

@app.on_message(filters.group & filters.document)
async def message_handler(client, message):
    await delete_pdf_files(client, message)

# ----------------------------------------
