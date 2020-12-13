import discord
from discord.ext import commands
from utils.utils import utils, hypixel
from utils.embeds import Embeds

pcembed = Embeds().PlayerCount()

class PlayerCountCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['players','count', 'pc'])
    async def playercount(self, ctx):
        perms = None
        if ctx.guild is not None:
            me = ctx.guild.get_member(self.bot.user.id)
            perms = ctx.channel.permissions_for(me)
            if perms.send_messages:
                if not perms.embed_links:
                    await ctx.send("Error: Cannot send embeds in this channel. Please contact a server administrator to fix this issue.")
                    return
                if perms.embed_links:
                    pass
            if not perms.send_messages:
                return
        data = await hypixel.counts()
        if data['success'] == True:
            embeds, paginator = await pcembed.generate(ctx, data, perms)
            await paginator.run(embeds)
        else:
            embed = discord.Embed(title="Error", description="""Couldn't retrieve Hypixel player counts. Please try again later.""", color=0xff0000)
            await ctx.send(embed=embed)
            return

def setup(bot):
    bot.add_cog(PlayerCountCMD(bot))