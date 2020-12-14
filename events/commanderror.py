import discord
from discord.ext import commands
import traceback
from configparser import ConfigParser
from utils.utils import con

parser = ConfigParser()
parser.read('config.ini')
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
        elif isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(title="Cooldown", description="""That command is on cooldown, you may use it again once all data has been retrieved.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        else:
            embed = discord.Embed(title="Error", description="""An unknown error occurred. This error has been reported.
            ```\n""" + str(error) + '\n```', color=0xff0000)
            await ctx.send(embed=embed)
            try:
                raise error
            except:
                tb = traceback.format_exc()
            con.log(error)
            with open('utils\\logs\\error.log', 'a') as logfile:
                logfile.write(tb)
            if logchannel is not None:
                channel = self.bot.get_channel(logchannel)
                if channel is not None:
                    embed = discord.Embed(title=f"Exception in '{ctx.command}'", description=f"```\n{tb}\n```", color=0xff0000)
                    try:
                        await channel.send(embed=embed)
                    except discord.Forbidden:
                        raise ValueError("The bot does not have permissions to send messages in the logchannel specified in config.ini.")
                else:
                    raise ValueError("The logchannel specified in config.ini is not visible to the bot, or does not exist.")
            return

def setup(bot):
    bot.add_cog(CMDError(bot))