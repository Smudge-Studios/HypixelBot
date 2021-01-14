import discord
from discord.ext import commands
from utils.utils import con
import random
import mystbin

mystbin_client = mystbin.MystbinClient()

class ReloadCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    @commands.is_owner()
    async def logs(self, ctx):
        if ctx.invoked_subcommand is None:
            color=random.randint(1, 16777215)
            try:
                with open('utils\\logs\\bot.log', 'r') as logfile:
                    content = logfile.read()
                paste = await mystbin_client.post(content, syntax="text")
                url = str(paste)
            except:
                paste = await mystbin_client.post('No logs to display.', syntax="text")
                url = str(paste)
            try:
                with open('utils\\logs\\error.log', 'r') as logfile:
                    errors = logfile.read()
                paste = await mystbin_client.post(errors, syntax="text")
                url2 = str(paste)
            except:
                paste = await mystbin_client.post('No errors to display.', syntax="text")
                url2 = str(paste)
            try:
                embed=discord.Embed(title='Logs', description=f"Logs have been uploaded to {url}.\nError logs have also been uploaded to {url2}.", color=color)
                await ctx.author.send(embed=embed)
                embed=discord.Embed(title='Logs', description=f"Check your DMs!", color=color)
                await ctx.send(embed=embed)
            except discord.HTTPException:
                embed=discord.Embed(title='Error', description=f"Sorry, I cannot DM you.", color=0xff0000)
                await ctx.send(embed=embed)
            except discord.Forbidden:
                embed=discord.Embed(title='Error', description=f"Sorry, I cannot DM you.", color=0xff0000)
                await ctx.send(embed=embed)

    @logs.command(aliases=['delete'])
    @commands.is_owner()
    async def wipe(self, ctx, logfile: str=None):
        if logfile is None:
            embed=discord.Embed(title='Error', description=f"Please provide the log file to wipe, either `logs` or `errors`.", color=0xff0000)
            await ctx.send(embed=embed)
            return
        color=random.randint(1, 16777215)
        if logfile.lower() == 'logs':
            con.wipelogs()
            embed=discord.Embed(title='Success', description=f"Console logs successfully wiped.", color=color)
            await ctx.send(embed=embed)
        elif logfile.lower() == 'errors':
            con.wipeerrors()
            embed=discord.Embed(title='Success', description=f"Error logs successfully wiped.", color=color)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title='Error', description=f"Invalis log file, please provide either `logs` or `errors`.", color=0xff0000)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(ReloadCMD(bot))