import discord
from discord.ext import commands
from utils.utils import hypixel, utils
import random

class InfoCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
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
        data = await hypixel.key()
        try:
            queries = data['record']['totalQueries']
        except:
            queries = 'N/A'
        try:
            queriesmin = data['record']['queriesInPastMin']
        except:
            queriesmin = 'N/A'
        color=random.randint(1, 16777215)
        embed = discord.Embed(title="Bot Information", description=f"""This bot was coded by plun1331#5535.
This bot is also open-sourced. You can view the source code [here](https://github.com/plun1331/HypixelBot)""", color = color)
        embed.add_field(name="Stats", value=f"""Amount of API Requests made in the past minute: {queriesmin}
Total API Requests: {queries}
Guilds: {utils.comma(len(self.bot.guilds))}""", inline=False)
        embed.add_field(name="Invite", value=f"""You can invite the bot by clicking [here](https://plun1331.github.io/hypixelbot/add)""", inline=False)
        embed.add_field(name="Vote", value=f"""You can vote for the bot on the following bot lists:
[Top.GG](https://top.gg/bot/764677833820995605/vote)
[Discord Bot List](https://discordbotlist.com/bots/hypixelbot/upvote)""", inline=False)
        embed.add_field(name="Support", value=f"""You can join the support server at [https://discord.gg/gxB8mRC](https://discord.gg/gxB8mRC)""", inline=False)
        embed.set_footer(text='Unofficial Hypixel Discord Bot')
        await ctx.send(embed=embed)

    @commands.command()
    async def invite(self, ctx):
        await ctx.send("https://plun1331.github.io/hypixelbot/add")

def setup(bot):
    bot.add_cog(InfoCMD(bot))