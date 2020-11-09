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

class MurderMysteryCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['mm'])
    async def murdermystery(self, ctx, username:str=None):
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
        try:
            gold = data['player']['stats']['MurderMystery']['coins']
        except:
            gold = 'N/A'
        try:
            played = data['player']['stats']['MurderMystery']['games']
        except:
            played = 'N/A'
        try:
            deaths = data['player']['stats']['MurderMystery']['deaths']
        except:
            deaths = 'N/A'
        try:
            kkills = data['player']['stats']['MurderMystery']['knife_kills']
        except:
            kkills = 'N/A'
        try:
            bkills = data['player']['stats']['MurderMystery']['bow_kills']
        except:
            bkills = 'N/A'
        try:
            wins = data['player']['stats']['MurderMystery']['wins']
        except:
            wins = 'N/A'
        req = Request("https://sessionserver.mojang.com/session/minecraft/profile/" + uuid)
        req.add_header('plun1331', 'https://plun1331.github.io')
        content = urlopen(req)
        data = json.load(content)
        embed = discord.Embed(title=data['name'] + "'s Murder Mystery Stats", color=0xff0000)
        embed.set_thumbnail(url='https://crafatar.com/avatars/' + uuid)
        embed.add_field(name='Games Played', value=str(utils.comma(played)))
        embed.add_field(name='Wins', value=str(utils.comma(wins)))
        embed.add_field(name='Deaths', value=str(utils.comma(deaths)))
        embed.add_field(name='Knife Kills', value=str(utils.comma(kkills)))
        embed.add_field(name='Bow Kills', value=str(utils.comma(bkills)))
        try:
            embed.add_field(name='Total Kills', value=str(utils.comma(int(kkills)+int(bkills))))
        except:
            embed.add_field(name='Total Kills', value='N/A')
        await ctx.send(embed=embed)
        
        

def setup(bot):
    bot.add_cog(MurderMysteryCMD(bot))