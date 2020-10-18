import discord
from discord.ext import commands


class LoadCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, *, cog: str):
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        print(f'{ctx.author.name} ({ctx.author.id}) is attempting to load extension {cog}...')
        try:
            self.bot.load_extension(cog)
            print(f'Successfully loaded extension {cog}.')
        except Exception as e:
            embed = discord.Embed(title='Error', description=str(e), color=0xff0000)
            await ctx.send(embed=embed)
            print(f"Couldn't load extension {cog}: {e}")
        else:
            embed = discord.Embed(title='Success', description=f'Successfully loaded extension {cog}', color=0xff0000)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(LoadCMD(bot))