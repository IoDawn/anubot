from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAIp9mBtwBBZGywWEmV-WC8gcMArjusuAAKMAgACTp1xV6m-mtC1YTfoHgQ")
    await message.reply_text(
        f"""**Hei {} Saya adalah *Roso* musik bot, selain Strong dan berEnergi Saya juga pandai bernyanyi🎙

Hubungi Owner saya jika Anda ingin menambahkan saya kedalam grup✔️
`Karena saat ini saya hanya tersedia untuk grup dibawah ini`⬇️        
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support Channel 🔊", url="https://t.me/arunasupportbot"
                    ),
                    InlineKeyboardButton(
                        "Help❔", url="https://telegra.ph/Command-Roso-Music-05-31"
                    ),
                    InlineKeyboardButton(
                        "Contact me 👤", url="https://t.me/assistenpokonya_bot"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Group Chat 🎙", url="https://t.me/vcg24jam"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Roso Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Help ❔", url="https://t.me/arunasupportbot/331")
                ]
            ]
        )
   )


