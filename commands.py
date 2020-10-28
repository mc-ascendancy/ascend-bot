import sys

import asyncio
import discord
import random

import config

bot = config.bot

# (bot) mods are the mods of the server and (bot) admins are the users
# in the Discord developer team

mod_ids = (
    305348568342855680,
    282513931854151681,
    355506351830597644,
    335394052834983938,
    355366164962082816
)


@bot.command(
    aliases=["latency"],
    hidden=True,
    help="Used to get the ping of the bot. "
         "(Only works when called by bot mods.)"
)
async def ping(ctx):
    if ctx.author.id not in mod_ids:
        return

    latency = round(bot.latency, 3) * 1000  # in ms to 3 d.p.

    await ctx.send(f"Pong! ({latency}ms)")


# closes the bot (only bot owners)
@bot.command(
    hidden=True,
    help="Used to terminate the bot. (Only works when called by bot admins.)"
)
async def cease(ctx):
    if not await bot.is_owner(ctx.author):
        return

    await ctx.send("Farewell...")
    print("Done.")

    await bot.close()
    sys.exit()


bot.remove_command("help")


@bot.command(
    name="help",
    aliases=["h"],
    help="Used for getting this message."
)
async def help_(ctx):
    commands_list = []

    for command in list(bot.commands):
        if not command.hidden:
            commands_list.append(command)

    commands_list.sort(key=lambda command_in: command_in.name)

    grouped_commands_list = [
        commands_list[i:i + 10] for i in range(0, len(commands_list), 10)
    ]

    pages = []

    i = 0
    total_pages = len(grouped_commands_list)

    for group in grouped_commands_list:
        page = discord.Embed(
            title=f"Commands",
            description=f"*Showing page {i + 1} of {total_pages}, "
                        f"use reactions to switch pages.*",
            color=0x9ab8d6
        )

        for command in group:
            page.add_field(
                name=command.name,
                value=command.help,
                inline=False
            )

        pages.append(page)

        i += 1

    n = 0

    help_message = await ctx.send(embed=pages[n])

    await help_message.add_reaction("◀️")
    await help_message.add_reaction("▶️")

    def check(reaction_in, user_in):
        return user_in == ctx.author and str(reaction_in.emoji) in ("◀️", "▶️")

    while True:
        try:
            reaction, user = await bot.wait_for(
                "reaction_add",
                check=check,
                timeout=90
            )

            if str(reaction.emoji) == "▶️":
                if n + 2 > total_pages:
                    pass
                else:
                    n += 1

                    await help_message.edit(embed=pages[n])

                await help_message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == "◀️":
                if n == 0:
                    pass
                else:
                    n -= 1

                    await help_message.edit(embed=pages[n])

                await help_message.remove_reaction(reaction, user)
            else:
                await help_message.remove_reaction(reaction, user)
        except asyncio.TimeoutError:
            break


@bot.command(
    name="mhelp",
    aliases=["mh"],
    help="Used for getting this message.",
    hidden=True
)
async def mod_help(ctx):
    commands_list = []

    for command in list(bot.commands):
        if command.hidden:
            commands_list.append(command)

    commands_list.sort(key=lambda command_in: command_in.name)

    grouped_commands_list = [
        commands_list[i:i + 10] for i in range(0, len(commands_list), 10)
    ]

    pages = []

    i = 0
    total_pages = len(grouped_commands_list)

    for group in grouped_commands_list:
        page = discord.Embed(
            title=f"Mod Commands",
            description=f"*Showing page {i + 1} of {total_pages}, "
                        f"use reactions to switch pages.*",
            color=0x9ab8d6
        )

        for command in group:
            page.add_field(
                name=command.name,
                value=command.help,
                inline=False
            )

        pages.append(page)

        i += 1

    n = 0

    help_message = await ctx.send(embed=pages[n])

    await help_message.add_reaction("◀️")
    await help_message.add_reaction("▶️")

    def check(reaction_in, user_in):
        return user_in == ctx.author and str(reaction_in.emoji) in ("◀️", "▶️")

    while True:
        try:
            reaction, user = await bot.wait_for(
                "reaction_add",
                check=check,
                timeout=90
            )

            if str(reaction.emoji) == "▶️":
                if n + 2 > total_pages:
                    pass
                else:
                    n += 1

                    await help_message.edit(embed=pages[n])

                await help_message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == "◀️":
                if n == 0:
                    pass
                else:
                    n -= 1

                    await help_message.edit(embed=pages[n])

                await help_message.remove_reaction(reaction, user)
            else:
                await help_message.remove_reaction(reaction, user)
        except asyncio.TimeoutError:
            break


# custom command
@bot.command(
    name="is",
    hidden=True,
    help="Used to set up <#734098917867782214>. "
         "(Only works when called by bot mods.)"
)
async def information_setup(ctx):
    if ctx.author.id not in mod_ids:
        return

    from information_channel import collection

    for embed in collection:
        await ctx.send(embed=embed)


@bot.command(
    name="rip",
    hidden=True,
    help="Used to refresh the polling in <#736325021856694385>. "
         "(Only works when called by bot mods.)"
)
async def refresh_ideas_polling(ctx, n):
    if ctx.author.id not in mod_ids:
        return

    ideas_channel = bot.get_channel(736325021856694385)

    if ctx.channel == ideas_channel:
        await ctx.message.delete()

    try:
        n = int(n)

        if n <= 0:
            raise ValueError
    except ValueError:
        return

    async for message in ideas_channel.history(limit=n):
        ok = False

        for reaction in message.reactions:
            if str(reaction.emoji) in (
                    "<:upvote:734576662229811230>",
                    "<:downvote:734576698217201674>"
            ) and reaction.me:
                ok = True

            if str(reaction.emoji) not in (
                    "<:upvote:734576662229811230>",
                    "<:downvote:734576698217201674>",
                    "⭐"
            ):
                await reaction.clear()

        if not ok:
            await message.add_reaction("<:upvote:734576662229811230>")
            await message.add_reaction("<:downvote:734576698217201674>")


@bot.command(
    name="cflip",
    aliases=["cf"],
    help="Used to flip a virtual coin."
)
async def coin_flip(ctx):
    if ctx.author.id in mod_ids:
        if not rigged_choice:
            choice = random.choice(("heads", "tails"))
        else:
            choice = rigged_choice
    else:
        choice = random.choice(("heads", "tails"))

    await ctx.send(f"The coin :coin: flipped on **{choice}**!")


rigged_choice = None


@bot.command(
    name="rcflip",
    hidden=True,
    aliases=["rcf"],
    help="Used to rig the coin flip command (short term). "
         "(Only works when called by bot mods.)"
)
async def rig_coin_flip(ctx, choice=None):
    global rigged_choice

    if not choice:
        rigged_choice = choice

        await ctx.send("👍")
    elif choice.lower().strip() in ("heads", "tails"):
        rigged_choice = choice

        await ctx.send("👍")
    else:
        return
