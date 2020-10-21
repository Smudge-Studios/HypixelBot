import discord
from discord.ext import commands
import requests
from configparser import ConfigParser

parser = ConfigParser()
parser.read('botconfig.ini')
API_KEY = parser.get('CONFIG', 'api_key')

def getLevelFromXP(xp):
        REQ_EXP = [
        100000,
        150000,
        250000,
        500000,
        750000,
        1000000,
        1250000,
        1500000,
        2000000,
        2500000,
        2500000,
        2500000,
        2500000,
        2500000,
        3000000
        ]
        lvl = 0
        for i in range(1000):
            needed = 0
            if  i >= len(REQ_EXP):
                needed = REQ_EXP[len(REQ_EXP) - 1]
            else:
                needed = REQ_EXP[i]
            xp -= needed
            if xp < 0:
                return lvl
            else:
                lvl += 1
        return 'N/A'

class GuildCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['g'])
    async def guild(self, ctx, *guildname):
        gname = ' '.join(guildname)
        if not gname:
            embed = discord.Embed(title="Error", description='Please provide a guild to search for.', color=0xff0000)
            await ctx.send(embed=embed)
            return
        gnamesearch = '%20'.join(guildname)
        r = requests.get(url='https://api.hypixel.net/findGuild?key=' + API_KEY + '&byName=' + gnamesearch)
        data = r.json()
        gid = data['guild']
        if gid == None:
            embed = discord.Embed(title="Error", description="""The guild """ + gname + ' does not exist.', color=0xff0000)
            await ctx.send(embed=embed)
            return
        else:
            r = requests.get(url='https://api.hypixel.net/guild?key=' + API_KEY + '&id=' + gid)
            data = r.json()

        try:
            glevel = getLevelFromXP(xp=data['guild']['exp'])
        except:
            glevel = 'N/A'
        try:
            gname = data['guild']['name']
        except:
            #should never happen
            gname = 'N/A'
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

            date_time = time.strftime("%m/%d/%Y at %H:%M")
            created = str(date) + ' at ' + str(hour) + ':' + str(minute) + ' ' + ampm + ', EST'
        except:
            created = 'N/A'
        try:
            desc = data['guild']['description']
        except:
            desc = 'N/A'
        try:
            tag = data['guild']['tag']
        except:
            tag = 'N/A'
        try:
            gmuuid = data['guild']['members'][0]['uuid']
            r = requests.get(url = "https://sessionserver.mojang.com/session/minecraft/profile/" + gmuuid)
            data = r.json()
            gm = data['name']
        except:
            gm = 'N/A'
        embed = discord.Embed(title='Guild Info', color=0xff0000)
        embed.add_field(name="Guild Name", value=str(gname), inline=True)
        embed.add_field(name="Guild Manager", value=str(gm), inline=True)
        embed.add_field(name="Created On", value=str(created), inline=True)
        embed.add_field(name="Guild Level", value=str(int(glevel)), inline=True)
        embed.add_field(name="Guild Description", value=str(desc), inline=True)
        embed.add_field(name="Guild Tag", value=str(tag), inline=True)
        embed.set_footer(text='Unofficial Hypixel Discord Bot')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(GuildCMD(bot))