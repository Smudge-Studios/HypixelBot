import discord
from discord.ext import commands

class StopCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['shutdown','logout'], hidden=True)
    @commands.is_owner()
    async def stop(self, ctx, *, cog: str):
        print('Bot shutting down...')
        try:
            self.bot.logout()
        except Exception as e:
            embed = discordEmbed(title='Error', description=str(e), color=0xff0000)
            await ctx.send(embed=embed)
            print(f"Couldn't stop the bot: {e}")

def setup(bot):
    bot.add_cog(StopCMD(bot))