import discord
from discord.ext import commands
from random import choice
from os import environ

# Help Pages
from Help import *

# For Encoding and Decoding
from DecodeEncode import *

client = commands.Bot(command_prefix='$')
client.remove_command("help")


##############################
# Decrypt
##############################

@ client.command()
async def decrypt(ctx, *arg):
    if not arg:
        print("$decrypt Help massage sent")
        await ctx.send(decryptHelp)
    elif arg[0] == "b64":
        try:
            print(f"{' '.join(arg[1:])} decoded from base64")
            await ctx.send(f"\nHere you go: `{base64Decode(' '.join(arg[1:]))}`")
        except Exception:
            print(f"Sorry i couldn't decode the: {' '.join(arg[1:])}")
            await ctx.send(f"\nSorry i couldn't decode the: `{' '.join(arg[1:])}` as {arg[0]}\n try to read the $decrypt or $help for more information")

    elif arg[0] == "hex":
        try:
            print(f"{' '.join(arg[1:])} decoded from hex")
            await ctx.send(f"\nHere you go: `{hexDecode(' '.join(arg[1:]))}`")
        except Exception:
            print(f"Couldn't decode the: {' '.join(arg[1:])}")
            await ctx.send(f"\nSorry i couldn't decode the: `{' '.join(arg[1:])}` as {arg[0]}\n try to read the $decrypt or $help for more information")

    elif arg[0] == "rot13":
        try:
            print(f"{' '.join(arg[1:])} decoded from rot13")
            await ctx.send(f"\nHere you go: `{rot13Decode(' '.join(arg[1:]))}`")
        except Exception:
            print(f"Couldn't decode the: {' '.join(arg[1:])}")
            await ctx.send(f"\nSorry i couldn't decode the: `{' '.join(arg[1:])}` as {arg[0]}\n try to read the $decrypt or $help for more information")

    elif arg[0] == "url":
        try:
            print(f"{' '.join(arg[1:])} URL decoded")
            await ctx.send(f"\nHere you go: `{urlDecode(' '.join(arg[1:]))}`")
        except Exception:
            print(f"Couldn't decode the: {' '.join(arg[1:])}")
            await ctx.send(f"\nSorry i couldn't decode the: `{' '.join(arg[1:])}` as {arg[0]}\n try to read the $decrypt or $help for more information")
    return


##############################
# Encrypt
##############################

@ client.command()
async def encrypt(ctx, *arg):
    if not arg:
        print("$encrypt Help massage sended")
        await ctx.send(encryptHelp)
    elif arg[0] == "b64":
        try:
            print(f"{' '.join(arg[1:])} encoded from base64")
            await ctx.send(f"\nHere you go: `{base64Encode(' '.join(arg[1:]))}`")
        except Exception:
            print(f"Sorry i couldn't encode the: {' '.join(arg[1:])}")
            await ctx.send(f"\nSorry i couldn't encode the `{' '.join(arg[1:])}` to {arg[0]}\n try to read the $encrypt or $help for more information")

    elif arg[0] == "hex":
        try:
            print(f"{' '.join(arg[1:])} encoded to hex")
            await ctx.send(f"\nHere you go: `{hexEncode(' '.join(arg[1:]))}`")
        except Exception:
            print(f"Couldn't encode the: {' '.join(arg[1:])}")
            await ctx.send(f"\nSorry i couldn't encode the `{' '.join(arg[1:])}` to {arg[0]}\n try to read the $encrypt or $help for more information")

    elif arg[0] == "rot13":
        try:
            print(f"{' '.join(arg[1:])} encoded from rot13")
            await ctx.send(f"\nHere you go: `{rot13Encode(' '.join(arg[1:]))}`")
        except Exception:
            print(f"Couldn't decode the: {' '.join(arg[1:])}")
            await ctx.send(f"\nSorry i couldn't encode the `{' '.join(arg[1:])}` to {arg[0]}\n try to read the $encrypt or $help for more information")

    elif arg[0] == "url":
        try:
            print(f"{' '.join(arg[1:])} URL encoded")
            await ctx.send(f"\nHere you go: `{urlEncode(' '.join(arg[1:]))}`")
        except Exception:
            print(f"Couldn't encoded the: {' '.join(arg[1:])}")
            await ctx.send(f"\nSorry i couldn't encode the `{' '.join(arg[1:])}` to {arg[0]}\n try to read the $encrypt or $help for more information")
    return


##############################
# Bot info
##############################

@ client.command()
async def info(ctx):
    embed = discord.Embed(title="H4ck3r T00l",
                          description="A tool for hackers made by N00B5", color=0xe73232)
    embed.set_author(name="Join our discord server", url="https://discord.gg/aeay3v3cfX",
                     icon_url="https://github.com/Itsnexn/Discord-H4ck3rT00ls/blob/main/R3versePl4net_logo.jpg?raw=true")
    embed.set_thumbnail(
        url="https://raw.githubusercontent.com/Itsnexn/Discord-H4ck3rT00ls/main/logo.jpg")
    embed.add_field(name="$Github", value="Bot repo", inline=True)
    embed.add_field(name="launched at:", value="june 18th of 2021", inline=False)
    embed.add_field(name="Help Command:", value="$help", inline=True)
    embed.set_footer(text="Hack the planet | made by @itsnexn and @LixPy with ❤️")
    await ctx.send(embed=embed)
    return

##############################
# Help
##############################

@ client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="Need Help ?", description="These are our command!", color=0xe73232)
    embed.set_thumbnail(
        url="https://raw.githubusercontent.com/Itsnexn/Discord-H4ck3rT00ls/main/logo.jpg")
    embed.add_field(name="$decrypt",
                    value="arg[0]=type arg[1]=input | for more info use $decrypt", inline=False)
    embed.add_field(name="$encrypt",
                    value="arg[0]=type arg[1]=input | for more info  use $encrypt", inline=False)
    # embed.add_field(name="$hash", value="Hash identifier", inline=True)
    # embed.add_field(
        # name="$r3", value="arg[0]=type arg[1]=ip arg[3]=port | for more info use $r3", inline=False)
    # embed.add_field(name="$privesc",
                    # value="Show some cool scripts and commands for Privilege escalation", inline=False)
    # embed.add_field(name="$lfi", value="show lfi payloads", inline=False)
    embed.add_field(name="$info", value="Bot info", inline=False)
    embed.set_footer(text="Hack the planet | made by @itsnexn and @LixPy with ❤️")
    await ctx.author.send(embed=embed)
    await ctx.send("I send you the command list! check your DM...")
    return

"""
##############################
# Events
##############################

gretings = ["hi", "hello", "watsup", "yo"]
gretings_res = ["Hello!", "yo, wyd?", "Hey i heard you!", "Welcome back!"]

@ client.listen()
async def on_message(message):
    for greting in gretings:
        if greting in message.content.lower() and not message.author.bot:
            await message.channel.send(f"{message.author.mention}\n {choice(gretings_res)}")
            await client.process_commands(message)
"""

##############################
# On ready
##############################

@ client.event
async def on_ready():
    await client.change_presence(activity=discord.CustomActivity("Hello World", emoji="🖥️"))
    print('Im ready!')

client.run(environ['TOKEN'])
