import discord
from discord.ext import commands
from mojang import MojangAPI
from utils.utils import utils, hypixel
import random

class UHCCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def uhc(self, ctx, username:str=None):
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
            coins = data['player']['stats']['UHC']['coins']
        except:
            coins = 'N/A'
        try:
            deaths = data['player']['stats']['UHC']['deaths']
        except:
            deaths = 'N/A'
        try:
            score = data['player']['stats']['UHC']['score']
        except:
            score = 'N/A'
        try:
            kills = data['player']['stats']['UHC']['kills']
        except:
            kills = 'N/A'
        try:
            wins = data['player']['stats']['UHC']['wins']
        except:
            wins = 'N/A'
        data = await hypixel.getname(uuid)
        if data is None:
            embed = discord.Embed(title="Error", description="""Something went wrong. Please try again later.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        color=random.randint(1, 16777215)
        embed = discord.Embed(title=data + "'s UHC Stats", color=color)
        embed.set_thumbnail(url='https://crafatar.com/avatars/' + uuid)
        embed.add_field(name="Coins", value=str(utils.comma(coins)), inline=True)
        embed.add_field(name="Score", value=str(utils.comma(score)), inline=True)
        embed.add_field(name="Wins", value=str(utils.comma(wins)), inline=True)
        embed.add_field(name="Kills", value=str(utils.comma(kills)), inline=True)
        embed.add_field(name="Deaths", value=str(utils.comma(deaths)), inline=True)
        try:
            embed.add_field(name="K/D Ratio", value=str(utils.comma(kills/deaths)), inline=True)
        except:
            embed.add_field(name="K/D Ratio", value=str('N/A'), inline=True)
        embed.set_footer(text='Unofficial Hypixel Discord Bot')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(UHCCMD(bot))