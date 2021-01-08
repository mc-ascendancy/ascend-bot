import discord
import asyncio
import random

import config
import commands

bot = config.bot
mod_ids = commands.mod_ids


@bot.event
async def on_ready():
    import tasks

    tasks.set_privileged_ids.start()
    tasks.clear_already_used.start()
    tasks.set_nickname.start()
    tasks.plasma_bot_maintenance.start()

    latency = round(bot.latency, 3) * 1000  # in ms to 3 d.p.

    await bot.get_channel(734108139158241320).send(
        f"Connected successfully ({latency}ms)."
    )

    print(f"Connected successfully as {bot.user} ({latency}ms).")


# contains the IDs of users that have already used the bot ping
# functionality once within a set time period
already_used = []


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if bot.user in message.mentions and message.author.id not in already_used:
        already_used.append(message.author.id)

        await message.channel.send(
            f"Hello! Use `{bot.command_prefix}help` to check out my commands!"
        )

    if message.channel.id == 736325021856694385:  # ideas channel
        if not message.content.startswith(bot.command_prefix):
            await message.add_reaction("<:upvote:734576662229811230>")
            await message.add_reaction("<:downvote:734576698217201674>")

    if message.guild.id == 732242190260109344:
        if message.channel == message.guild.system_channel:
            if message.type in (
                    discord.MessageType.premium_guild_subscription,
                    discord.MessageType.premium_guild_tier_1,
                    discord.MessageType.premium_guild_tier_2,
                    discord.MessageType.premium_guild_tier_3
            ):
                await asyncio.sleep(5)

                await message.channel.send(
                    f"Thank you **{message.author.name}**! "
                    f"<:swaghappy:734034994108039178>"
                )

        if message.author.id in mod_ids:
            if message.content.startswith("!!"):
                if message.content[2:6].rstrip() in ("warn", "mute", "ban"):
                    await message.add_reaction("<:mod:772893560949047378>")

        if random.randrange(420) == 69:
            await message.add_reaction("<:famcat:788538192004775957>")

    await bot.process_commands(message)


@bot.event
async def on_member_join(member):
    if member.guild.id != 732242190260109344:
        return

    await asyncio.sleep(5)

    await member.guild.system_channel.send(f"Hello **{member.name}**! o/")
