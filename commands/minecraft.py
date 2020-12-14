import discord
from discord.ext import commands
from mojang import MojangAPI
from utils.utils import hypixel
import random

class Minecraft(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def skin(self, ctx, username:str=None):
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
        if username==None:
            embed = discord.Embed(title="Error", description="""Please provide a username.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        uuid = MojangAPI.get_uuid(str(username))
        if uuid == '5d1f7b0fdceb472d9769b4e37f65db9f':
            embed = discord.Embed(title="Error", description="""That user does not exist.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        elif not uuid:
            embed = discord.Embed(title="Error", description="""That user does not exist.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        color=random.randint(1, 16777215)
        name = await hypixel.getname(uuid)
        embed = discord.Embed(title=f"{name}'s Skin", description=f"[Download](https://crafatar.com/skins/{uuid})", color=color)
        embed.set_image(url=f"https://crafatar.com/renders/body/{uuid}")
        await ctx.send(embed=embed)
        
            

def setup(bot):
    bot.add_cog(Minecraft(bot))