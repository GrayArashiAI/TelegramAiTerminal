from core.core import run_bot, Bot
from commands import *

if __name__ == '__main__':
    mybot = Bot('mybot').addcmd(start=start).run()