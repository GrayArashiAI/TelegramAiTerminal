import os
import glob
import yaml
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update


def load_config(config: dict = {}):
    for yaml_file in glob.glob(os.path.join(os.getcwd(), "config*.yaml")):
        with open(yaml_file, "r") as y:
            config.update(yaml.safe_load(y))
    return config


def run_bot(bot_name: str, **command_list: dict[str, callable]):
    config = load_config()[bot_name]
    app = ApplicationBuilder().token(config["TOKEN"]).build()
    for cmd, function in command_list.items():
        app.add_handler(CommandHandler(cmd, function))
    app.run_polling()


async def send_message(update: Update, context: ContextTypes.DEFAULT_TYPE, text):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)


class Bot:
    def __init__(self, bot_name: str):
        self.config = load_config()[bot_name]
        self.app = ApplicationBuilder().token(self.config["TOKEN"]).build()

    def addcmd(self, **command_list: dict[str, callable]):
        for cmd, function in command_list.items():
            self.app.add_handler(CommandHandler(cmd, function))
        return self

    def run(self):
        self.app.run_polling()
