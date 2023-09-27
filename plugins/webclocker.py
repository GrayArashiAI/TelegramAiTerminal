import io
import os
import time
import webbrowser
from core.core import *
from telegram import Update
from telegram.ext import ContextTypes
from pyautogui import typewrite, press, hotkey
from PIL import ImageGrab


async def screenshot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with io.BytesIO() as image:
        ImageGrab.grab(all_screens=True).save(image, "PNG")
        image.seek(0)
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=image)


async def webclocker(update: Update, context: ContextTypes.DEFAULT_TYPE):
    hotkey("ctrl", "alt")
    time.sleep(0.5)
    os.system("taskkill /F /IM chrome.exe")
    time.sleep(0.5)
    webbrowser.open("https://sites.google.com/k-cr.jp/k-net")
    press("tab")
    time.sleep(0.1)
    press("enter")
    time.sleep(0.1)
    time.sleep(8)
    for i in range(15):
        press("tab")
        time.sleep(0.1)
    press("enter")
    time.sleep(8)
    hotkey("ctrl", "shift", "1")
    typewrite("71903")
    press("tab")
    typewrite("zhangyiming")
    press("tab")
    await screenshot(update, context)


async def key(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = update.message.text.split()[1:]
    for s in args:
        arg = s.strip().lower()
        if "+" in arg:
            hotkey(*arg.split("+"))
            time.sleep(0.1)
        else:
            press(arg)
            time.sleep(0.1)
        time.sleep(1)
    await screenshot(update, context)


async def type(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.split(" ", 1)
    if len(text) > 1:
        typewrite(text[1])
        time.sleep(0.5)
        await screenshot(update, context)
    else:
        await update.message.reply_text("Empty text.")
