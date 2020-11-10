import discord
from discord.ext import commands
from urllib.request import Request, urlopen
import json
from configparser import ConfigParser
from utils.utils import utils
import random

parser = ConfigParser()
parser.read('botconfig.ini')
API_KEY = parser.get('CONFIG', 'api_key')

class InfoCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        try:
            req = Request('https://api.hypixel.net/key?key=' + API_KEY)
            req.add_header('plun1331', 'https://plun1331.github.io')
            content = urlopen(req)
            data = json.load(content)
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
This bot is also open-sourced. You can view the source code [here](https://github.com/plun1331/HypixelBot)

Amount of API Requests made in the past minute: {queriesmin}
Total API Requests: {queries}""", color = color)
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