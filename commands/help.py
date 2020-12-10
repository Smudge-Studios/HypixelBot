import discord
from discord.ext import commands
from utils.embeds import Embeds

hembed = Embeds().Help()

class HelpCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
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
        embeds, paginator = await hembed.generate(ctx, perms)
        await paginator.run(embeds)

def setup(bot):
    bot.add_cog(HelpCMD(bot))