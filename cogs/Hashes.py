import discord
from discord.ext import commands
from libs.Hashes import *
from libs.help import hashesHelp


class Hashes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ==============================
    # => Encrypt
    # ==============================

    @ commands.command()
    async def hashit(self, ctx, *arg):
        if not arg:
            print("$hashit Help massage sent")
            await ctx.channel.send(hashesHelp)

        elif arg[0] == "blake2b":
            try:
                print(f"encrypting {arg[1]} with blake2b algorithm")
                await ctx.channel.send(f"\nHere you go: `{Hblake2b(arg[1])}`")
            except Exception as e:
                print(f"Failed to hash {arg[1]} with blake2b algorithm\nError msg: {e}")
                await ctx.channel.send(f"Failed to hash {arg[1]} with blake2b")
        elif arg[0] == "sha256":
            try:
                print(f"encrypting {arg[1]} with sha256 algorithm")
                await ctx.channel.send(f"\nHere you go: `{Hsha256(arg[1])}`")
            except Exception as e:
                print(f"Failed to hash {arg[1]} with sha256 algorithm\nError msg: {e}")
                await ctx.channel.send(f"Failed to hash {arg[1]} with sha256")
        elif arg[0] == "blake2s":
            try:
                print(f"encrypting {arg[1]} with blake2s algorithm")
                await ctx.channel.send(f"\nHere you go: `{Hblake2s(arg[1])}`")
            except Exception as e:
                print(f"Failed to hash {arg[1]} with blake2s algorithm\nError msg: {e}")
                await ctx.channel.send(f"Failed to hash {arg[1]} with blake2s")
        elif arg[0] == "md5":
            try:
                print(f"encrypting {arg[1]} with md5 algorithm")
                await ctx.channel.send(f"\nHere you go: `{Hmd5(arg[1])}`")
            except Exception as e:
                print(f"Failed to hash {arg[1]} with md5 algorithm\nError msg: {e}")
                await ctx.channel.send(f"Failed to hash {arg[1]} with md5 {e}")
        elif arg[0] == "sha224":
            try:
                print(f"encrypting {arg[1]} with sha224 algorithm")
                await ctx.channel.send(f"\nHere you go: `{Hsha224(arg[1])}`")
            except Exception as e:
                print(f"Failed to hash {arg[1]} with sha224 algorithm\nError msg: {e}")
                await ctx.channel.send(f"Failed to hash {arg[1]} with sha224")
        elif arg[0] == "sha512":
            try:
                print(f"encrypting {arg[1]} with sha512 algorithm")
                await ctx.channel.send(f"\nHere you go: `{Hsha512(arg[1])}`")
            except Exception as e:
                print(f"Failed to hash {arg[1]} with sha512 algorithm\nError msg: {e}")
                await ctx.channel.send(f"Failed to hash {arg[1]} with sha512")
        elif arg[0] == "sha3_224":
            try:
                print(f"encrypting {arg[1]} with sha3_224 algorithm")
                await ctx.channel.send(f"\nHere you go: `{Hsha3_224(arg[1])}`")
            except Exception as e:
                print(f"Failed to hash {arg[1]} with sha3_224 algorithm\nError msg: {e}")
                await ctx.channel.send(f"Failed to hash {arg[1]} with sha3_224")
        elif arg[0] == "sha1":
            try:
                print(f"encrypting {arg[1]} with sha1 algorithm")
                await ctx.channel.send(f"\nHere you go: `{Hsha1(arg[1])}`")
            except Exception as e:
                print(f"Failed to hash {arg[1]} with sha1 algorithm\nError msg: {e}")
                await ctx.channel.send(f"Failed to hash {arg[1]} with sha1")
        elif arg[0] == "sha3_256":
            try:
                print(f"encrypting {arg[1]} with sha3_256 algorithm")
                await ctx.channel.send(f"\nHere you go: `{Hsha3_256(arg[1])}`")
            except Exception as e:
                print(f"Failed to hash {arg[1]} with sha3_256 algorithm\nError msg: {e}")
                await ctx.channel.send(f"Failed to hash {arg[1]} with sha3_256")
        elif arg[0] == "sha3_384":
            try:
                print(f"encrypting {arg[1]} with sha3_384 algorithm")
                await ctx.channel.send(f"\nHere you go: `{Hsha3_384(arg[1])}`")
            except Exception as e:
                print(f"Failed to hash {arg[1]} with sha3_384 algorithm\nError msg: {e}")
                await ctx.channel.send(f"Failed to hash {arg[1]} with sha3_384")
        elif arg[0] == "shake_256":
            try:
                print(f"encrypting {arg[1]} with shake_256 algorithm")
                await ctx.channel.send(f"\nHere you go: `{Hshake_256(arg[1])}`")
            except Exception as e:
                print(f"Failed to hash {arg[1]} with shake_256 algorithm\nError msg: {e}")
                await ctx.channel.send(f"Failed to hash {arg[1]} with shake_256")
        elif arg[0] == "sha3_512":
            try:
                print(f"encrypting {arg[1]} with sha3_512 algorithm")
                await ctx.channel.send(f"\nHere you go: `{Hsha3_512(arg[1])}`")
            except Exception as e:
                print(f"Failed to hash {arg[1]} with sha3_512 algorithm\nError msg: {e}")
                await ctx.channel.send(f"Failed to hash {arg[1]} with sha3_512")
        elif arg[0] == "sha384":
            try:
                print(f"encrypting {arg[1]} with sha384 algorithm")
                await ctx.channel.send(f"\nHere you go: `{Hsha384(arg[1])}`")
            except Exception as e:
                print(f"Failed to hash {arg[1]} with sha384 algorithm\nError msg: {e}")
                await ctx.channel.send(f"Failed to hash {arg[1]} with sha384")
        elif arg[0] == "shake_128":
            try:
                print(f"encrypting {arg[1]} with shake_128 algorithm")
                await ctx.channel.send(f"\nHere you go: `{Hshake_128(arg[1])}`")
            except Exception as e:
                print(f"Failed to hash {arg[1]} with shake_128 algorithm\nError msg: {e}")
                await ctx.channel.send(f"Failed to hash {arg[1]} with shake_128")
        return


def setup(bot):
    bot.add_cog(Hashes(bot))
