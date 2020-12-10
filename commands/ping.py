import discord
from discord.ext import commands
import random

class PingCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        if ctx.guild is not None:
            me = ctx.guild.get_member(self.bot.user.id)
            perms = ctx.channel.permissions_for(me)
            if perms.send_messages:
                if not perms.embed_links:
                    await ctx.send("Error: Cannot send embeds in this channel. Please contact a server administrator to fix this issue.")
                    return
                if perms.embed_links:
                    pass
            if not perms.send_messages:
                return
        color=random.randint(1, 16777215)
        embed = discord.Embed(title='Ping', description='Pong!', color=color)
        msg = await ctx.send(embed=embed)
        ms = (msg.created_at-ctx.message.created_at).total_seconds() * 1000
        try:
            embed = discord.Embed(title='Ping', description=f'Pong! `{int(ms)}ms`', color=color)
            await msg.edit(embed=embed)
        except discord.NotFound:
            pass
def setup(bot):
    bot.add_cog(PingCMD(bot))