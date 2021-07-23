import discord
from discord.ext import commands
from libs.hashID import HashID
from libs.help import hashidHelp

class Hash_ID(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @ commands.command()
    async def hashid(self, ctx, *arg):
        if not arg:
            await ctx.channel.send(hashidHelp)
            return
        for i in arg[0:]:
            res = HashID(i)
            if not res:
                await ctx.channel.send(f"Hash (`{i}`) not found :(\n"+''.join(['-' for _ in range(45)]))
            else:
                if len(res) == 2:
                    msg = f"Two most possible types for `{i}` :\n1) {res[0]}\n2) {res[1]}\n"+''.join([
                                                                                                     '-' for _ in range(45)])
                    await ctx.channel.send(msg)
                elif len(res) == 1:
                    msg = f"Most possible type for `{i}` :\n1) {res[0]}\n"+''.join(
                        ['-' for _ in range(45)])
                    await ctx.channel.send(msg)
        return

def setup(bot):
    bot.add_cog(Hash_ID(bot))

