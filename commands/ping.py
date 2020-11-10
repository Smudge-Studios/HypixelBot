import discord
from discord.ext import commands


class PingCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        try:
            msg = await ctx.send('Pong!')
            ms = (msg.created_at-ctx.message.created_at).total_seconds() * 1000
            try:
                await msg.edit(content=f"Pong!  `{int(ms)}ms`")
            except discord.NotFound:
                pass
        except discord.Forbidden:
            try:
                await ctx.author.send("Error: Cannot send messages in that channel. Please contact a server administrator to fix this issue.")
            except discord.Forbidden:
                return
def setup(bot):
    bot.add_cog(PingCMD(bot))