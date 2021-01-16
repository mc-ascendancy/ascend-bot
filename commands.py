import sys

import asyncio
import discord
from discord.ext import commands
import random
import textwrap
from num2words import num2words

import config

bot = config.bot


def get_mods():
    return bot.get_guild(
        732242190260109344
    ).get_role(
        734097025574109274
    ).members


def get_staff():
    return bot.get_guild(
        732242190260109344
    ).get_role(
        734100717874446396
    ).members


# (bot) mods are the mods of the server and (bot) admins are the users
# in the Discord developer team


@bot.command(
    aliases=["latency"],
    hidden=True,
    help="Used to get the ping of the bot."
)
async def ping(ctx):
    if ctx.author not in get_mods() and not await bot.is_owner(ctx.author):
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


def help_pages(mod):
    commands_list = []

    for command in bot.commands:
        if not mod:
            if not command.hidden:
                commands_list.append(command)
        else:
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
            title=f"Commands",
            color=0x9ab8d6
        ).set_footer(
            text=f"Showing page {i + 1} of {total_pages}, "
                 f"use reactions to switch pages."
        )

        for command in group:
            page.add_field(
                name=command.name,
                value=(
                        command.help +
                        (
                            f"\n*Usage:* `{command.usage}`" if command.usage
                            else ""
                        ) +
                        (
                            f"\n*Alias"
                            f"{'' if len(command.aliases) == 1 else 'es'}"
                            f":* `{'`, `'.join(command.aliases)}`"
                            if command.aliases
                            else ""
                        )
                ),
                inline=False
            )

        pages.append(page)

        i += 1

    return pages


bot.remove_command("help")


@bot.command(
    name="help",
    aliases=["h"],
    help="Used for getting this message."
)
@commands.cooldown(1, 5, type=commands.BucketType.user)
@commands.max_concurrency(1, per=commands.BucketType.user)
async def help_(ctx):
    pages = help_pages(False)
    total_pages = len(pages)

    n = 0

    help_message = await ctx.send(embed=pages[n])

    react_emotes = ("◀️", "❌", "▶️")

    for react_emote in react_emotes:
        await help_message.add_reaction(react_emote)

    def check(reaction_in, user_in):
        return user_in == ctx.author and str(reaction_in) in react_emotes

    while True:
        try:
            reaction, user = await bot.wait_for(
                "reaction_add",
                check=check,
                timeout=60
            )

            if str(reaction) == "▶️":
                if n + 2 > total_pages:
                    pass
                else:
                    n += 1

                    await help_message.edit(embed=pages[n])

                await help_message.remove_reaction(reaction, user)
            elif str(reaction) == "◀️":
                if n == 0:
                    pass
                else:
                    n -= 1

                    await help_message.edit(embed=pages[n])

                await help_message.remove_reaction(reaction, user)
            elif str(reaction) == "❌":
                await help_message.clear_reactions()

                break
            else:
                await help_message.remove_reaction(reaction, user)
        except asyncio.TimeoutError:
            await help_message.clear_reactions()

            break


@bot.command(
    name="mhelp",
    aliases=["mh"],
    help="Used for getting this message.",
    hidden=True
)
@commands.cooldown(1, 5, type=commands.BucketType.user)
@commands.max_concurrency(1, per=commands.BucketType.user)
async def mod_help(ctx):
    if ctx.author not in get_staff() and not await bot.is_owner(ctx.author):
        return

    pages = help_pages(True)
    total_pages = len(pages)

    n = 0

    help_message = await ctx.send(embed=pages[n])

    react_emotes = ("◀️", "❌", "▶️")

    for react_emote in react_emotes:
        await help_message.add_reaction(react_emote)

    def check(reaction_in, user_in):
        return user_in == ctx.author and str(reaction_in) in react_emotes

    while True:
        try:
            reaction, user = await bot.wait_for(
                "reaction_add",
                check=check,
                timeout=60
            )

            if str(reaction) == "▶️":
                if n + 2 > total_pages:
                    pass
                else:
                    n += 1

                    await help_message.edit(embed=pages[n])

                await help_message.remove_reaction(reaction, user)
            elif str(reaction) == "◀️":
                if n == 0:
                    pass
                else:
                    n -= 1

                    await help_message.edit(embed=pages[n])

                await help_message.remove_reaction(reaction, user)
            elif str(reaction) == "❌":
                await help_message.clear_reactions()

                break
            else:
                await help_message.remove_reaction(reaction, user)
        except asyncio.TimeoutError:
            await help_message.clear_reactions()

            break


