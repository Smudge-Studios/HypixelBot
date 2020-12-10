import discord
from discord.ext import commands
from utils.utils import hypixel
import random

class LeaderboardCMD(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['lb'])   
    async def leaderboard(self, ctx, game: str=None, *, type: str=None):
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
        if game is None:
            embed = discord.Embed(title="Error", description="""Please provide a game.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        if type is None:
            embed = discord.Embed(title="Error", description="""Please provide a leaderboard.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        #send request
        data = await hypixel.leaderboards()
        #errors
        if data['success'] == False:
            embed = discord.Embed(title="Error", description="""Something went wrong.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        #it worked!
        elif data['success'] == True:
            game = game.upper()
            type = type.lower()
            leaders = None
            path = None
            for lb in data['leaderboards']:
                if lb == game.upper():
                    for reekid in data['leaderboards'][lb]:
                        if reekid['path'].replace('_', ' ') == type:
                            path = reekid['path']
                            leaders = reekid['leaders']
                            break
            if leaders is None:
                embed = discord.Embed(title='Error', description='Invalid leaderboard.', color=0xff0000)
                await ctx.send(embed=embed)
                return
            msg = ''
            num = 0
            async with ctx.channel.typing():
                for uid in leaders:
                    uid = uid.replace('-','')
                    name = await hypixel.getname(uid)
                    if name is None:
                        name = 'N/A'
                    num += 1
                    msg += f"{num}: {name}\n"
                color=random.randint(1, 16777215)
                path = path.capitalize()
                path = path.replace('_', ' ')
                embed = discord.Embed(title=f'{game.lower().capitalize()}: {path} leaderboard', description=msg, color=color)
                embed.set_footer(text='Unofficial Hypixel Discord Bot')
                await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(LeaderboardCMD(bot))