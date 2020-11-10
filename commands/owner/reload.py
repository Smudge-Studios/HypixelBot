import discord
from discord.ext import commands
from utils.utils import con
import random
class ReloadCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    @commands.is_owner()
    async def reload(self, ctx, *, cog: str):
        try:
            self.bot.unload_extension(cog)
            con.log(f' Unloaded extension {cog}.')
            self.bot.load_extension(cog)
            con.log(f' Loaded extension {cog}.')
            con.log(f'Successfully reloaded extension {cog}.')
        except Exception as e:
            embed = discord.Embed(title='Error', description=str(e), color=0xff0000)
            await ctx.send(embed=embed)
            con.log(f"Couldn't reload extension {cog}: {e}")
        else:
            color=random.randint(1, 16777215)
            embed = discord.Embed(title='Success', description=f'Successfully reloaded extension {cog}', color=color)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(ReloadCMD(bot))