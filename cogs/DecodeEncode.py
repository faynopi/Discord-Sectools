import discord
from discord.ext import commands
from libs.decodeEncode import *
from libs.help import decodeHelp, encodeHelp


class DecodeEncode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ==============================
    # => decode
    # ==============================

    @ commands.command()
    async def decode(self, ctx, *arg):
        if not arg:
            print("$decode Help massage sent")
            await ctx.channel.send(decodeHelp)
        elif arg[0] == "b64":
            try:
                print(f"{' '.join(arg[1:])} decoded from base64")
                await ctx.channel.send(f"\nHere you go: `{base64Decode(' '.join(arg[1:]))}`")
            except Exception as e:
                print(f"Sorry i couldn't decode the: {' '.join(arg[1:])}")
                await ctx.channel.send(f"\nSorry i couldn't decode the: `{' '.join(arg[1:])}` as {arg[0]}\n \
                        try to read the $decode or $help for more information")

        elif arg[0] == "hex":
            try:
                if arg[1] != '-s':
                    print(f"{' '.join(arg[1:])} decoded from hex")
                    await ctx.channel.send(f"\nHere you go: `{hexDecode(' '.join(arg[1:]))}`")
                else:
                    print(f"{' '.join(arg[3:]).replace(arg[2],'')} decoded from hex")
                    await ctx.channel.send(f"\nHere you go: `{hexDecode(' '.join(arg[3:]).replace(arg[2],''))}`")
            except Exception as e:
                print(f"Couldn't decode the: {' '.join(arg[1:])}")
                await ctx.channel.send(f"\nSorry i couldn't decode the: `{' '.join(arg[1:])}` as {arg[0]}\n \
                        try to read the $decode or $help for more information")

        elif arg[0] == "rot13":
            try:
                print(f"{' '.join(arg[1:])} decoded from rot13")
                await ctx.channel.send(f"\nHere you go: `{rot13Decode(' '.join(arg[1:]))}`")
            except Exception as e:
                print(f"Couldn't decode the: {' '.join(arg[1:])}")
                await ctx.channel.send(f"\nSorry i couldn't decode the: `{' '.join(arg[1:])}` as {arg[0]}\n \
                        try to read the $decode or $help for more information")

        elif arg[0] == "url":
            try:
                print(f"{' '.join(arg[1:])} URL decoded")
                await ctx.channel.send(f"\nHere you go: `{urlDecode(' '.join(arg[1:]))}`")
            except Exception as e:
                print(f"Couldn't decode the: {' '.join(arg[1:])}")
                await ctx.channel.send(f"\nSorry i couldn't decode the: `{' '.join(arg[1:])}` as {arg[0]}\n \
                        try to read the $decode or $help for more information")
        return

    # ==============================
    # => encode
    # ==============================

    @ commands.command()
    async def encode(self, ctx, *arg):
        if not arg:
            print("$encode Help massage sent")
            await ctx.channel.send(encodeHelp)
        elif arg[0] == "b64":
            try:
                print(f"{' '.join(arg[1:])} encoded from base64")
                await ctx.channel.send(f"\nHere you go: `{base64Encode(' '.join(arg[1:]))}`")
            except Exception as e:
                print(f"Sorry i couldn't encode the: {' '.join(arg[1:])}")
                await ctx.channel.send(f"\nSorry i couldn't encode the `{' '.join(arg[1:])}` to {arg[0]}\n \
                        try to read the $encode or $help for more information")

        elif arg[0] == "hex":
            try:
                if arg[1] != '-s':
                    print(f"{' '.join(arg[1:])} encoded to hex")
                    await ctx.channel.send(f"\nHere you go: `{hexEncode(' '.join(arg[1:]))}`")
                else:
                    print(f"{' '.join(arg[3:])} encoded to hex")
                    tmp = str(hexEncode(' '.join(arg[3:])))
                    encodeed = ""
                    for i in range(0, len(tmp), 2):
                        encodeed += str(arg[2])
                        encodeed += tmp[i:i+2]
                    await ctx.channel.send(f"\nHere you go: `{encodeed}`")
            except Exception as e:
                print(f"Couldn't encode the: {' '.join(arg[1:])}")
                await ctx.channel.send(f"\nSorry i couldn't encode the `{' '.join(arg[1:])}` to {arg[0]}\n \
                        try to read the $encode or $help for more information")

        elif arg[0] == "rot13":
            try:
                print(f"{' '.join(arg[1:])} encoded from rot13")
                await ctx.channel.send(f"\nHere you go: `{rot13Encode(' '.join(arg[1:]))}`")
            except Exception as e:
                print(f"Couldn't decode the: {' '.join(arg[1:])}")
                await ctx.channel.send(f"\nSorry i couldn't encode the `{' '.join(arg[1:])}` to {arg[0]}\n \
                        try to read the $encode or $help for more information")
        elif arg[0] == "url":
            try:
                print(f"{' '.join(arg[1:])} URL encoded")
                await ctx.channel.send(f"\nHere you go: `{urlEncode(' '.join(arg[1:]))}`")
            except Exception as e:
                print(f"Couldn't encoded the: {' '.join(arg[1:])}")
                await ctx.channel.send(f"\nSorry i couldn't encode the `{' '.join(arg[1:])}` to {arg[0]}\n \
                        try to read the $encode or $help for more information")
        return


def setup(bot):
    bot.add_cog(DecodeEncode(bot))
