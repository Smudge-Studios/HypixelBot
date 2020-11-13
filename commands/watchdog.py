import discord
from discord.ext import commands
from utils.utils import utils
from aiohttp import ClientSession
from configparser import ConfigParser
import json
import random


parser = ConfigParser()
parser.read('botconfig.ini')
API_KEY = parser.get('CONFIG', 'api_key')

class WatchDogCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.session = ClientSession()

    @commands.command(aliases=['wd','watchdog','wds'])
    async def watchdogstats(self, ctx):
        try:
            async with self.session.get('https://api.hypixel.net/watchdogstats?key=' + API_KEY) as response:
                data = await response.json()
            if data['success'] == True:
                try:
                    wdtotal = data['watchdog_total']
                except:
                    wdtotal = 'N/A'
                try:
                    stafftotal = data['staff_total']
                except:
                    stafftotal = 'N/A'
                color=random.randint(1, 16777215)
                embed = discord.Embed(title="Hypixel Watchdog Statistics", color = color)
                embed.add_field(name="Watchdog Bans", value=str(utils.comma(wdtotal)))
                embed.add_field(name="Staff Bans", value=str(utils.comma(stafftotal)))
                try:
                    embed.add_field(name="Total Bans", value=str(utils.comma(wdtotal+stafftotal)))
                except:
                    embed.add_field(name="Total Bans", value='N/A')
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
    bot.add_cog(WatchDogCMD(bot))