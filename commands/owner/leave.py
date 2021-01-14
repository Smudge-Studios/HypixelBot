import discord
from discord.ext import commands

class LeaveCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    @commands.is_owner()
    async def leave(self, ctx):
       await ctx.guild.leave()

def setup(bot):
    bot.add_cog(LeaveCMD(bot))