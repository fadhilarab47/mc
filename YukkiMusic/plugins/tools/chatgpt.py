import requests
from pyrogram import Client, filters
from pyrogram.enums import ChatAction
from TheApi import api

from YukkiMusic import app


@app.on_message(
    filters.command(["chatgpt", "ai", "ask"], prefixes=["+", ".", "/", "-", "?", "$", "#", "&"] ~filters.private)
)
async def chatgpt_chat(bot, message):
    if len(message.command) < 2 and not message.reply_to_message:
        await message.reply_text(
            "Example:\n\n`/ai write simple website code using html, css, js?`"
        )
        return

    # Determine the user input
    if message.reply_to_message and message.reply_to_message.text:
        user_input = message.reply_to_message.text
    else:
        user_input = " ".join(message.command[1:])

    try:
        # Indicate that the bot is typing
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        # Send the request to the API
        results = api.chatgpt(user_input)
        # Check if the API call was successful and respond with the result
        if results["success"]:
            await message.reply_text(results["results"])
    except requests.exceptions.RequestException as e:
        await message.reply_text("There was an error processing your request. Please try again later.")


__MODULE__ = "ChatGPT"
__HELP__ = """
/advice - Get random advice from the bot
/ai [query] - Ask your question using ChatGPT's AI
/gemini [query] - Ask your question using Google's Gemini AI
/bard [query] - Ask your question using Google's Bard AI
"""
