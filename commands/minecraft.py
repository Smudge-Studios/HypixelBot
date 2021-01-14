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
        
    @commands.command()
    async def server(self, ctx, ipo: str=None, porto: str="25565"):
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
        if ipo is None:
            ipo = 'mc.hypixel.net'
        data = await hypixel.mcserver(ipo, porto)
        if len(data['ip']) == 0:
            embed = discord.Embed(title="Error", description="""That server does not exist.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        if data['online'] == False:
            embed = discord.Embed(title="Error", description="""That server is currently offline.\nTrying to query a Minecraft: Bedrock Edition server? Try port 19132.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        try:
            hostname = data['hostname']
        except:
            hostname = 'N/A'
        try:
            ip = data['ip']
        except:
            ip = 'N/A'
        try:
            port = data['port']
        except:
            port = 'N/A'
        try:
            vers = data['version']
        except:
            vers = 'N/A'
        try:
            motd = ''
            if isinstance(data['motd']['clean'], list):
                mot = '\n'.join(data['motd']['clean'])
            else:
                mot = data['motd']['clean']
            abc = mot.split('?')
            for strl in abc:
                if strl != ' ':
                    strl = strl[1:]
                motd += strl
            if motd.replace(' ', '') == '':
                motd = "None"
        except:
            motd = "N/A"
        try:
            players = f"{data['players']['online']}/{data['players']['max']}"
        except:
            players = "N/A"
        color=random.randint(1, 16777215)
        embed = discord.Embed(title=f"Information on {ipo}:{porto}", color=color)
        embed.set_thumbnail(url=f'https://api.mcsrvstat.us/icon/{hostname}:{port}')
        embed.add_field(name="Hostname", value=hostname, inline=True)
        embed.add_field(name="IP", value=ip, inline=True)
        embed.add_field(name="Port", value=port, inline=True)
        embed.add_field(name="Version", value=vers, inline=True)
        embed.add_field(name="Players", value=players, inline=True)
        embed.add_field(name="MoTD", value=motd, inline=True)
        embed.set_footer(text="Unofficial Hypixel Discord Bot - Server info retrieved from api.mcsrvstat.us.")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Minecraft(bot))