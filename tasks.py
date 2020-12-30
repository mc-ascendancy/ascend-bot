from discord.ext import tasks

import config

bot = config.bot


@tasks.loop(hours=72)
async def plasma_bot_maintenance():
    await bot.get_channel(734117420888883231).send(
        "<@&793981258291740723> Do `.invites`!"
    )
