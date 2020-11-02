import discord
from discord.ext import commands


class PingCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        msg = await ctx.send('Pong!')
        ms = (msg.created_at-ctx.message.created_at).total_seconds() * 1000
        await msg.edit(content=f"Pong!  `{int(ms)}ms`")

def setup(bot):
    bot.add_cog(PingCMD(bot))