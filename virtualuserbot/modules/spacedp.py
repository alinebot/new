import asyncio
import os
import random
import re
import urllib

import requests
from virtualuserbot import CMD_HELP
from virtualuserbot.utils import friday_on_cmd
from telethon.tl import functions

# Space lovers
COLLECTION_STRINGS = [
    "1920x1080-space-wallpapers",
    "4k-space-wallpaper",
    "cool-space-wallpapers-hd",
]


async def animepp():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRINGS) - 1)

    pack = COLLECTION_STRINGS[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile("/\w+/full.+.jpg")

    f = f.findall(pc)

    fy = "http://getwallpapers.com" + random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )

    urllib.request.urlretrieve(fy, "friday.jpg")


@friday.on(friday_on_cmd(pattern="spacedp ?(.*)"))
async def main(event):

    await event.edit(
        "**Starting Space Profile Pic...\n\nDone !!! Check Your DP"
    )  # Owner MarioDevs

    while True:

        await animepp()

        file = await event.client.upload_file("donottouch.jpg")

        await event.client(functions.photos.UploadProfilePhotoRequest(file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(3600)  # Edit this to your required needs


CMD_HELP.update(
    {
        "spacedp": "**Space Dp**\
\n\n**Syntax : **`.spacedp`\
\n**Usage :** uploades new space picture as your profile pic."
    }
)
