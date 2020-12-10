import discord
from discord.ext import commands
from datetime import datetime
from utils.utils import hypixel, utils
import random

class GuildCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['g'])
    async def guild(self, ctx, *, guildname:str=None):
        if ctx.guild is not None:
            me = ctx.guild.get_member(self.bot.user.id)
            perms = ctx.channel.permissions_for(me)
            if perms.send_messages:
                if not perms.embed_links:
                    await ctx.send("Error: Cannot send embeds in this channel. Please contact a server administrator to fix this issue.")
                    return
                if perms.embed_links:
                    pass
            if not perms.send_messages:
                return
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
        except:
            glevel = 'N/A'
        try:
            gname = data['guild']['name']
        except:
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
            else: #this should never happen
                hour = None
                ampm = None

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
            mbrs = len(data['guild']['members'])
        except:
            mbrs = 'N/A'
        try:
            gmuuid = data['guild']['members'][0]['uuid']
            gm = await hypixel.getname(gmuuid)
            if gm is None:
                gm = 'N/A'
        except:
            gm = 'N/A'
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

def setup(bot):
    bot.add_cog(GuildCMD(bot))