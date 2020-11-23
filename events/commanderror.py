from attr import __description__
import discord
from discord.ext import commands
import traceback
from configparser import ConfigParser
from utils.utils import con

parser = ConfigParser()
parser.read('botconfig.ini')
try:
    logchannel = int(parser.get('CONFIG', 'log_channel'))
except Exception as e:
    print(f"Couldn't define logchannel: {e}")
    logchannel = None

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
            try:
                raise error
            except:
                tb = traceback.format_exc()
            print("")
            con.log('Ignoring exception in command {}:'.format(ctx.command))
            con.log("=====(BEGIN ERROR OUTPUT)=====")
            print(tb)
            con.log("=====(END ERROR OUTPUT)=====")
            print("")
            with open('utils\\logs\\error.log', 'a') as logfile:
                logfile.write(tb)
            if logchannel is not None:
                channel = self.bot.get_channel(logchannel)
                embed = discord.Embed(title=f"Exception in '{ctx.command}'", description=f"```\n{tb}\n```", color=0xff0000)
                await channel.send(embed=embed)
            return

def setup(bot):
    bot.add_cog(CMDError(bot))