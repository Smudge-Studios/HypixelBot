import discord
from discord.ext import commands
from aiohttp import ClientSession
from mojang import MojangAPI
from configparser import ConfigParser
from utils.utils import utils
import random

parser = ConfigParser()
parser.read('botconfig.ini')
API_KEY = parser.get('CONFIG', 'api_key')

class PlayerCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.session = ClientSession()
    
    def cog_unload(self):
        self.session.close()

    @commands.command(aliases=['p'])
    async def player(self, ctx, username:str=None):
        try:
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
            async with self.session.get('https://api.hypixel.net/player?key=' + API_KEY + '&uuid=' + uuid) as response:
                data = await response.json()
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
                async with self.session.get("https://sessionserver.mojang.com/session/minecraft/profile/" + uuid) as response:
                    data = await response.json()
                color=random.randint(1, 16777215)
                embed = discord.Embed(title=data['name'] + "'s Profile", color=color)
                embed.set_thumbnail(url='https://crafatar.com/avatars/' + uuid)
                embed.add_field(name="Rank", value=str(rank), inline=True)
                embed.add_field(name="Karma", value=str(utils.comma(karma)), inline=True)
                embed.add_field(name="Guild", value=str(utils.comma(guild)), inline=True)
                embed.add_field(name="Level", value=str(utils.comma(level)), inline=True)
                embed.add_field(name="Recently Played", value=str(recent), inline=True)
                embed.add_field(name="Status", value=str(status), inline=True)
                embed.set_footer(text='Unofficial Hypixel Discord Bot')
                await ctx.send(embed=embed)
        except discord.Forbidden:
            try:
                await ctx.send("Error: Cannot send embeds in this channel. Please contact a server administrator to fix this issue.")
                return
            except discord.Forbidden:
                try:
                    await ctx.author.send("Error: Cannot send messages in that channel. Please contact a server administrator to fix this issue.")
                    return
                except discord.Forbidden:
                    return

def setup(bot):
    bot.add_cog(PlayerCMD(bot))