# custom command
@bot.command(
    name="is",
    hidden=True,
    help="Used to set up <#734098917867782214>."
)
async def information_setup(ctx):
    if ctx.author not in get_mods() and not await bot.is_owner(ctx.author):
        return

    from information_channel import collection

    for embed in collection:
        await ctx.send(embed=embed)


@bot.command(
    name="cflip",
    aliases=["cf"],
    help="Used to flip a virtual coin."
)
async def coin_flip(ctx):
    if ctx.author in get_mods() or await bot.is_owner(ctx.author):
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
    help="Used to rig the coin flip command (short term)."
)
async def rig_coin_flip(ctx, choice=None):
    if ctx.author not in get_mods() and not await bot.is_owner(ctx.author):
        return

    global rigged_choice

    if not choice:
        rigged_choice = choice

        await ctx.send("👍")
    elif choice.lower().strip() in ("heads", "tails"):
        rigged_choice = choice

        await ctx.send("👍")
    else:
        return


@bot.command(
    name="mode",
    hidden=True,
    aliases=["m"],
    help="Used for enabling, disabling, and getting the statuses of modes.",
    usage=f"{bot.command_prefix}mode [game nights] [enable/disable]"
)
async def mode_(ctx, *, args):
    if ctx.author not in get_mods() and not await bot.is_owner(ctx.author):
        return

    args_list = args.split(" ")

    mode = " ".join(args_list[:-1]).strip().lower()
    method = args_list[-1].strip().lower()

    if method not in ("enable", "on", "disable", "off", "status"):
        return

    guild = bot.get_guild(732242190260109344)

    if mode in ("game nights", "gn"):
        game_nights_role = guild.get_role(778500719292186635)
        member_role = guild.get_role(734096990396350515)
        muted_role = guild.get_role(734219419760328716)
        game_nights_category = guild.get_channel(779386959897296927)

        overwrite = discord.PermissionOverwrite
        enabled_overwrites = {
            game_nights_role: overwrite(read_messages=None),
            member_role: overwrite(read_messages=None),
            muted_role: overwrite(
                send_messages=False,
                add_reactions=False,
                speak=False
            )
        }
        disabled_overwrites = {
            game_nights_role: overwrite(read_messages=True),
            member_role: overwrite(read_messages=False),
            muted_role: overwrite(
                send_messages=False,
                add_reactions=False,
                speak=False
            )
        }

        if method in ("enable", "on"):
            await game_nights_role.edit(colour=0x8fbbda)
            await game_nights_category.edit(
                overwrites=enabled_overwrites
            )

            for channel in game_nights_category.channels:
                await channel.edit(sync_permissions=True)

            await ctx.message.add_reaction("✅")
        elif method in ("disable", "off"):
            await game_nights_role.edit(colour=0x000000)
            await game_nights_category.edit(
                overwrites=disabled_overwrites
            )

            for channel in game_nights_category.channels:
                await channel.edit(sync_permissions=True)

            await ctx.message.add_reaction("✅")
        elif method == "status":
            async def send_embed(value):
                await ctx.send(
                    embed=discord.Embed(
                        title="`Game Nights` Mode",
                        colour=0x9ab8d6
                    ).add_field(
                        name="Status",
                        value=value
                    )
                )

            enabled_channels_count = 0

            for channel in game_nights_category.channels:
                if channel.overwrites == disabled_overwrites:
                    pass
                elif channel.overwrites == enabled_overwrites:
                    enabled_channels_count += 1
                else:
                    await send_embed("N/A")

                    return

            if enabled_channels_count == 0:
                channel_status = False
            elif enabled_channels_count == len(game_nights_category.channels):
                channel_status = True
            else:
                await send_embed("N/A")

                return

            if game_nights_role.colour.value == 0x8fbbda:
                colour_status = True
            elif game_nights_role.colour.value == 0x000000:
                colour_status = False
            else:
                await send_embed("N/A")

                return

            if channel_status != colour_status:
                await send_embed("N/A")

                return

            await send_embed("Enabled" if channel_status else "Disabled")


