import discord
from discord.ext import commands
from urllib.request import Request, urlopen
import json
from configparser import ConfigParser
from datetime import datetime
from utils.utils import utils
import random

parser = ConfigParser()
parser.read('botconfig.ini')
API_KEY = parser.get('CONFIG', 'api_key')

class GuildCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['g'])
    async def guild(self, ctx, *, guildname:str=None):
        try:
            if guildname is None:
                embed = discord.Embed(title="Error", description='Please provide a guild to search for.', color=0xff0000)
                await ctx.send(embed=embed)
                return
            gnamesearch = guildname.replace(' ','%20')
            req = Request('https://api.hypixel.net/findGuild?key=' + API_KEY + '&byName=' + gnamesearch)
            req.add_header('plun1331', 'https://plun1331.github.io')
            content = urlopen(req)
            data = json.load(content) 
            gid = data['guild']
            if gid == None:
                embed = discord.Embed(title="Error", description="""The guild """ + guildname + ' does not exist.', color=0xff0000)
                await ctx.send(embed=embed)
                return
            else:
                req = Request('https://api.hypixel.net/guild?key=' + API_KEY + '&id=' + gid)
                req.add_header('plun1331', 'https://plun1331.github.io')
                content = urlopen(req)
                data = json.load(content)
            try:
                glevel = utils.guildlevel(xp=data['guild']['exp'])
            except Exception as e:
                glevel = 'N/A'
                print(f"Couldn't get guild level: {e}")

            try:
                gname = data['guild']['name']
            except Exception as e:
                gname = 'N/A'
                print(f"Couldn't get guild name: {e}")
            try:
                time = datetime.fromtimestamp(data['guild']['created']/1000.0)
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
                else: #this should never happen
                    hour = None
                    ampm = None

                date_time = time.strftime("%m/%d/%Y at %H:%M")
                created = str(date) + ' at ' + str(hour) + ':' + str(minute) + ' ' + ampm + ', EST'
            except Exception as e:
                created = 'N/A'
                print(f"Couldn't get guild created date: {e}")
            try:
                desc = data['guild']['description']
            except Exception as e:
                desc = 'N/A'
                print(f"Couldn't get guild description: {e}")
            try:
                tag = data['guild']['tag']
            except Exception as e:
                tag = 'N/A'
                print(f"Couldn't get guild tag: {e}")
            try:
                mbrs = 0
                for m in data['guild']['members']:
                    mbrs = mbrs + 1
            except Exception as e:
                mbrs = 'N/A'
                print(f"Couldn't get guild members: {e}")
            try:
                gmuuid = data['guild']['members'][0]['uuid']
                req = Request("https://sessionserver.mojang.com/session/minecraft/profile/" + gmuuid)
                req.add_header('plun1331', 'https://plun1331.github.io')
                content = urlopen(req)
                data = json.load(content)
                gm = data['name']
            except Exception as e:
                gm = 'N/A'
                print(f"Couldn't get guild manager: {e}")
            color=random.randint(1, 16777215)
            embed = discord.Embed(title='Guild Info', color=color)
            embed.add_field(name="Guild Name", value=str(gname), inline=True)
            embed.add_field(name="Guild Manager", value=str(gm), inline=True)
            embed.add_field(name="Members", value=str(mbrs), inline=True)
            embed.add_field(name="Created On", value=str(created), inline=True)
            embed.add_field(name="Guild Level", value=str(utils.comma(int(glevel))), inline=True)
            embed.add_field(name="Guild Description", value=str(desc), inline=True)
            embed.add_field(name="Guild Tag", value=str(tag), inline=True)
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
    bot.add_cog(GuildCMD(bot))