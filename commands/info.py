import discord
from discord.ext import commands
from aiohttp import ClientSession
from configparser import ConfigParser
from utils.utils import utils
import random

parser = ConfigParser()
parser.read('botconfig.ini')
API_KEY = parser.get('CONFIG', 'api_key')

class InfoCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.session = ClientSession()

    def cog_unload(self):
        self.session.close()

    @commands.command()
    async def info(self, ctx):
        try:
            async with self.session.get('https://api.hypixel.net/key?key=' + API_KEY) as response:
                data = await response.json()
            try:
                queries = data['record']['totalQueries']
            except:
                queries = 'N/A'
            try:
                queriesmin = data['record']['queriesInPastMin']
            except:
                queriesmin = 'N/A'
            color=random.randint(1, 16777215)
            embed = discord.Embed(title="Bot Information", description=f"""This bot was coded by plun1331#5535.
This bot is also open-sourced. You can view the source code [here](https://github.com/plun1331/HypixelBot)""", color = color)
            embed.add_field(name="Stats", value=f"""Amount of API Requests made in the past minute: {queriesmin}
Total API Requests: {queries}
Guilds: {utils.comma(len(self.bot.guilds))}""", inline=False)
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
    bot.add_cog(InfoCMD(bot))