import discord
from discord.ext import commands
import random

from discord.ext.commands.help import HelpCommand

class HelpCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        try:
            color=random.randint(1, 16777215)
            embed = discord.Embed(title="Help", description="""`h!help` - Displays this.
`h!ping` - Displays the bot's latency.
`h!info` - Displays some info and stats about the bot.
`h!player <player>` - Returns the specified player's profile.
`h!bedwars <player>` - Returns the specified player's Bedwars statistics.
`h!skywars <player>` - Returns the specified player's Skywars statistics.
`h!pit <player>` - Returns the specified player's Pit statistics.
`h!murdermystery <player>` - Returns the specified player's Murder Mystery statistics.
`h!buildbattle <player>` - Returns the specified player's Build Battle statistics.
`h!uhc <player>` - Returns the specified player's UHC statistics.
`h!leaderboard <game> <type>` - Returns the leaders on the specified leaderboard.
`h!guild <guild name>` - Returns information on the specified guild.
`h!playercount` - Returns Hypixel player counts.
`h!watchdog` - Returns Hypixel Watchdog statistics.

If you require more assistance, [join the support server](https://discord.gg/gxB8mRC).""", color = color)
            embed.set_footer(text='Unofficial Hypixel Discord Bot')
            await ctx.send(embed=embed)
        except discord.Forbidden:
            try:
                await ctx.send("Error: Cannot send embeds in this channel. Please contact a server administrator to fix this issue.")
                return
            except discord.Forbidden:
                try:
                    await ctx.author.send("Error: Cannot send messages in that channel. Please contact a server administrator to fix this issue.")
                except discord.Forbidden:
                    return

def setup(bot):
    bot.add_cog(HelpCMD(bot))