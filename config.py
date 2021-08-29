TOKEN = None

bot = None


def set_bot():
    import discord
    from discord.ext import commands

    global bot

    intents = discord.Intents.default()
    intents.members = True

    bot = commands.Bot(
        command_prefix="a!",
        intents=intents
    )

    bot.allowed_mentions = discord.AllowedMentions(
        everyone=False,
        users=True,
        roles=False,
        replied_user=True
    )


set_bot()
