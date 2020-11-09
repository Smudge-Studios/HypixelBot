import discord
from discord.ext import commands
from datetime import datetime
import traceback
from utils import con

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
            print("")
            con.log(f'Ignoring exception in command {ctx.command}: {str(error)}\nThe full traceback has been sent to logs\\errors.log')
            with open('logs\\errors.log', 'a') as logfile:
                now = datetime.now()
                time = now.strftime("%d/%m/%Y at %H:%M")
                logfile.write(f"An unhandled exception occurred in command {ctx.command} on {time}:\n\n")
                traceback.print_exception(type(error), error, error.__traceback__, file=logfile)
                logfile.write('\n============')
            return

def setup(bot):
    bot.add_cog(CMDError(bot))