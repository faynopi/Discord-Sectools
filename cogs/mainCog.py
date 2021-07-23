import discord
from discord.ext import commands
from libs.hashID import HashID
from libs.help import hashidHelp

class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# ==============================
# => Bot info
# ==============================


    @ commands.command()
    async def info(self, ctx):
        embed = discord.Embed(title="H4ck3r T00l",
                              description="A tool for hackers made by N00B5", color=0xe73232)
        embed.set_author(name="Join our discord server", url="https://discord.gg/aeay3v3cfX",
                         icon_url="https://github.com/Itsnexn/Discord-H4ck3rT00ls/blob/main/R3versePl4net_logo.jpg?raw=true")
        embed.set_thumbnail(
            url="https://raw.githubusercontent.com/Itsnexn/Discord-H4ck3rT00ls/main/logo.jpg")
        embed.add_field(name="$Github", value="Bot repo", inline=True)
        embed.add_field(name="launched at:",
                        value="june 18th of 2021", inline=False)
        embed.add_field(name="Help Command:", value="$help", inline=True)
        embed.set_footer(
            text="Hack the planet | made by @itsnexn and @LixPy with ❤️")
        await ctx.send(embed=embed)
        return

# ==============================
# => Help Command
# ==============================


    @ commands.command(pass_context=True)
    async def help(self, ctx):
        embed = discord.Embed(title="Need Help ?",
                              description="These are our command!", color=0xe73232)
        embed.set_thumbnail(
            url="https://raw.githubusercontent.com/Itsnexn/Discord-H4ck3rT00ls/main/logo.jpg")
        embed.add_field(name="$decrypt",
                        value="arg[0]=type arg[1]=input | for more info use $decrypt", inline=False)
        embed.add_field(name="$encrypt",
                        value="arg[0]=type arg[1]=input | for more info  use $encrypt", inline=False)
        embed.add_field(name="$hashid", value="Hash identifier", inline=True)
        # embed.add_field(
        # name="$r3", value="arg[0]=type arg[1]=ip arg[3]=port | for more info use $r3", inline=False)
        # embed.add_field(name="$privesc",
        # value="Show some cool scripts and commands for Privilege escalation", inline=False)
        # embed.add_field(name="$lfi", value="show lfi payloads", inline=False)
        embed.add_field(name="$info", value="Bot info", inline=False)
        embed.set_footer(
            text="Hack the planet | made by @itsnexn and @LixPy with ❤️")
        await ctx.author.send(embed=embed)
        await ctx.send("I send you the command list! check your DM...")
        return

def setup(bot):
    bot.add_cog(Main(bot))
