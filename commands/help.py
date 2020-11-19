import discord
from discord.ext import commands
import random

botinfo = """`h!help` - Displays this.
`h!info` - Displays some info and stats about the bot.
`h!ping` - Displays the bot's latency."""

playerstats = """`h!player <player>` - Returns the specified player's profile.
`h!bedwars <player>` - Returns the specified player's Bedwars statistics.
`h!skywars <player>` - Returns the specified player's Skywars statistics.
`h!pit <player>` - Returns the specified player's Pit statistics.
`h!murdermystery <player>` - Returns the specified player's Murder Mystery statistics.
`h!buildbattle <player>` - Returns the specified player's Build Battle statistics.
`h!uhc <player>` - Returns the specified player's UHC statistics.
`h!skyblock <subcommand>` - Does nothing without a subcommand. Do `h!skyblock` for more information."""

hypixelstats = """`h!leaderboard <game> <type>` - Returns the leaders on the specified leaderboard.
`h!guild <guild name>` - Returns information on the specified guild.
`h!playercount` - Returns Hypixel player counts.
`h!watchdog` - Returns Hypixel Watchdog statistics."""

other = """This bot is in no way affiliated with or endorsed by [Hypixel, Inc](https://hypixel.net). All logos, brands, trademarks, and registered trademarks are property of their respective owners.
If you require more assistance, [join the support server](https://discord.gg/gxB8mRC)."""

class HelpCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        try:
            color=random.randint(1, 16777215)
            embed = discord.Embed(title="Help", color = color)
            embed.add_field(name="Bot Information", value=botinfo)
            embed.add_field(name="Hypixel Player Stats", value=playerstats)
            embed.add_field(name="Hypixel Statistics", value=hypixelstats)
            embed.add_field(name="Other Information", value=other)
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