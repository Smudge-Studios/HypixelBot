import discord
from discord.ext import commands
from configparser import ConfigParser
from utils.utils import hypixel
import random

parser = ConfigParser()
parser.read('botconfig.ini')
API_KEY = parser.get('CONFIG', 'api_key')

class LeaderboardCMD(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['lb'])   
    async def leaderboard(self, ctx, game: str=None, *, type: str=None):
        try:
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
                async with ctx.channel.typing():
                    for uid in leaders:
                        uid = uid.replace('-','')
                        name = await hypixel.getname(uid)
                        msg = msg + f"{name}\n"
                    color=random.randint(1, 16777215)
                    embed = discord.Embed(title=f'{game.lower().capitalize()}: {path.capitalize()} leaderboard', description=msg, color=color)
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
    bot.add_cog(LeaderboardCMD(bot))