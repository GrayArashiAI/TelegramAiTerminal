from core.core import *
from commands import *

if __name__ == '__main__':
    mybot = Bot('mybot').addcmd(start=start).run()

