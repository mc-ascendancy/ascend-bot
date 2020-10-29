import config

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

    await bot.process_commands(message)
