# Credit: @r4v4n4
"""Emoji

Available Commands:

.fleave"""


import asyncio

from uniborg.util import VAMPBOT_cmd


@borg.on(VAMPBOT_cmd(pattern=r"fleave"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 17)

    # input_str = event.pattern_match.group(1)

    # if input_str == "fleave":

    await event.edit("fleave")

    animation_chars = [
        "⬛⬛⬛\n⬛⬛⬛\n⬛⬛⬛",
        "⬛⬛⬛\n⬛🔄⬛\n⬛⬛⬛",
        "⬛⬆️⬛\n⬛🔄⬛\n⬛⬛⬛",
        "⬛⬆️↗️\n⬛🔄⬛\n⬛⬛⬛",
        "⬛⬆️↗️\n⬛🔄➡️\n⬛⬛⬛",
        "⬛⬆️↗️\n⬛🔄➡️\n⬛⬛↘️",
        "⬛⬆️↗️\n⬛🔄➡️\n⬛⬇️↘️",
        "⬛⬆️↗️\n⬛🔄➡️\n↙️⬇️↘️",
        "⬛⬆️↗️\n⬅️🔄➡️\n↙️⬇️↘️",
        "↖️⬆️↗️\n⬅️🔄➡️\n↙️⬇️↘️",
        "**Chat Message Exported To** `./Inpu/`",
        "**Chat Message Exported To** `./Inpu/homework/`",
        "**Chat Message Exported To** `./Inpu/homework/groupchat.txt`",
        "__Legend is leaving this chat.....! ",
        "__Legend is leaving this chat.....!",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 17])
