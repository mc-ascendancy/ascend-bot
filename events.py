import config

import discord
import asyncio

bot = config.bot


@bot.event
async def on_ready():
    latency = round(bot.latency, 3) * 1000  # in ms to 3 d.p.

    print(f"Connected successfully as {bot.user} ({latency}ms).")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if bot.user in message.mentions:
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

    await bot.process_commands(message)


@bot.event
async def on_member_join(member):
    if member.guild.id != 732242190260109344:
        return

    await asyncio.sleep(5)

    await member.guild.system_channel.send(f"Hello **{member.name}**! o/")
