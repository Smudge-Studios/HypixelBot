import discord
from discord.ext import commands
from utils.utils import utils

class LinkCMDs(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def link(self, ctx, ign):
        try:
            utils.link(ctx, ign)
        except ValueError:
            embed = discord.Embed(title="Error", description="""That user does not exist.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        embed = discord.Embed(title="Success", description=f"""Successfully linked {ign} to your account.""", color=0xff0000)
        await ctx.send(embed=embed)

    @commands.command()
    async def unlink(self, ctx):
        try:
            ign = utils.unlink(ctx)
        except ValueError:
            embed = discord.Embed(title="Error", description="""You do not have a user linked to your account.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        embed = discord.Embed(title="Success", description=f"""Successfully unlinked {ign} from your account.""", color=0xff0000)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(LinkCMDs(bot))