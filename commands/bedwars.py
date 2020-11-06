import discord
from discord.ext import commands
from urllib.request import Request, urlopen
import json
from mojang import MojangAPI
from configparser import ConfigParser
from utils import utils

parser = ConfigParser()
parser.read('botconfig.ini')
API_KEY = parser.get('CONFIG', 'api_key')

class BedwarsCMD(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['bw'])   
    async def bedwars(self, ctx, username:str=None):
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
                level = str(utils.comma(int(data['player']['achievements']['bedwars_level']))) + ' ⭐'
            except:
                level = 'N/A'
            try:
                games_played = data['player']['stats']['Bedwars']['games_played_bedwars']
            except:
                games_played = 'N/A'
            try:
                exp = data['player']['stats']['Bedwars']['Experience']
            except:
                exp = 'N/A'
            try:
                final_deaths = data['player']['stats']['Bedwars']['final_deaths_bedwars']
            except:
                final_deaths = 'N/A'
            try:
                normal_deaths = data['player']['stats']['Bedwars']['deaths_bedwars']
            except:
                normal_deaths = 'N/A'
            try:
                total_deaths = final_deaths+normal_deaths
                if total_deaths == 'N/AN/A':
                    raise ValueError
            except:
                total_deaths = 'N/A'
            try:
                beds_lost = data['player']['stats']['Bedwars']['beds_lost_bedwars']
            except:
                beds_lost = 'N/A'
            try:
                beds_broken = data['player']['stats']['Bedwars']['beds_broken_bedwars']
            except:
                beds_broken = 'N/A'
            try:
                normal_kills = data['player']['stats']['Bedwars']['kills_bedwars']
            except:
                normal_kills = 'N/A'
            try:
                final_kills = data['player']['stats']['Bedwars']['final_kills_bedwars']
            except:
                final_kills = 'N/A'
            try:
                total_kills = final_kills+normal_kills
                if total_kills == 'N/AN/A':
                    raise ValueError
            except:
                total_kills = 'N/A'
            try:
                wins = data['player']['stats']['Bedwars']['wins_bedwars']
            except:
                wins = 'N/A'
            try:
                losses = data['player']['stats']['Bedwars']['losses_bedwars']
            except:
                losses = 'N/A'
            try:
                winstreak = data['player']['stats']['Bedwars']['winstreak']
            except:
                winstreak = 'N/A'
            
            req = Request("https://sessionserver.mojang.com/session/minecraft/profile/" + uuid)
            req.add_header('plun1331', 'https://plun1331.github.io')
            content = urlopen(req)
            data = json.load(content) 
            embed = discord.Embed(title=data['name'] + "'s Bedwars Stats", color=0xff0000)
            embed.set_thumbnail(url='https://crafatar.com/avatars/' + uuid)
            embed.add_field(name="Level", value=str(level), inline=True)
            embed.add_field(name="Games Played", value=str(utils.comma(games_played)), inline=True)
            embed.add_field(name="Experience", value=str(utils.comma(round(exp, 0))), inline=True)
            embed.add_field(name="Normal Deaths", value=str(utils.comma(normal_deaths)), inline=True)
            embed.add_field(name="Final Deaths", value=str(utils.comma(final_deaths)), inline=True)
            embed.add_field(name="Total Deaths", value=str(utils.comma(total_deaths)), inline=True)
            embed.add_field(name="Normal Kills", value=str(utils.comma(normal_kills)), inline=True)
            embed.add_field(name="Final Kills", value=str(utils.comma(final_kills)), inline=True)
            embed.add_field(name="Total Kills", value=str(utils.comma(total_kills)), inline=True)
            try:
                embed.add_field(name="Normal K/D Ratio", value=str(utils.comma(round(normal_kills/normal_deaths, 2))), inline=True)
            except:
                embed.add_field(name="Normal K/D Ratio", value=str('N/A'), inline=True)
            try:
                embed.add_field(name="Final K/D Ratio", value=str(utils.comma(round(final_kills/final_deaths, 2))), inline=True)
            except:
                embed.add_field(name="Final K/D Ratio", value=str('N/A'), inline=True)
            try:
                embed.add_field(name="K/D Ratio", value=str(utils.comma(round(total_kills/total_deaths, 2))), inline=True)
            except:
                embed.add_field(name="K/D Ratio", value=str('N/A'), inline=True)
            embed.add_field(name="Wins", value=str(utils.comma(wins)), inline=True)
            embed.add_field(name="Losses", value=str(utils.comma(losses)), inline=True)
            try:
                embed.add_field(name="W/L Ratio", value=str(utils.comma(round(wins/losses, 2))), inline=True)
            except:
                embed.add_field(name="W/L Ratio", value=str('N/A'), inline=True)
            embed.add_field(name="Beds Lost", value=str(utils.comma(beds_lost)), inline=True)
            embed.add_field(name="Beds Broken", value=str(utils.comma(beds_broken)), inline=True)
            embed.add_field(name="Winstreak", value=str(utils.comma(winstreak)), inline=True)
            embed.set_footer(text='Unofficial Hypixel Discord Bot')
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(BedwarsCMD(bot))