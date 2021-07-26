import discord
from discord.ext import commands
from libs.r3vShell import nameSearch, osSearch, r3vIt, list
from libs.help import r3vHelp
from libs.cfg import get_config


class R3v(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @ commands.command()
    async def r3v(self, ctx, *arg):
        if not arg:
            print("$r3v Help massage sent")
            await ctx.channel.send(r3vHelp)
        elif arg[0].lower() == "search":
            try:
                t = "".join(arg[1:])
                newline = "\n"
                await ctx.channel.send(f"""```{newline.join(nameSearch(t))}```""")
            except Exception as e:
                await ctx.channel.send("Unexpected Error!\nread $r3v for more information.")
                print(f"Unexpected Error! in {__name__}\nError msg:{e}")

        elif arg[0].lower() == "list":
            try:
                newline = "\n"
                await ctx.channel.send(f"""```{newline.join(list())}```""")
            except Exception as e:
                await ctx.channel.send("Unexpected Error!")
                print(f"Unexpected Error! in {__name__}\nError msg:{e}")

        elif arg[0].lower() == "os":
            try:
                t = "".join(arg[1:])
                newline = "\n"
                if osSearch(t) == False:
                    await ctx.channel.send("Unexpected Error!\nPlease use valid os name for this action...\n```[windows, linux, mac]```read $r3v for more information.")
                else:
                    await ctx.channel.send(f"""```{newline.join(osSearch(t))}```""")
            except Exception as e:
                await ctx.channel.send("Unexpected Error!")
                print(f"Unexpected Error! in {__name__}\nError msg:{e}")

        elif arg[0].lower() == "gen":
            try:
                print(arg)
                print(len(arg))
                name = arg[1]
                ip = arg[2]
                port = arg[3]

                # Check if shell argument is set
                # why this checking if arg is bigger then 4? because len of the tuple will
                # check number of item in tuple but it will start from 1
                # Example: len(("1", "2", "3", "4", "5")) will return 5
                if len(arg) > 4:
                    shell = "".join(arg[4:])

                # if shell isnt set change it to default Shell value
                else:
                    shell = get_config("defaultShell")

                newline = "\n"
                await ctx.channel.send(f"""\n```{r3vIt(name, ip, port, shell)}```""")
            except Exception as e:
                await ctx.channel.send("Unexpected Error!\n basic syntax: \n```$r3v gen (name *required) (ip *required) (port *required) (shell)```read $r3v for more information.")
                print(f"Unexpected Error! in {__name__}\nError msg:{e}")
        return


def setup(bot):
    bot.add_cog(R3v(bot))
