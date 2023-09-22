from telegram import Update
from telegram.ext import ContextTypes

start_message = '''I'm a bot, please talk to me!'''

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=start_message)