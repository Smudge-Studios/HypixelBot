import discord
from discord.ext import commands
from urllib.request import Request, urlopen
import json
from mojang import MojangAPI
from configparser import ConfigParser
from utils.utils import utils

parser = ConfigParser()
parser.read('botconfig.ini')
API_KEY = parser.get('CONFIG', 'api_key')

class LeaderboardCMD(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['lb'])   
    async def leaderboard(self, ctx, game: str=None, *, type: str=None):
        #verify if player exists
        if game is None:
            embed = discord.Embed(title="Error", description="""Please provide a game.
Supported games: `skywars`, `bedwars`""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        if type is None:
            embed = discord.Embed(title="Error", description="""That user does not exist.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        #send request
        req = Request('https://api.hypixel.net/leaderboards?key=' + API_KEY)
        req.add_header('plun1331', 'https://plun1331.github.io')
        content = urlopen(req)
        data = json.load(content) 
        #errors
        if data['success'] == False:
            embed = discord.Embed(title="Error", description="""Something went wrong.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        #it worked!
        elif data['success'] == True:
            if game.lower() == 'skywars':
                data = data['leaderboards']['SKYWARS']
            elif game.lower() == 'bedwars':
                data = data['leaderboards']['BEDWARS']
            else:
                embed = discord.Embed(title='Error', description='Unsupported game type.', color=0xff0000)
                await ctx.send(embed=embed)
                return
            type = type.lower()
            leaders = None
            for lb in data:
                if lb['path'].replace('_', '') == type:
                    path = lb['path']
                    leaders = lb['leaders']
                    break
            if leaders is None:
                embed = discord.Embed(title='Error', description='Invalid leaderboard.', color=0xff0000)
                await ctx.send(embed=embed)
                return
            msg = ''
            for uid in leaders:
                uid = uid.replace('-','')
                req = Request("https://sessionserver.mojang.com/session/minecraft/profile/" + uuid)
                req.add_header('plun1331', 'https://plun1331.github.io')
                content = urlopen(req)
                data = json.load(content)
                name = data['name']
                req = Request('https://api.hypixel.net/player?key=' + API_KEY + '&uuid=' + uid)
                req.add_header('plun1331', 'https://plun1331.github.io')
                content = urlopen(req)
                data = json.load(content)
                try:
                    amnt = data['player']['stats'][game.lower().capitalize()][path]
                except:
                    amnt = 'N/A'
                msg = msg + f"{name} - {amnt}\n"
            embed = discord.Embed(title=f'{game.lower().capitalize()}: {path.capitalize()} leaderboard', description=msg)
            await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(LeaderboardCMD(bot))