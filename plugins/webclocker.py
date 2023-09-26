import os
import time
import webbrowser
from core.core import *
from telegram import Update
from telegram.ext import ContextTypes
from pyautogui import typewrite, press, hotkey
from PIL import ImageGrab


async def screenshot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    image_file = "image/screenshot.png"
    screenshot = ImageGrab.grab(all_screens=True)
    screenshot.save(image_file, "PNG")
    await context.bot.send_photo(
        chat_id=update.effective_chat.id, photo=open(image_file, "rb")
    )
    os.remove(image_file)


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


async def press(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = update.message.text.split()[1:]
    for s in args:
        arg = s.strip().lower
        try:
            if "+" in arg:
                hotkey(*arg.split("+"))
            else:
                press(arg)
            await screenshot(update, context)
        except Exception as e:
            await send_message(update, context, str(e))
    

async def input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.split("", 1)[1]
    try:
        typewrite(text)
        await screenshot(update, context)
    except Exception as e:
        await send_message(update, context, str(e))

