import discord
from discord.ext import commands

initial_extensions = ['commands.help',
                      'commands.player',
                      'commands.bedwars',
                      'commands.skywars',
                      'commands.guild',
                      'commands.owner.load',
                      'commands.owner.unload',
                      'commands.owner.reload',
                      'commands.owner.stop',
                      'events.commanderror',
                      'events.ready']

class ReloadCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    @commands.is_owner()
    async def reload(self, ctx, *, cog: str):
        try:
            self.bot.unload_extension(cog)
            print(f' Unloaded extension {cog}.')
            self.bot.load_extension(cog)
            print(f' Loaded extension {cog}.')
            print(f'Successfully reloaded extension {cog}.')
        except Exception as e:
            embed = discord.Embed(title='Error', description=str(e), color=0xff0000)
            await ctx.send(embed=embed)
            print(f"Couldn't reload extension {cog}: {e}")
        else:
            embed = discord.Embed(title='Success', description=f'Successfully reloaded extension {cog}', color=0xff0000)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(ReloadCMD(bot))