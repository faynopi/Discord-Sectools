#!/bin/env python3
#  _  _ _ _     _   ____      _____ __   __  _
# | || | | | __| |_|__ /_ _  |_   _/  \ /  \| |___
# | __ |_  _/ _| / /|_ \ '_|   | || () | () | (_-<
# |_||_| |_|\__|_\_\___/_|     |_| \__/ \__/|_/__/
#
# @Itsnexn & @Lixpy
# Github: https://github.com/Itsnexn/Discord-H4ck3rT00ls

import discord
from discord.ext import commands
from random import choice
from os import listdir
from random import choice

# Local librarys
from libs.cfg import get_config

# ==============================
# => Local variables
# ==============================

prefix = get_config("prefix")
tokenPath = get_config("tokenFile")
token = open(tokenPath, "r").readline()

commands.view._quotes = {}
commands.view._all_quotes = {}

bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")

# ==============================
# => Load Extensions
# ==============================

print("\n")
print("=" * 30)
print("Loading the extensions:")
print("=" * 30)

for extension in listdir("./cogs"):
    if extension.endswith(".py"):
        try:
            bot.load_extension(f"cogs.{extension[:-3]}")
            print(f"[Success] {extension} loaded successfully.")
        except Exception as e:
            print(f"[ERROR]\tAn error occurred while loading {extension}\n" + str(e) + "\n")



# ==============================
# => On Ready Event
# ==============================

@ bot.event
async def on_ready():
    print('Im ready!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"your command in {len(bot.guilds)} servers!"))

# Run the bot
bot.run(token)
