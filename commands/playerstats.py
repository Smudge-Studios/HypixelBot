import discord
from discord.ext import commands
from mojang import MojangAPI
from utils.utils import utils, hypixel
from utils.embeds import Embeds
import random

class PlayerStats(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['p'])
    async def player(self, ctx, username:str=None):
        perms = None
        if ctx.guild is not None:
            me = ctx.guild.get_member(self.bot.user.id)
            perms = ctx.channel.permissions_for(me)
            if perms.send_messages:
                if not perms.embed_links:
                    await ctx.send("Error: Cannot send embeds in this channel. Please contact a server administrator to fix this issue.")
                    return
                if perms.embed_links:
                    if not perms.add_reactions:
                        embed=discord.Embed(title="Error", description="Cannot add reactions in this channel. Please contact a server administrator to fix this issue.", color=0xff0000)
                        await ctx.send(embed=embed)
                        return
                    if perms.add_reactions:
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
        #send request
        data = await hypixel.player(uuid)
        #errors
        if data['success'] == False:
            embed = discord.Embed(title="Error", description="""Something went wrong.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        #it worked!
        elif data['success'] == True:
            if data['player']==None:
                embed = discord.Embed(title="Error", description="""That player has never joined the Hypixel Network.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
        name = await hypixel.getname(uuid)
        embeds, paginator = await Embeds().Player().generate(ctx, name, data, perms)
        await paginator.run(embeds)

    @commands.command(aliases=['bw'])   
    async def bedwars(self, ctx, username:str=None):
        perms = None
        if ctx.guild is not None:
            me = ctx.guild.get_member(self.bot.user.id)
            perms = ctx.channel.permissions_for(me)
            if perms.send_messages:
                if not perms.embed_links:
                    await ctx.send("Error: Cannot send embeds in this channel. Please contact a server administrator to fix this issue.")
                    return
                if perms.embed_links:
                    if not perms.add_reactions:
                        embed=discord.Embed(title="Error", description="Cannot add reactions in this channel. Please contact a server administrator to fix this issue.", color=0xff0000)
                        await ctx.send(embed=embed)
                        return
                    if perms.add_reactions:
                        pass
            if not perms.send_messages:
                return
        #verify if player exists
        if username==None:
            embed = discord.Embed(title="Error", description="""Please provide a username.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        try:
            uuid = MojangAPI.get_uuid(str(username))
        except:
            embed = discord.Embed(title="Error", description="""That user does not exist.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        if uuid == '5d1f7b0fdceb472d9769b4e37f65db9f':
            embed = discord.Embed(title="Error", description="""That user does not exist.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        elif not uuid:
            embed = discord.Embed(title="Error", description="""That user does not exist.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        #send request
        data = await hypixel.player(uuid)
        #errors
        if data['success'] == False:
            if data['cause'] == 'Malformed UUID':
                embed = discord.Embed(title="Error", description="""Something went wrong.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
            else:
                embed = discord.Embed(title="Error", description="""Something went wrong.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
        elif data['success'] == True:
            if data['player'] == None:
                embed = discord.Embed(title="Error", description="""That user has never joined the Hypixel Network.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
        name = await hypixel.getname(uuid)
        embeds, paginator = await Embeds().Bedwars().generate(ctx, name, data, perms)
        await paginator.run(embeds)

    @commands.command(aliases=['sw'])
    async def skywars(self, ctx, username:str=None):
        perms = None
        if ctx.guild is not None:
            me = ctx.guild.get_member(self.bot.user.id)
            perms = ctx.channel.permissions_for(me)
            if perms.send_messages:
                if not perms.embed_links:
                    await ctx.send("Error: Cannot send embeds in this channel. Please contact a server administrator to fix this issue.")
                    return
                if perms.embed_links:
                    if not perms.add_reactions:
                        embed=discord.Embed(title="Error", description="Cannot add reactions in this channel. Please contact a server administrator to fix this issue.", color=0xff0000)
                        await ctx.send(embed=embed)
                        return
                    if perms.add_reactions:
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
        #send request
        data = await hypixel.player(uuid)
        #errors
        if data['success'] == False:
            embed = discord.Embed(title="Error", description="""Something went wrong.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        #it worked!
        elif data['success'] == True:
            if data['player']==None:
                embed = discord.Embed(title="Error", description="""That player has never joined the Hypixel Network.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
        name = await hypixel.getname(uuid)
        embeds, paginator = await Embeds().Skywars().generate(ctx, name, data, perms)
        await paginator.run(embeds)

    @commands.command()
    async def pit(self, ctx, username: str=None):
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
        #verify if player exists
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
        #send request
        data = await hypixel.player(uuid)
        #errors
        if data['success'] == False:
            if data['cause'] == 'Malformed UUID':
                embed = discord.Embed(title="Error", description="""Something went wrong.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
            else:
                embed = discord.Embed(title="Error", description="""Something went wrong.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
        #it worked!
        elif data['success'] == True:
            if data['player'] == None:
                embed = discord.Embed(title="Error", description="""That user has never joined the Hypixel Network.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
        try:
            deaths = data['player']['stats']['Pit']['pit_stats_ptl']['deaths']
        except:
            deaths = 'N/A'
        try:
            dmgdealt = data['player']['stats']['Pit']['pit_stats_ptl']['damage_dealt']
        except:
            dmgdealt = 'N/A'
        try:
            dmgrecieved = data['player']['stats']['Pit']['pit_stats_ptl']['damage_received']
        except:
            dmgrecieved = 'N/A'
        try:
            joins = data['player']['stats']['Pit']['pit_stats_ptl']['joins']
        except:
            joins = 'N/A'
        try:
            kills = data['player']['stats']['Pit']['pit_stats_ptl']['kills']
        except:
            kills = 'N/A'
        try:
            assists = data['player']['stats']['Pit']['pit_stats_ptl']['assists']
        except:
            assists = 'N/A'
        try:
            bdmgdealt = data['player']['stats']['Pit']['pit_stats_ptl']['bow_damage_dealt']
        except:
            bdmgdealt = 'N/A'
        try:
            bdmgrecieved = data['player']['stats']['Pit']['pit_stats_ptl']['bow_damage_received']
        except:
            bdmgrecieved = 'N/A'
        try:
            jumped = data['player']['stats']['Pit']['pit_stats_ptl']['jumped_into_pit']
        except:
            jumped = 'N/A'
        try:
            hits = data['player']['stats']['Pit']['pit_stats_ptl']['sword_hits']
        except:
            hits = 'N/A'
        try:
            bhits = data['player']['stats']['Pit']['pit_stats_ptl']['arrow_hits']
        except:
            bhits = 'N/A'
        data = await hypixel.getname(uuid)
        if data is None:
            embed = discord.Embed(title="Error", description="""Something went wrong. Please try again later.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        color=random.randint(1, 16777215)
        embed = discord.Embed(title=data + "'s Pit Stats", color=color)
        embed.set_thumbnail(url='https://crafatar.com/renders/head/' + uuid)
        embed.add_field(name="Times Joined", value=str(utils.comma(joins)), inline=True)
        embed.add_field(name="Times Jumped into Pit", value=str(utils.comma(jumped)), inline=True)
        embed.add_field(name="Assists", value=str(utils.comma(assists)), inline=True)
        embed.add_field(name="Kills", value=str(utils.comma(kills)), inline=True)
        embed.add_field(name="Deaths", value=str(utils.comma(deaths)), inline=True)
        try:
            embed.add_field(name="K/D Ratio", value=str(utils.comma(round(int(kills)/int(deaths), 2))), inline=True)
        except:
            embed.add_field(name="K/D Ratio", value='N/A', inline=True)
        embed.add_field(name="Melee Damage Dealt", value=str(utils.comma(dmgdealt)), inline=True)
        embed.add_field(name="Melee Damage Received", value=str(utils.comma(dmgrecieved)), inline=True)
        embed.add_field(name="Melee Hits", value=str(utils.comma(hits)))
        embed.add_field(name="Bow Damage Dealt", value=str(utils.comma(bdmgdealt)), inline=True)
        embed.add_field(name="Bow Damage Received", value=str(utils.comma(bdmgrecieved)), inline=True)
        embed.add_field(name="Bow Hits", value=str(utils.comma(bhits)))
        embed.set_footer(text="Unofficial Hypixel Discord Bot")
        await ctx.send(embed=embed)

    @commands.command(aliases=['mm'])
    async def murdermystery(self, ctx, username:str=None):
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
        #verify if player exists
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
        #send request
        data = await hypixel.player(uuid)
        #errors
        if data['success'] == False:
            if data['cause'] == 'Malformed UUID':
                embed = discord.Embed(title="Error", description="""Something went wrong.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
            else:
                embed = discord.Embed(title="Error", description="""Something went wrong.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
        #it worked!
        elif data['success'] == True:
            if data['player'] == None:
                embed = discord.Embed(title="Error", description="""That user has never joined the Hypixel Network.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
        try:
            played = data['player']['stats']['MurderMystery']['games']
        except:
            played = 'N/A'
        try:
            deaths = data['player']['stats']['MurderMystery']['deaths']
        except:
            deaths = 'N/A'
        try:
            kkills = data['player']['stats']['MurderMystery']['knife_kills']
        except:
            kkills = 'N/A'
        try:
            bkills = data['player']['stats']['MurderMystery']['bow_kills']
        except:
            bkills = 'N/A'
        try:
            wins = data['player']['stats']['MurderMystery']['wins']
        except:
            wins = 'N/A'
        data = await hypixel.getname(uuid)
        if data is None:
            embed = discord.Embed(title="Error", description="""Something went wrong. Please try again later.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        color=random.randint(1, 16777215)
        embed = discord.Embed(title=data + "'s Murder Mystery Stats", color=color)
        embed.set_thumbnail(url='https://crafatar.com/renders/head/' + uuid)
        embed.add_field(name='Games Played', value=str(utils.comma(played)))
        embed.add_field(name='Wins', value=str(utils.comma(wins)))
        embed.add_field(name='Deaths', value=str(utils.comma(deaths)))
        embed.add_field(name='Knife Kills', value=str(utils.comma(kkills)))
        embed.add_field(name='Bow Kills', value=str(utils.comma(bkills)))
        try:
            embed.add_field(name='Total Kills', value=str(utils.comma(int(kkills)+int(bkills))))
        except:
            embed.add_field(name='Total Kills', value='N/A')
        embed.set_footer(text='Unofficial Hypixel Discord Bot')
        await ctx.send(embed=embed)

    @commands.command(aliases=['bb'])
    async def buildbattle(self, ctx, username:str=None):
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
        #verify if player exists
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
        #send request
        data = await hypixel.player(uuid)
        #errors
        if data['success'] == False:
            if data['cause'] == 'Malformed UUID':
                embed = discord.Embed(title="Error", description="""Something went wrong.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
            else:
                embed = discord.Embed(title="Error", description="""Something went wrong.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
        #it worked!
        elif data['success'] == True:
            if data['player'] == None:
                embed = discord.Embed(title="Error", description="""That user has never joined the Hypixel Network.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
        try:
            wins = data['player']['stats']['BuildBattle']['wins']
        except:
            wins = 'N/A'
        try:
            played = data['player']['stats']['BuildBattle']['games_played']
        except:
            played = 'N/A'
        try:
            coins = data['player']['stats']['BuildBattle']['coins']
        except:
            coins = 'N/A'
        data = await hypixel.getname(uuid)
        if data is None:
            embed = discord.Embed(title="Error", description="""Something went wrong. Please try again later.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        color=random.randint(1, 16777215)
        embed = discord.Embed(title=data + "'s Build battle Stats", color=color)
        embed.set_thumbnail(url='https://crafatar.com/renders/head/' + uuid)
        embed.add_field(name='Games Played', value=str(utils.comma(played)))
        embed.add_field(name='Wins', value=str(utils.comma(wins)))
        embed.add_field(name='Coins', value=str(utils.comma(coins)))
        embed.set_footer(text='Unofficial Hypixel Discord Bot')
        await ctx.send(embed=embed)

    @commands.command()
    async def uhc(self, ctx, username:str=None):
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
        #verify if player exists
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
        data = await hypixel.player(uuid)
        #errors
        if data['success'] == False:
            if data['cause'] == 'Malformed UUID':
                embed = discord.Embed(title="Error", description="""Something went wrong.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
            else:
                embed = discord.Embed(title="Error", description="""Something went wrong.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
        #it worked!
        elif data['success'] == True:
            if data['player'] == None:
                embed = discord.Embed(title="Error", description="""That user has never joined the Hypixel Network.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
        try:
            coins = data['player']['stats']['UHC']['coins']
        except:
            coins = 'N/A'
        try:
            deaths = data['player']['stats']['UHC']['deaths']
        except:
            deaths = 'N/A'
        try:
            score = data['player']['stats']['UHC']['score']
        except:
            score = 'N/A'
        try:
            kills = data['player']['stats']['UHC']['kills']
        except:
            kills = 'N/A'
        try:
            wins = data['player']['stats']['UHC']['wins']
        except:
            wins = 'N/A'
        data = await hypixel.getname(uuid)
        if data is None:
            embed = discord.Embed(title="Error", description="""Something went wrong. Please try again later.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        color=random.randint(1, 16777215)
        embed = discord.Embed(title=data + "'s UHC Stats", color=color)
        embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{uuid}")
        embed.add_field(name="Coins", value=str(utils.comma(coins)), inline=True)
        embed.add_field(name="Score", value=str(utils.comma(score)), inline=True)
        embed.add_field(name="Wins", value=str(utils.comma(wins)), inline=True)
        embed.add_field(name="Kills", value=str(utils.comma(kills)), inline=True)
        embed.add_field(name="Deaths", value=str(utils.comma(deaths)), inline=True)
        try:
            embed.add_field(name="K/D Ratio", value=str(utils.comma(kills/deaths)), inline=True)
        except:
            embed.add_field(name="K/D Ratio", value=str('N/A'), inline=True)
        embed.set_footer(text='Unofficial Hypixel Discord Bot')
        await ctx.send(embed=embed)

    @commands.command(aliases=['tnt'])
    async def tntgames(self, ctx, username:str=None):
        perms = None
        if ctx.guild is not None:
            me = ctx.guild.get_member(self.bot.user.id)
            perms = ctx.channel.permissions_for(me)
            if perms.send_messages:
                if not perms.embed_links:
                    await ctx.send("Error: Cannot send embeds in this channel. Please contact a server administrator to fix this issue.")
                    return
                if perms.embed_links:
                    if not perms.add_reactions:
                        embed=discord.Embed(title="Error", description="Cannot add reactions in this channel. Please contact a server administrator to fix this issue.", color=0xff0000)
                        await ctx.send(embed=embed)
                        return
                    if perms.add_reactions:
                        pass
            if not perms.send_messages:
                return
        #verify if player exists
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
        data = await hypixel.player(uuid)
        #errors
        if data['success'] == False:
            if data['cause'] == 'Malformed UUID':
                embed = discord.Embed(title="Error", description="""Something went wrong.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
            else:
                embed = discord.Embed(title="Error", description="""Something went wrong.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
        #it worked!
        elif data['success'] == True:
            if data['player'] == None:
                embed = discord.Embed(title="Error", description="""That user has never joined the Hypixel Network.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
        name = await hypixel.getname(uuid)
        if name is None:
            embed = discord.Embed(title="Error", description="""Something went wrong. Please try again later.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        embeds, paginator = await Embeds().TNT().generate(ctx, name, data, perms)
        await paginator.run(embeds)

def setup(bot):
    bot.add_cog(PlayerStats(bot))