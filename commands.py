import sys

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
    sys.exit()


# custom command
@bot.command(hidden=True)
async def execute(ctx):
    if not await bot.is_owner(ctx.author):
        return

    from information_channel import collection

    for embed in collection:
        await ctx.send(embed=embed)


@bot.command(
    hidden=True,
    aliases=["rip"]
)
async def refresh_ideas_polling(ctx, n):
    if not await bot.is_owner(ctx.author):
        return


    ideas_channel = bot.get_channel(736325021856694385)
    upvote_emoji = bot.get_emoji(734576662229811230)
    downvote_emoji = bot.get_emoji(734576698217201674)

    try:
        n = int(n)

        if n <= 0:
            raise ValueError
    except ValueError:
        await ctx.send("Invalid value.")

        return

    messages = await ideas_channel.history(limit=n).flatten()

    for message in messages:
        ok = False
        for reaction in message.reactions:
            if reaction.emoji in (
                    upvote_emoji, downvote_emoji
            ) and reaction.me:
                ok = True

            if reaction.emoji not in (upvote_emoji, downvote_emoji, "⭐"):
                await reaction.clear()

        if not ok:
            await message.add_reaction(upvote_emoji)
            await message.add_reaction(downvote_emoji)
