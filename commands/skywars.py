import discord
from discord.ext import commands
from mojang import MojangAPI
from configparser import ConfigParser
from utils.utils import utils, hypixel
import random

parser = ConfigParser()
parser.read('botconfig.ini')
API_KEY = parser.get('CONFIG', 'api_key')

class SkywarsCMD(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['sw'])   
    async def skywars(self, ctx, username:str=None):
        try:
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
            data = await hypixel.player(uuid)
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
                        level = 'N/A'
                        xp = data['player']['stats']['SkyWars']['skywars_experience']
                        xps = [0, 20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000]
                        if xp >= 15000:
                            level = (xp - 15000) / 10000. + 12
                        else:
                            for i in range(len(xps)):
                                if xp < xps[i]:
                                    level = str(utils.comma(int(round(int(1 + i + float(xp - xps[i-1]) / (xps[i] - xps[i-1], 0)))))) + ' ⭐'
                    except:
                        level = 'N/A'
                    try:
                        games_played = data['player']['stats']['SkyWars']['games_played_skywars']
                    except:
                        games_played = 'N/A'
                    try:
                        winstreak = data['player']['stats']['SkyWars']['win_streak']
                    except:
                        winstreak = 'N/A'
                    try:
                        kills = data['player']['stats']['SkyWars']['kills']
                    except:
                        kills = 'N/A'
                    try:
                        deaths = data['player']['stats']['SkyWars']['deaths']
                    except:
                        deaths = 'N/A'
                    try:
                        top_winstreak = data['player']['stats']['SkyWars']['highestWinstreak']
                    except:
                        top_winstreak = 'N/A'
                    try:
                        coins = data['player']['stats']['SkyWars']['coins']
                    except:
                        coins = 'N/A'
                    try:
                        souls = data['player']['stats']['SkyWars']['souls']
                    except:
                        souls = 'N/A'
                    try:
                        wins = data['player']['stats']['SkyWars']['wins']
                    except:
                        wins = 'N/A'
                    try:
                        losses = data['player']['stats']['SkyWars']['losses']
                    except:
                        losses = 'N/A'
                    data = await hypixel.getname(uuid)
                    color=random.randint(1, 16777215)
                    embed = discord.Embed(title=data['name'] + "'s Skywars Stats", color=color)
                    embed.set_thumbnail(url='https://crafatar.com/avatars/' + uuid)
                    try:
                        embed.add_field(name="Level", value=str(int(level))+' ⭐', inline=True)
                    except:
                        embed.add_field(name="Level", value='N/A', inline=True)
                    embed.add_field(name="Games Played", value=str(utils.comma(round(games_played, 0))), inline=True)
                    embed.add_field(name="Coins", value=str(utils.comma(coins)), inline=True)
                    embed.add_field(name="Souls", value=str(utils.comma(souls)), inline=True)
                    embed.add_field(name="Winstreak", value=str(utils.comma(winstreak)), inline=True)
                    embed.add_field(name="Highest Winstreak", value=str(utils.comma(top_winstreak)), inline=True)
                    embed.add_field(name="Kills", value=str(utils.comma(kills)), inline=True)
                    embed.add_field(name="Deaths", value=str(utils.comma(deaths)), inline=True)
                    try:
                        embed.add_field(name="K/D Ratio", value=str(utils.comma(round(int(kills)/int(deaths), 2))), inline=True)
                    except:
                        embed.add_field(name="K/D Ratio", value='N/A', inline=True)
                    embed.add_field(name="Wins", value=str(utils.comma(wins)), inline=True)
                    embed.add_field(name="Losses", value=str(utils.comma(losses)), inline=True)
                    try:
                        embed.add_field(name="W/L Ratio", value=str(utils.comma(round(int(wins)/int(losses), 2))), inline=True)
                    except:
                        embed.add_field(name="W/L Ratio", value='N/A', inline=True)
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
    bot.add_cog(SkywarsCMD(bot))