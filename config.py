TOKEN = None

bot = None


def set_bot():
    import discord
    from discord.ext import commands

    global bot

    intents = discord.Intents().default()
    intents.members = True

    bot = commands.Bot(
        command_prefix="a!",
        intents=intents
    )


set_bot()

mod_ids = (
    305348568342855680,
    282513931854151681,
    355506351830597644,
    335394052834983938,
    355366164962082816
)