async def refresh_ideas_polling(number):
    async for message in bot.get_channel(736325021856694385).history(
            limit=number if number != 0 else None
    ):
        upvote = None
        downvote = None

        upvoted = None
        downvoted = None

        users_up = set()
        users_down = set()

        d = {}

        for reaction in message.reactions:
            emote = str(reaction)

            if emote not in (
                    "<:upvote:734576662229811230>",
                    "<:downvote:734576698217201674>",
                    "⭐",
                    "✅",
                    "⌛",
                    "☑️",
                    "❌"
            ):
                await reaction.clear()
            else:
                author = message.author
                users = await reaction.users().flatten()

                if author in users and author not in get_staff():
                    await reaction.remove(author)

                if emote == "<:upvote:734576662229811230>":
                    upvote = reaction

                    users_up = set(users)

                    if reaction.me:
                        upvoted = True
                elif emote == "<:downvote:734576698217201674>":
                    downvote = reaction

                    users_down = set(users)

                    if reaction.me:
                        downvoted = True
                elif emote in ("✅", "⌛", "☑️", "❌"):
                    if len(
                            set(
                                await reaction.users().flatten()
                            ).intersection(set(get_staff()))
                    ) != 0:
                        d.update({emote: reaction})
                    else:
                        await reaction.clear()

        if len(d) > 1:
            if "✅" in d:
                d.pop("✅")

                for reaction in d.values():
                    await reaction.clear()
            elif "⌛" in d:
                d.pop("⌛")

                for reaction in d.values():
                    await reaction.clear()
            elif "☑️" in d:
                d.pop("☑️")

                for reaction in d.values():
                    await reaction.clear()

        if not (upvoted and downvoted):
            try:
                await message.add_reaction(
                    "<:upvote:734576662229811230>"
                )
                await message.add_reaction(
                    "<:downvote:734576698217201674>"
                )
            except discord.Forbidden as error:
                if error.code != 90001:
                    raise error

                await message.delete()

                continue

        united = users_up.intersection(users_down)
        united.discard(bot.user)

        for user in united:
            await upvote.remove(user)

            await downvote.remove(user)


