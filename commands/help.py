import discord
from discord.ext import commands
import random

class OnReady(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        color=random.randint(1, 16777215)
        embed = discord.Embed(title="Help", description="""`h!help` - Displays this.
`h!ping - Displays the bot's latency.
`h!player <player>` - Returns the specified player's profile.
`h!bedwars <player>` - Returns the specified player's Bedwars statistics.
`h!skywars <player>` - Returns the specified player's Skywars statistics.
`h!guild <guild name>` - Returns information on the specified guild.""", color = color)
        embed.set_footer(text='Unofficial Hypixel Discord Bot')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(OnReady(bot))