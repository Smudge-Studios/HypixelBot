import discord
from discord.ext import commands
from mojang import MojangAPI
from utils.utils import utils, hypixel
import random

class MurderMysteryCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['mm'])
    async def murdermystery(self, ctx, username:str=None):
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
        try:
            played = data['player']['stats']['MurderMystery']['games']
        except:
            played = 'N/A'
        try:
            deaths = data['player']['stats']['MurderMystery']['deaths']
        except:
            deaths = 'N/A'
        try:
            kkills = data['player']['stats']['MurderMystery']['knife_kills']
        except:
            kkills = 'N/A'
        try:
            bkills = data['player']['stats']['MurderMystery']['bow_kills']
        except:
            bkills = 'N/A'
        try:
            wins = data['player']['stats']['MurderMystery']['wins']
        except:
            wins = 'N/A'
        data = await hypixel.getname(uuid)
        if data is None:
            embed = discord.Embed(title="Error", description="""Something went wrong. Please try again later.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        color=random.randint(1, 16777215)
        embed = discord.Embed(title=data + "'s Murder Mystery Stats", color=color)
        embed.set_thumbnail(url='https://crafatar.com/renders/head/' + uuid)
        embed.add_field(name='Games Played', value=str(utils.comma(played)))
        embed.add_field(name='Wins', value=str(utils.comma(wins)))
        embed.add_field(name='Deaths', value=str(utils.comma(deaths)))
        embed.add_field(name='Knife Kills', value=str(utils.comma(kkills)))
        embed.add_field(name='Bow Kills', value=str(utils.comma(bkills)))
        try:
            embed.add_field(name='Total Kills', value=str(utils.comma(int(kkills)+int(bkills))))
        except:
            embed.add_field(name='Total Kills', value='N/A')
        embed.set_footer(text='Unofficial Hypixel Discord Bot')
        await ctx.send(embed=embed)
        
        

def setup(bot):
    bot.add_cog(MurderMysteryCMD(bot))