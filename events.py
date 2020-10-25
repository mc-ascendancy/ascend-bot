import config

bot = config.bot


@bot.event
async def on_ready():
    latency = round(bot.latency, 3) * 1000  # in ms to 3 d.p.

    print(f"Connected successfully as {bot.user} ({latency}ms).")


@bot.event
async def on_message(message):
    if message.channel == bot.get_channel(736325021856694385):
        await message.add_reaction("<:upvote:734576662229811230>")
        await message.add_reaction("<:downvote:734576698217201674>")

    await bot.process_commands(message)
