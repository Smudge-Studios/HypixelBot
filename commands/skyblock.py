from attr import __description__
import discord
from discord.ext import commands
from mojang import MojangAPI
from configparser import ConfigParser
from utils.utils import utils, hypixel
import random
from datetime import datetime

sb = """`help` - Skyblock command help.
`profiles <player>` - Returns a list of a player's Skyblock profiles.
`profile <player> <profile>` - Returns a player's Skyblock stats on a specified profile.
`auctions <player> <profile>` - Returns a list of a player's Skyblock auctions on a specified profile.
`auction <player> <profile> <auction ID>` - Returns a player's Skyblock auction on a specified profile."""

other = """For a more detailed list of Skyblock commands, [click here](https://github.com/plun1331/HypixelBot/blob/main/COMMANDS.md#skyblock).
If you require more assistance, [join the support server](https://discord.gg/gxB8mRC)."""

parser = ConfigParser()
parser.read('botconfig.ini')
API_KEY = parser.get('CONFIG', 'api_key')

class Skyblock(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.group(aliases=['sb'])
    async def skyblock(self, ctx):
        if ctx.invoked_subcommand is None:
            try:
                color=random.randint(1, 16777215)
                embed = discord.Embed(title="Help", color = color)
                embed.add_field(name="Skyblock Commands", value=sb, inline=False)
                embed.add_field(name="Other Information", value=other, inline=False)
                embed.set_footer(text='Unofficial Hypixel Discord Bot')
                await ctx.send(embed=embed)
            except discord.Forbidden:
                try:
                    await ctx.send("Error: Cannot send embeds in this channel. Please contact a server administrator to fix this issue.")
                    return
                except discord.Forbidden:
                    try:
                        await ctx.author.send("Error: Cannot send messages in that channel. Please contact a server administrator to fix this issue.")
                    except discord.Forbidden:
                        return

    @skyblock.command()
    async def profiles(self, ctx, username: str=None):
        try:
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
                else:
                    data = await hypixel.player(uuid)
                    msg = ''
                    for profile in data['player']['stats']['SkyBlock']['profiles']:
                        profile = data['player']['stats']['SkyBlock']['profiles'][profile]
                        msg = msg+f"{profile['cute_name']}\n"
                    if msg == '':
                        msg = "This player has no skyblock profiles."
                    data = await hypixel.getname(uuid)
                    color=random.randint(1, 16777215)
                    embed = discord.Embed(title=f"{data}'s Skyblock Profiles", description=msg, color=color)
                    await ctx.send(embed=embed)
        except discord.Forbidden:
            try:
                await ctx.send("Error: Cannot send embeds in this channel. Please contact a server administrator to fix this issue.")
                return
            except discord.Forbidden:
                try:
                    await ctx.author.send("Error: Cannot send messages in that channel. Please contact a server administrator to fix this issue.")
                except discord.Forbidden:
                    return

    @skyblock.command()
    async def profile(self, ctx, username: str=None, profile: str=None):
        try:
            #verify if player exists
            if username==None:
                embed = discord.Embed(title="Error", description="""Please provide a username.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
            if profile==None:
                embed = discord.Embed(title="Error", description="""Please provide a profile.""", color=0xff0000)
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
                else:
                    data = await hypixel.player(uuid)
                    i = None
                    pname = 'N/A'
                    for profile1 in data['player']['stats']['SkyBlock']['profiles']:
                        profile1 = data['player']['stats']['SkyBlock']['profiles'][profile1]
                        if profile1['cute_name'].lower() == profile.lower():
                            pname = profile1['cute_name']
                            i = 'Something'
                            data = await hypixel.skyblock.profile(profile1['profile_id'])
                            break
                    if i is None:
                        embed = discord.Embed(title="Error", description="""Invalid Skyblock profile.""", color=0xff0000)
                        await ctx.send(embed=embed)
                        return
                    if data['success'] == False:
                        embed = discord.Embed(title="Error", description="""Something went wrong.""", color=0xff0000)
                        await ctx.send(embed=embed)
                        return
                    try:
                        members = len(data['profile']['members'])
                    except:
                        members = 'N/A'
                    try:
                        bank = round(data['profile']['banking']['balance'], 2)
                    except:
                        bank = 'N/A'
                    data = data['profile']['members'][uuid]
                    try:
                        first_join = data['first_join']
                        time = datetime.fromtimestamp(first_join/1000.0)
                        date = time.strftime("%m/%d/%Y")
                        first_join = str(date)
                    except:
                        first_join = 'N/A'
                    try:
                        deaths = int(data['stats']['deaths'])
                    except:
                        deaths = 'N/A'
                    try:
                        kills = int(data['stats']['kills'])
                    except:
                        kills = 'N/A'
                    try:
                        bids = int(data['stats']['auctions_bids'])
                    except:
                        bids = 'N/A'
                    try:
                        topbid = int(data['stats']['auctions_highest_bid'])
                    except:
                        topbid = 'N/A'
                    try:
                        awon = int(data['stats']['auctions_won'])
                    except:
                        awon = 'N/A'
                    try:
                        purse = round(data['coin_purse'], 2)
                    except:
                        purse = 'N/A'
                    data = await hypixel.getname(uuid)
                    name = data
                    color=random.randint(1, 16777215)
                    embed = discord.Embed(title = f"{name}'s Skyblock Stats on {pname}", color = color)
                    embed.add_field(name="Profile Members", value=utils.comma(members))
                    embed.add_field(name="Profile Bank", value=utils.comma(bank))
                    embed.add_field(name="First Join", value=first_join)
                    embed.add_field(name="Kills", value=utils.comma(kills))
                    embed.add_field(name="Deaths", value=utils.comma(deaths))
                    try:
                        embed.add_field(name="K/D Ratio", value=utils.comma(round(kills/deaths, 2)))
                    except:
                        embed.add_field(name="K/D Ratio", value='N/A')
                    embed.add_field(name="Bids", value=utils.comma(bids))
                    embed.add_field(name="Highest Bid", value=utils.comma(topbid))
                    embed.add_field(name="Auctions Won", value=utils.comma(awon))
                    embed.add_field(name="Purse", value=utils.comma(purse))
                    await ctx.send(embed=embed)


        except discord.Forbidden:
            try:
                await ctx.send("Error: Cannot send embeds in this channel. Please contact a server administrator to fix this issue.")
                return
            except discord.Forbidden:
                try:
                    await ctx.author.send("Error: Cannot send messages in that channel. Please contact a server administrator to fix this issue.")
                except discord.Forbidden:
                    return

    @skyblock.command(aliases=['ah'])
    async def auctions(self, ctx, username: str=None, profile: str=None):
        try:
            #verify if player exists
            if username==None:
                embed = discord.Embed(title="Error", description="""Please provide a username.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
            if profile==None:
                embed = discord.Embed(title="Error", description="""Please provide a profile.""", color=0xff0000)
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
                else:
                    data = await hypixel.player(uuid)
                    ah = None
                    i = None
                    pname = 'N/A'
                    for profile1 in data['player']['stats']['SkyBlock']['profiles']:
                        profile1 = data['player']['stats']['SkyBlock']['profiles'][profile1]
                        if profile1['cute_name'].lower() == profile.lower():
                            pname = profile1['cute_name']
                            i = 'Something'
                            ah = await hypixel.skyblock.auctions(profile1['profile_id'])
                            break
                    if i is None:
                        embed = discord.Embed(title="Error", description="""Invalid Skyblock profile.""", color=0xff0000)
                        await ctx.send(embed=embed)
                        return
                    if data['success'] == False:
                        embed = discord.Embed(title="Error", description="""Something went wrong.""", color=0xff0000)
                        await ctx.send(embed=embed)
                        return
                    if ah is None:
                        embed = discord.Embed(title="Error", description="""Something went wrong.""", color=0xff0000)
                        await ctx.send(embed=embed)
                        return
                    length = len(ah['auctions'])
                    color=random.randint(1, 16777215)
                    if length == 0:
                        data = await hypixel.getname(uuid)
                        name = data
                        embed = discord.Embed(title = f"{name}'s Skyblock Auctions on {pname}", description=f"{name} has no auctions on profile {pname}.", color = color)
                        await ctx.send(embed=embed)
                        return
                    i = await hypixel.getname(uuid)
                    name = i
                    msg = f'{name} on profile {pname} has {length} auctions.\n\n'
                    for auction in ah['auctions']:
                        msg = msg+f"{auction['tier'].lower().capitalize()} {auction['item_name']} - ID: {auction['_id']}\n"
                    embed = discord.Embed(title=f"{name}'s Skyblock Auctions on {pname}", description=msg, color=color)
                    await ctx.send(embed=embed)
        except discord.Forbidden:
            try:
                await ctx.send("Error: Cannot send embeds in this channel. Please contact a server administrator to fix this issue.")
                return
            except discord.Forbidden:
                try:
                    await ctx.author.send("Error: Cannot send messages in that channel. Please contact a server administrator to fix this issue.")
                except discord.Forbidden:
                    return
    
    @skyblock.command(aliases=['a'])
    async def auction(self, ctx, username: str=None, profile: str=None, auction_id: str=None):
        try:
            #verify if player exists
            if username==None:
                embed = discord.Embed(title="Error", description="""Please provide a username.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
            if profile==None:
                embed = discord.Embed(title="Error", description="""Please provide a profile.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
            if auction_id==None:
                embed = discord.Embed(title="Error", description="""Please provide an auction ID.""", color=0xff0000)
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
                data = await hypixel.player(uuid)
                ah = None
                i = None
                pname = 'N/A'
                for profile1 in data['player']['stats']['SkyBlock']['profiles']:
                    profile1 = data['player']['stats']['SkyBlock']['profiles'][profile1]
                    if profile1['cute_name'].lower() == profile.lower():
                        pname = profile1['cute_name']
                        i = 'Something'
                        ah = await hypixel.skyblock.auctions(profile1['profile_id'])
                        break
                if i is None:
                    embed = discord.Embed(title="Error", description="""Invalid Skyblock profile.""", color=0xff0000)
                    await ctx.send(embed=embed)
                    return
                if data['success'] == False:
                    embed = discord.Embed(title="Error", description="""Something went wrong.""", color=0xff0000)
                    await ctx.send(embed=embed)
                    return
                if ah is None:
                    embed = discord.Embed(title="Error", description="""Something went wrong.""", color=0xff0000)
                    await ctx.send(embed=embed)
                    return
                length = len(ah['auctions'])
                color=random.randint(1, 16777215)
                if length == 0:
                    data = await hypixel.getname(uuid)
                    name = data
                    embed = discord.Embed(title = f"{name}'s Skyblock Auction on {pname}", description=f"{name} has no auctions on profile {pname}.", color = color)
                    await ctx.send(embed=embed)
                    return
                i = await hypixel.getname(uuid)
                name = i
                success = False
                for auction in ah['auctions']:
                    if auction['_id'] == auction_id:
                        success = True
                        lore1 = auction['item_lore'].split('§', 1)
                        lore = ''
                        for i in lore1:
                            i = str(i)
                            lore = lore+i[1:]
                        time = datetime.fromtimestamp(auction['start']/1000.0)
                        started = time.strftime("%m/%d/%Y at %H:$M EST")
                        time = datetime.fromtimestamp(auction['end']/1000.0)
                        ends = time.strftime("%m/%d/%Y at %H:$M EST")
                        if auction['bin'] == True:
                            type = "BIN"
                        else:
                            type = 'Auction'
                        bids = len(auction['bids'])
                        topbid = auction['highest_bid_amount']
                        startbid = auction['starting_bid']
                        item = auction['item_name']
                        tier = auction['tier'].lower().capitalize()
                        category = auction['category'].capitalize()
                        claimed = str(auction['claimed'])
                        embed = discord.Embed(title=f"{name}'s Skyblock Auction on {pname}", color=color)
                        embed.add_field(name="Item", value=item)
                        embed.add_field(name="Item Lore", value=lore)
                        embed.add_field(name="Category", value=category)
                        embed.add_field(name="Tier", value=tier)
                        embed.add_field(name="Auction Type", value=type)
                        embed.add_field(name="Amount of Bids", value=utils.comma(bids))
                        embed.add_field(name="Starting Bid", value=utils.comma(startbid))
                        embed.add_field(name="Top Bid", value=utils.comma(topbid))
                        embed.add_field(name="Started", value=started)
                        embed.add_field(name="Ends", value=ends)
                        embed.add_field(name="Claimed", value=claimed)
                        await ctx.send(embed=embed)
                if success == False:
                    embed = discord.Embed(title = f"Error", description=f"Invalid auction.", color = 0xff0000)
                    await ctx.send(embed=embed)
                    return 
        except discord.Forbidden:
            try:
                await ctx.send("Error: Cannot send embeds in this channel. Please contact a server administrator to fix this issue.")
                return
            except discord.Forbidden:
                try:
                    await ctx.author.send("Error: Cannot send messages in that channel. Please contact a server administrator to fix this issue.")
                except discord.Forbidden:
                    return


def setup(bot):
    bot.add_cog(Skyblock(bot))