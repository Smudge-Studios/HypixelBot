import discord
from discord.ext import commands
from urllib.request import Request, urlopen
import json
from mojang import MojangAPI
from datetime import datetime
from configparser import ConfigParser

parser = ConfigParser()
parser.read('botconfig.ini')
API_KEY = parser.get('CONFIG', 'api_key')


class PlayerCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['p'])
    async def player(self, ctx, username:str=None):
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
                try:
                    recent = data['player']['mostRecentGameType']
                    if recent == "QUAKECRAFT":
                        recent = "Quake"
                    elif recent == "WALLS":
                        recent = 'Walls'
                    elif recent == 'PAINTBALL':
                        recent == 'paintball'
                    elif recent == 'SURVIVAL_GAMES':
                        recent = 'Blitz Survival Games'
                    elif recent == 'TNTGAMES':
                        recent = 'TNT Games'
                    elif recent == 'VAMPIREZ':
                        recent = 'VampireZ'
                    elif recent == 'WALLS3':
                        recent = 'Mega Walls'
                    elif recent == 'ARCADE':
                        recent = 'Arcade'
                    elif recent == 'ARENA':
                        recent = 'Arena'
                    elif recent == 'UHC':
                        recent = 'UHC Champions'
                    elif recent == 'MCGO':
                        recent = 'Cops and Crims'
                    elif recent == 'BATTLEGROUND':
                        recent = 'Warlords'
                    elif recent == 'SUPER_SMASH':
                        recent = 'Smash Heroes'
                    elif recent == 'GINGERBREAD':
                        recent = 'Turbo Kart Racers'
                    elif recent == 'HOUSING':
                        recent = 'Housing'
                    elif recent == 'SKYWARS':
                        recent = 'Skywars'
                    elif recent == 'TRUE_COMBAT':
                        recent = 'Crazy Walls'
                    elif recent == 'SPEED_UHC':
                        recent = 'Speed UHC'
                    elif recent == 'SKYCLASH':
                        recent = 'SkyClash'
                    elif recent == 'LEGACY':
                        recent = 'Classic Games'
                    elif recent == 'PROTOTYPE':
                        recent = 'Prototype'
                    elif recent == 'BEDWARS':
                        recent = 'BedWars'
                    elif recent == 'MURDER_MYSTERY':
                        recent = 'Murder Mystery'
                    elif recent == 'BUILD_BATTLE':
                        recent = 'Build Battle'
                    elif recent == 'DUELS':
                        recent = 'Duels'
                    elif recent == 'SKYBLOCK':
                        recent = 'Skyblock'
                    elif recent == 'PIT':
                        recent = 'The Pit'

                except:
                    recent = 'N/A'
                try:
                    karma = data["player"]["karma"] if "karma" in data["player"] else 0
                except:
                    karma = 'N/A'
                try:
                    if data['player']['lastLogin'] > data['player']['lastLogout']:
                        status = 'Online'
                    elif data['player']['lastLogin'] < data['player']['lastLogout']:
                        time = datetime.fromtimestamp(data['player']['lastLogout']/1000.0)
                        date = time.strftime("%m/%d/%Y")
                        minute = time.strftime("%M")
                        if int(time.strftime('%H')) == 12:
                            ampm = 'PM'
                            hour = time.strftime('%H')
                        elif int(time.strftime('%H')) > 12:
                            hour = int(time.strftime('%H')) - 12
                            ampm = 'PM'
                        elif int(time.strftime('%H')) < 12:
                            ampm = 'AM'
                            hour = time.strftime('%H')

                        date_time = time.strftime("%m/%d/%Y at %H:%M")
                        status = 'Offline - Last seen on ' + str(date) + ' at ' + str(hour) + ':' + str(minute) + ' ' + ampm + ', EST'
                    else:
                        status = 'N/A'
                except Exception as e:
                    status = 'N/A'
                try:
                    exp = data['player']['networkExp']
                    network_level = (((2 * exp) + 30625)**(1/2) / 50) - 2.5
                    level = round(network_level, 0)
                    level = int(level)
                except:
                    level = 'N/A'
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
            embed.add_field(name="Karma", value=str(karma), inline=True)
            embed.add_field(name="Guild", value=str(guild), inline=True)
            embed.add_field(name="Level", value=str(level), inline=True)
            embed.add_field(name="Recently Played", value=str(recent), inline=True)
            embed.add_field(name="Status", value=str(status), inline=True)
            embed.set_footer(text='Unofficial Hypixel Discord Bot')
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(PlayerCMD(bot))