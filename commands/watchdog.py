import discord
from discord.ext import commands
from utils.utils import hypixel, utils
import random

class WatchDogCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['wd','watchdog','wds'])
    async def watchdogstats(self, ctx):
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
        data = await hypixel.watchdog()
        if data['success'] == True:
            try:
                wdtotal = data['watchdog_total']
            except:
                wdtotal = 'N/A'
            try:
                stafftotal = data['staff_total']
            except:
                stafftotal = 'N/A'
            color=random.randint(1, 16777215)
            embed = discord.Embed(title="Hypixel Watchdog Statistics", color = color)
            embed.add_field(name="Watchdog Bans", value=str(utils.comma(wdtotal)))
            embed.add_field(name="Staff Bans", value=str(utils.comma(stafftotal)))
            try:
                embed.add_field(name="Total Bans", value=str(utils.comma(wdtotal+stafftotal)))
            except:
                embed.add_field(name="Total Bans", value='N/A')
            embed.set_footer(text='Unofficial Hypixel Discord Bot')
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(WatchDogCMD(bot))