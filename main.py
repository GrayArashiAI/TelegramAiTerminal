from core.core import *
from commands import *
from plugins.webclocker import *

(
    Bot("mybot")
    .addcmd(start=start)
    .addcmd(screenshot=screenshot)
    .addcmd(webclocker=webclocker)
    .addcmd(type=type)
    .addcmd(key=key)
).run()
