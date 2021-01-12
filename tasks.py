import discord
from discord.ext import tasks

import config
import events
import commands

bot = config.bot


@tasks.loop(minutes=5)
async def clear_already_used():
    events.already_used = []


@tasks.loop(hours=24)
async def set_nickname():
    for guild in bot.guilds:
        try:
            await guild.me.edit(nick=f"{bot.user.name} | {bot.command_prefix}")
        except discord.Forbidden:
            pass


@tasks.loop(hours=72)
async def plasma_bot_maintenance():
    await bot.get_channel(734117420888883231).send(
        "<@&793981258291740723> Do `.invites`!"
    )


@tasks.loop(minutes=5)
async def refresh_ideas_polling():
    await commands.refresh_ideas_polling(5)
