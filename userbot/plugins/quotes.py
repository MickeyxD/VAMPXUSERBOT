import random

import requests

from uniborg.util import VAMPBOT_cmd


@borg.on(VAMPBOT_cmd(pattern="quote ?(.*)"))
async def quote_search(event):
    if event.fwd_from:
        return
    await event.edit("Processing...")
    search_string = event.pattern_match.group(1)
    input_url = "https://bots.shrimadhavuk.me/Telegram/GoodReadsQuotesBot/?q={}".format(
        search_string
    )
    headers = {"USER-AGENT": "UniBorg"}
    try:
        response = requests.get(input_url, headers=headers).json()
    except:
        response = None
    if response is not None:
        result = (
            random.choice(response).get("input_message_content").get("message_text")
        )
    else:
        result = None
    if result:
        await event.edit(result.replace("<code>", "`").replace("</code>", "`"))
    else:
        await event.edit("Zero results found")
