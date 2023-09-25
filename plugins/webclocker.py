import os
import time
import webbrowser
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


async def shukkin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    press("enter")
    await screenshot(update, context)


async def taikin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    press("tab")
    press("enter")
    await screenshot(update, context)
