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

class PitCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pit(self, ctx, username):
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
            deaths = data['player']['stats']['Pit']['pit_stats_ptl']['deaths']
        except:
            deaths = 'N/A'
        try:
            dmgdealt = data['player']['stats']['Pit']['pit_stats_ptl']['damage_dealt']
        except:
            dmgdealt = 'N/A'
        try:
            dmgrecieved = data['player']['stats']['Pit']['pit_stats_ptl']['damage_received']
        except:
            dmgrecieved = 'N/A'
        try:
            joins = data['player']['stats']['Pit']['pit_stats_ptl']['joins']
        except:
            joins = 'N/A'
        try:
            kills = data['player']['stats']['Pit']['pit_stats_ptl']['kills']
        except:
            kills = 'N/A'
        try:
            assists = data['player']['stats']['Pit']['pit_stats_ptl']['assists']
        except:
            assists = 'N/A'
        try:
            bdmgdealt = data['player']['stats']['Pit']['pit_stats_ptl']['bow_damage_dealt']
        except:
            bdmgdealt = 'N/A'
        try:
            bdmgrecieved = data['player']['stats']['Pit']['pit_stats_ptl']['bow_damage_received']
        except:
            bdmgrecieved = 'N/A'
        try:
            jumped = data['player']['stats']['Pit']['pit_stats_ptl']['jumped_into_pit']
        except:
            jumped = 'N/A'
        try:
            hits = data['player']['stats']['Pit']['pit_stats_ptl']['sword_hits']
        except:
            hits = 'N/A'
        try:
            bhits = data['player']['stats']['Pit']['pit_stats_ptl']['arrow_hits']
        except:
            bhits = 'N/A'
        req = Request("https://sessionserver.mojang.com/session/minecraft/profile/" + uuid)
        req.add_header('plun1331', 'https://plun1331.github.io')
        content = urlopen(req)
        data = json.load(content)
        embed = discord.Embed(title=data['name'] + "'s Pit Stats", color=0xff0000)
        embed.set_thumbnail(url='https://crafatar.com/avatars/' + uuid)
        embed.add_field(name="Times Joined", value=str(utils.comma(joins)), inline=True)
        embed.add_field(name="Times Jumped into Pit", value=str(utils.comma(jumped)), inline=True)
        embed.add_field(name="Assists", value=str(utils.comma(assists)), inline=True)
        embed.add_field(name="Kills", value=str(utils.comma(kills)), inline=True)
        embed.add_field(name="Deaths", value=str(utils.comma(deaths)), inline=True)
        try:
            embed.add_field(name="K/D Ratio", value=str(utils.comma(round(int(kills)/int(deaths), 2))), inline=True)
        except:
            embed.add_field(name="K/D Ratio", value='N/A', inline=True)
        embed.add_field(name="Melee Damage Dealt", value=str(utils.comma(dmgdealt)), inline=True)
        embed.add_field(name="Melee Damage Received", value=str(utils.comma(dmgrecieved)), inline=True)
        embed.add_field(name="Melee Hits", value=str(utils.comma(hits)))
        embed.add_field(name="Bow Damage Dealt", value=str(utils.comma(bdmgdealt)), inline=True)
        embed.add_field(name="Bow Damage Received", value=str(utils.comma(bdmgrecieved)), inline=True)
        embed.add_field(name="Bow Hits", value=str(utils.comma(bhits)))
        embed.set_footer(text="Unofficial Hypixel Bot")
        await ctx.send(embed=embed)
        
                

def setup(bot):
    bot.add_cog(PitCMD(bot))