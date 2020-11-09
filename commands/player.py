import discord
from discord.ext import commands
from urllib.request import Request, urlopen
import json
from mojang import MojangAPI
from configparser import ConfigParser
from utils.utils import utils
import sqlite3

parser = ConfigParser()
parser.read('botconfig.ini')
API_KEY = parser.get('CONFIG', 'api_key')
conn = sqlite3.connect('db\\data.db')

class PlayerCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['p'])
    async def player(self, ctx, username:str=None):
        if username==None:
            cursor = conn.execute("SELECT * from LINKS")
            for row in cursor:
                if row[0] == ctx.author.id:
                    username = row[1]
                    break
            if username is None:
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
            embed = discord.Embed(title="Error", description="""Something went wrong.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        #it worked!
        elif data['success'] == True:
            if data['player']==None:
                embed = discord.Embed(title="Error", description="""That player has never joined the Hypixel Network.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
            try:
                #set rank to players rank
                rank = 'N/A'
                if "rank" in data["player"] and data["player"]["rank"] != "NORMAL":
                    rank = data["player"]["rank"]
                elif "monthlyPackageRank" in data["player"]:
                    if data['player']['monthlyPackageRank'] == "SUPERSTAR":
                        rank = "MVP++"
                elif "newPackageRank" in data["player"]:
                    rank = data["player"]["newPackageRank"]
                elif "packageRank" in data["player"]:
                    rank = data["player"]["packageRank"]
                else:
                    rank = "Default"
                if rank == "VIP_PLUS":
                    rank = "VIP+"
                elif rank == "MVP_PLUS":
                    rank = "MVP+"
                elif rank == "YOUTUBER":
                    rank = "YouTube"
                elif rank == "ADMIN":
                    rank = "Administrator"
                elif rank == "MODERATOR":
                    rank = "Moderator"
                elif rank == "HELPER":
                    rank = "Helper"
                recent = utils.gameconverter(data['player']['mostRecentGameType'])
                try:
                    karma = data["player"]["karma"] if "karma" in data["player"] else 0
                except:
                    karma = 'N/A'
                status = utils.timeconverter(data['player']['lastLogin'], data['player']['lastLogout'])
                level = utils.networklevel(data['player']['networkExp'])
            except Exception as e:
                embed = discord.Embed(title="Error", description="""An error occured while retriving data on """ + username + f" - {e}", color=0xff0000)
                await ctx.send(embed=embed)
                return
            try:
                guild = data['guild']['name']
                if guild == None:
                    guild = 'None'
            except:
                guild = 'None'
            req = Request("https://sessionserver.mojang.com/session/minecraft/profile/" + uuid)
            req.add_header('plun1331', 'https://plun1331.github.io')
            content = urlopen(req)
            data = json.load(content)
            embed = discord.Embed(title=data['name'] + "'s Profile", color=0xff0000)
            embed.set_thumbnail(url='https://crafatar.com/avatars/' + uuid)
            embed.add_field(name="Rank", value=str(rank), inline=True)
            embed.add_field(name="Karma", value=str(utils.comma(karma)), inline=True)
            embed.add_field(name="Guild", value=str(utils.comma(guild)), inline=True)
            embed.add_field(name="Level", value=str(utils.comma(level)), inline=True)
            embed.add_field(name="Recently Played", value=str(recent), inline=True)
            embed.add_field(name="Status", value=str(status), inline=True)
            embed.set_footer(text='Unofficial Hypixel Discord Bot')
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(PlayerCMD(bot))