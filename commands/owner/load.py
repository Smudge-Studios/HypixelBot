import discord
from discord.ext import commands
from utils.utils import con
import random

class LoadCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, *, cog: str):
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        con.log(f'{ctx.author.name} ({ctx.author.id}) is attempting to load extension {cog}...')
        try:
            self.bot.load_extension(cog)
            con.log(f'Successfully loaded extension {cog}.')
        except Exception as e:
            embed = discord.Embed(title='Error', description=str(e), color=0xff0000)
            await ctx.send(embed=embed)
            con.log(f"Couldn't load extension {cog}: {e}")
        else:
            color=random.randint(1, 16777215)
            embed = discord.Embed(title='Success', description=f'Successfully loaded extension {cog}', color=color)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(LoadCMD(bot))