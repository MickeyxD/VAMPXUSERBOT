"""Send Chat Actions
Syntax: .sca <option> <time in sec>
        sca options: Options for sca 

typing
contact
game
location
voice
round
video
photo
document
cancel"""

import asyncio

from uniborg.util import VAMPBOT_cmd


@borg.on(VAMPBOT_cmd("sca ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    input_str = event.pattern_match.group(1)
    action = "typing"
    if input_str:
        action = input_str
    async with borg.action(event.chat_id, action):
        await asyncio.sleep(86400)  # type for 10 seconds
