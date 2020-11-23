import discord
from discord.ext import commands
from configparser import ConfigParser
from datetime import datetime
from utils.utils import hypixel, utils
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
            try:
                data = await hypixel.guild(gnamesearch)
            except ValueError:
                embed = discord.Embed(title="Error", description="""The guild """ + guildname + ' does not exist.', color=0xff0000)
                await ctx.send(embed=embed)
                return
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
            try:
                tag = data['guild']['tag']
            except Exception as e:
                tag = 'N/A'
            try:
                mbrs = len(data['guild']['members'])
            except Exception as e:
                mbrs = 'N/A'

            try:
                gmuuid = data['guild']['members'][0]['uuid']
                gm = await hypixel.getname(gmuuid)
            except Exception as e:
                gm = 'N/A'
                print(f"Couldn't get guild manager: {e}")
            color=random.randint(1, 16777215)
            embed = discord.Embed(title='Guild Info', color=color)
            embed.add_field(name="Guild Name", value=str(gname), inline=True)
            embed.add_field(name="Guild Manager", value=str(gm), inline=True)
            embed.add_field(name="Members", value=str(utils.comma(mbrs)), inline=True)
            embed.add_field(name="Created On", value=str(created), inline=True)
            embed.add_field(name="Guild Level", value=str(utils.comma(glevel)), inline=True)
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