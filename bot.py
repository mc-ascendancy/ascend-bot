# Note: If you host the bot on Heroku (https://heroku.com/), you
# need to assign your Discord bot token to a Config Var named "TOKEN".


import sys
import os

# import discord
from discord.ext import commands
import logging


# look at line 75


def logging_setup():
    logger = logging.getLogger("discord")
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(
        filename="discord.log",
        encoding="utf-8",
        mode="a"
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s: %(message)s"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


def check_environment():
    global on_heroku

    if "DYNO" in os.environ:
        on_heroku = True
    else:
        on_heroku = False


def handle_token():
    if not on_heroku:
        choice = input(
            "Has token changed or NOT been set? (y/n) - "
        ).lower().strip(" ")

        if choice in ("y", "yes"):
            # sys.platform is current OS
            if sys.platform in ("win32", "linux", "darwin"):
                token_input = input("Input Discord bot token: ").strip(" ")
                cwd = os.getcwd()

                # creates a file called ".env" containing the bot token
                os.system(f"cmd /c cd {cwd} & echo TOKEN={token_input} > .env")

                del token_input
            else:
                print("Unsupported operating system.")
                sys.exit()
        elif choice in ("n", "no"):
            pass
        else:
            print("Invalid input, try again.")
            handle_token()

        from dotenv import load_dotenv

        load_dotenv()

    global TOKEN
    TOKEN = os.environ["TOKEN"]


logging_setup()

on_heroku = None
check_environment()

TOKEN = None
handle_token()

bot = commands.Bot(command_prefix="!a ")


@bot.event
async def on_ready():
    latency = round(bot.latency, 3) * 1000  # in ms to 3 d.p.

    print(f"Connected successfully as {bot.user} ({latency}ms).")


@bot.command()
async def ping(ctx):
    latency = round(bot.latency, 3) * 1000  # in ms to 3 d.p.

    await ctx.send(f"Pong! ({latency}ms)")


# closes the bot (only bot owners)
@bot.command(hidden=True)
async def cease(ctx):
    if await bot.is_owner(ctx.author):
        await ctx.send("Farewell...")
        print("Done.")

        await bot.close()
        sys.exit()


bot.run(TOKEN)
