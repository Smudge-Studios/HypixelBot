import discord
from discord.ext import commands
from urllib.request import Request, urlopen
import json
from mojang import MojangAPI
from configparser import ConfigParser

parser = ConfigParser()
parser.read('botconfig.ini')
API_KEY = parser.get('CONFIG', 'api_key')

class MurderMysteryCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def murdermystery(self, ctx, username):
        #verify if player exists
        if username==None:
            embed = discord.Embed(title="Error", description="""Please provide a username.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        uuid = MojangAPI.get_uuid(str(username))
        if uuid == '5d1f7b0fdceb472d9769b4e37f65db9f':
            embed = discord.Embed(title="Error", description="""That user does not exist.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        elif not uuid:
            embed = discord.Embed(title="Error", description="""That user does not exist.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        #send request
        req = Request('https://api.hypixel.net/player?key=' + API_KEY + '&uuid=' + uuid)
        req.add_header('plun1331', 'https://plun1331.github.io')
        content = urlopen(req)
        data = json.load(content) 
        #errors
        if data['success'] == False:
            if data['cause'] == 'Malformed UUID':
                embed = discord.Embed(title="Error", description="""Something went wrong.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
            else:
                embed = discord.Embed(title="Error", description="""Something went wrong.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
        #it worked!
        elif data['success'] == True:
            if data['player'] == None:
                embed = discord.Embed(title="Error", description="""That user has never joined the Hypixel Network.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
            else:
                try:
                    wins = data['player']
                except:
                    wins = 'N/A'
                try:
                    losses = data['player']
                except:
                    losses = 'N/A'
                try:
                    kills = data['player']
                except:
                    kills = 'N/A'
                try:
                    deaths = data['player']
                except:
                    deaths = 'N/A'
                try:
                    gold = data['player']
                except:
                    gold = 'N/A'
                try:
                    coins = data['player']
                except:
                    coins = 'N/A'
                

def setup(bot):
    bot.add_cog(MurderMysteryCMD(bot))