@bot.command(
    name="ideas",
    aliases=["i"],
    help="Used for doing various things with <#736325021856694385>. "
         "(`refresh` only usable by mods.)",
    usage=f"{bot.command_prefix}ideas "
          f"[refresh/list] "
          f"[number|upvotes/downvotes/points] [ascending/descending] "
          "{implemented/in progress/approved/neutral/rejected}"
)
@commands.cooldown(1, 30, type=commands.BucketType.user)
@commands.max_concurrency(1, per=commands.BucketType.user)
async def ideas_(ctx, function, *, args):
    author = ctx.author

    ideas_channel = bot.get_channel(736325021856694385)

    args_list = args.split(" ")

    if function.lower() in ("refresh", "r"):
        if author not in get_mods() and not await bot.is_owner(author):
            return

        if len(args_list) != 1:
            return

        n = args_list[0]

        if not n.isdigit():
            return

        await refresh_ideas_polling(int(n))

        await ctx.message.add_reaction("✅")

        if ctx.channel == ideas_channel:
            await asyncio.sleep(5)

            await ctx.message.delete()
    elif function.lower() in ("list", "l"):
        if len(args_list) < 2:
            return
        elif len(args_list) == 2:
            fltr = None
        else:
            fltr = " ".join(args_list[2:])

        criteria = args_list[0]
        order = args_list[1]

        if criteria not in ("u", "upvotes", "d", "downvotes", "p", "points"):
            return

        if order in ("a", "asc", "ascending"):
            desc_order = False
        elif order in ("d", "desc", "descending"):
            desc_order = True
        else:
            return

        if not fltr:
            pass
        elif fltr.lower() == "implemented":
            pass
        elif fltr.lower() == "in progress":
            pass
        elif fltr.lower() == "approved":
            pass
        elif fltr.lower() == "neutral":
            pass
        elif fltr.lower() == "rejected":
            pass
        else:
            return

        messages = await ideas_channel.history(limit=None).flatten()

        def get_reaction_count(msg, emt):
            reacts = {str(react): react for react in msg.reactions}

            return reacts[emt].count

        message_values = {}

        for message in messages:
            upvotes = get_reaction_count(
                message,
                "<:upvote:734576662229811230>"
            )
            downvotes = get_reaction_count(
                message,
                "<:downvote:734576698217201674>"
            )

            status = None

            t = 0

            for reaction in message.reactions:
                emote = str(reaction)

                if emote == "✅":
                    status = "implemented"

                    t += 1
                elif emote == "⌛":
                    status = "in progress"

                    t += 1
                elif emote == "☑️":
                    status = "approved"

                    t += 1
                elif emote == "❌":
                    status = "rejected"

                    t += 1

            if t == 0:
                status = "neutral"
            elif t != 1:
                status = "N/A"

            message_values.update(
                {
                    message: (
                        upvotes,  # 0 - upvotes
                        downvotes - 1,  # 1 - downvotes
                        upvotes - (downvotes - 1),  # 2 - points
                        status  # 3 - status
                    )
                }
            )

        if criteria.lower() in ("u", "upvotes"):
            criteria = "u"

            messages.sort(
                reverse=desc_order,
                key=lambda msg: (message_values[msg][0], message.created_at)
            )
        elif criteria.lower() in ("d", "downvotes"):
            criteria = "d"

            messages.sort(
                reverse=desc_order,
                key=lambda msg: (message_values[msg][1], message.created_at)
            )
        elif criteria.lower() in ("p", "points"):
            criteria = "p"

            messages.sort(
                reverse=desc_order,
                key=lambda msg: (message_values[msg][2], message.created_at)
            )
        else:
            return

        if fltr:
            messages = list(
                filter(
                    lambda msg: (
                        True if message_values[msg][3] == fltr else False
                    ),
                    messages
                )
            )

        grouped_messages = [
            messages[i:i + 10] for i in range(0, len(messages), 10)
        ]

        pages = []

        i = 0

        total_pages = len(grouped_messages)

        criteria_index = {
            "u": "upvotes",
            "d": "downvotes",
            "p": "points"
        }

        for group in grouped_messages:
            page = discord.Embed(
                title=f"Ideas",
                description=(
                    f"*Sorted by **{criteria_index[criteria]}** in **"
                    f"{'descending' if desc_order else 'ascending'}**"
                    f" order"
                    f"{' and filtered by status' if fltr else ''}"
                    f"{' (**' + fltr + '**)' if fltr else ''}"
                    f".*"
                ),
                color=0x9ab8d6
            ).set_footer(
                text=f"Showing page {i + 1} of {total_pages}, "
                     f"use reactions to switch pages."
            )

            for message in group:
                index = messages.index(message)

                page.add_field(
                    name=(
                        f"{num2words(index + 1, to='ordinal_num')} "
                        f"by {message.author.name} "
                        f"(on {message.created_at.strftime('%d %b %Y')})"
                    ),
                    value=(
                        f"{textwrap.shorten(message.content, 450)}\n"
                        f"([here]({message.jump_url}))\n\n"
                        f"*Upvotes: `{message_values[message][0]}` • "
                        f"Downvotes: `{message_values[message][1]}` • "
                        f"Points: `{message_values[message][2]}` • "
                        f"Status: `{message_values[message][3]}`*"
                    ),
                    inline=False
                )

            pages.append(page)

            i += 1

        n = 0

        ideas_message = await ctx.send(embed=pages[n])

        react_emotes = ("◀️", "❌", "▶️")

        for react_emote in react_emotes:
            await ideas_message.add_reaction(react_emote)

        def check(reaction_in, user_in):
            return user_in == ctx.author and str(reaction_in) in react_emotes

        while True:
            try:
                reaction, user = await bot.wait_for(
                    "reaction_add",
                    check=check,
                    timeout=300
                )

                if str(reaction) == "▶️":
                    if n + 2 > total_pages:
                        pass
                    else:
                        n += 1

                        await ideas_message.edit(embed=pages[n])

                    await ideas_message.remove_reaction(reaction, user)
                elif str(reaction) == "◀️":
                    if n == 0:
                        pass
                    else:
                        n -= 1

                        await ideas_message.edit(embed=pages[n])

                    await ideas_message.remove_reaction(reaction, user)
                elif str(reaction) == "❌":
                    await ideas_message.clear_reactions()

                    break
                else:
                    await ideas_message.remove_reaction(reaction, user)
            except asyncio.TimeoutError:
                await ideas_message.clear_reactions()

                break


@bot.command(
    name="stats",
    help="Used for getting the Minecraft server stats, for example "
         "the TPS.",
    aliases=["s"]
)
async def stats_(_):
    # this is implemented on the instance
    # running on the Minecraft server
    return


@bot.command(
    name="nation_lookup",
    help="Used for looking up nations. "
         "(Only works when called in <#734117420888883231>.)",
    aliases=["nl"],
    hidden=True
)
async def nation_lookup_(_):
    # this is implemented on the instance
    # running on the Minecraft server
    return


@bot.command(
    name="player_lookup",
    help="Used for looking up players. "
         "(Only works when called in <#734117420888883231>.)",
    aliases=["pl"],
    hidden=True
)
async def player_lookup_(_):
    # this is implemented on the instance
    # running on the Minecraft server
    return


@bot.command(
    name="astats",
    help="Used for getting the Minecraft server stats for admins. "
         "(Only works when called in <#734117420888883231>.)",
    aliases=["adminstats", "as"],
    hidden=True
)
async def admin_stats_(_):
    # this is implemented on the instance
    # running on the Minecraft server
    return
