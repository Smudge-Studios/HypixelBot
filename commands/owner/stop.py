import discord
from discord.ext import commands
from utils.utils import con

class StopCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['shutdown','logout'], hidden=True)
    @commands.is_owner()
    async def stop(self, ctx):
        con.log(f'{ctx.author.id} is attempting to remotely shutdown the bot...')
        await ctx.send('Stopping the bot...')
        try:
            await self.bot.logout()
        except Exception as e:
            embed = discord.Embed(title='Error', description=str(e), color=0xff0000)
            await ctx.send(embed=embed)
            con.log(f"Couldn't stop the bot: {e}")

def setup(bot):
    bot.add_cog(StopCMD(bot))