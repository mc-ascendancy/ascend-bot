import config

bot = config.bot


@bot.command()
async def ping(ctx):
    latency = round(bot.latency, 3) * 1000  # in ms to 3 d.p.

    await ctx.send(f"Pong! ({latency}ms)")


# closes the bot (only bot owners)
@bot.command(hidden=True)
async def cease(ctx):
    if not await bot.is_owner(ctx.author):
        return

    await ctx.send("Farewell...")
    print("Done.")

    await bot.close()
    config.sys.exit()


# custom command
@bot.command(hidden=True)
async def execute(ctx):
    if not await bot.is_owner(ctx.author):
        return

    from information_channel import collection

    for embed in collection:
        await ctx.send(embed=embed)
