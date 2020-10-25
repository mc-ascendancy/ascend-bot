import config

bot = config.bot


@bot.event
async def on_ready():
    latency = round(bot.latency, 3) * 1000  # in ms to 3 d.p.

    print(f"Connected successfully as {bot.user} ({latency}ms).")


@bot.event
async def on_message(message):
    ideas_channel = bot.get_channel(736325021856694385)
    upvote_emoji = bot.get_emoji(734576662229811230)
    downvote_emoji = bot.get_emoji(734576698217201674)

    if message.channel == ideas_channel:
        await message.add_reaction(upvote_emoji)
        await message.add_reaction(downvote_emoji)

    await bot.process_commands(message)


@bot.event
async def on_reaction_add(reaction, _):
    ideas_channel = bot.get_channel(736325021856694385)
    upvote_emoji = bot.get_emoji(734576662229811230)
    downvote_emoji = bot.get_emoji(734576698217201674)

    if reaction.message.channel == ideas_channel:
        if reaction.emoji not in (upvote_emoji, downvote_emoji, "⭐"):
            await reaction.clear()
