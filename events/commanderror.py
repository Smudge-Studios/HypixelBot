import discord
from discord.ext import commands
import sys
import traceback
from utils.utils import con

class CMDError(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Error", description="""Missing Required Argument.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        elif isinstance(error, commands.NotOwner):
            embed = discord.Embed(title="Error", description="""This command is restricted.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        else:
            embed = discord.Embed(title="Error", description="""An unknown error occurred. This error has been reported.
            `""" + str(error) + '`', color=0xff0000)
            await ctx.send(embed=embed)
            con.log("")
            con.log('Ignoring exception in command {}:'.format(ctx.command))
            con.log("=====(BEGIN ERROR OUTPUT)=====")
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
            con.log("=====(END ERROR OUTPUT)=====")
            return

def setup(bot):
    bot.add_cog(CMDError(bot))