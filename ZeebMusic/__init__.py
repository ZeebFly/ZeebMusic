#
# Copyright (C) 2024-2025 by TheTeamVivek@Github, < https://github.com/TheTeamVivek >.
#
# This file is part of < https://github.com/TheTeamVivek/ZeebMusic > project,
# and is released under the MIT License.
# Please see < https://github.com/TheTeamVivek/ZeebMusic/blob/master/LICENSE >
#
# All rights reserved.
import asyncio as _asyncio

import asyncio

try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except Exception:
    pass

try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

from ZeebMusic.core.bot import YukkiBot
from ZeebMusic.core.dir import dirr
from ZeebMusic.core.git import git
from ZeebMusic.core.userbot import Userbot
from ZeebMusic.misc import dbb, heroku

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

app = YukkiBot()
userbot = Userbot()

HELPABLE = {}
