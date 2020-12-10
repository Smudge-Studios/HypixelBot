import discord
from discord.ext import commands
from mojang import MojangAPI
from utils.utils import utils, hypixel
import random
from datetime import datetime
import mystbin
from utils.embeds import Embeds

sb = """`help` - Skyblock command help.
`profiles <player>` - Returns data on all of the player's Skyblock profiles.
`auctions <player> <profile>` - Returns a list of a player's Skyblock auctions on a specified profile.
`auction <player> <profile> <auction ID>` - Returns a player's Skyblock auction on a specified profile.
`bazaar <item>` - Returns information about an item in the Bazaar.
`news [article]` - Returns the specified article, or all articles if no article is specified."""

other = """For a more detailed list of Skyblock commands, [click here](https://github.com/plun1331/HypixelBot/blob/main/COMMANDS.md#skyblock).
If you require more assistance, [join the support server](https://discord.gg/gxB8mRC)."""

mystbin_client = mystbin.MystbinClient()
sbembeds = Embeds().Skyblock()

class Skyblock(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.group(aliases=['sb'])
    async def skyblock(self, ctx):
        if ctx.invoked_subcommand is None:
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
            color=random.randint(1, 16777215)
            embed = discord.Embed(title="Help", color = color)
            embed.add_field(name="Skyblock Commands", value=sb, inline=False)
            embed.add_field(name="Other Information", value=other, inline=False)
            embed.set_footer(text='Unofficial Hypixel Discord Bot')
            await ctx.send(embed=embed)

    @skyblock.command()
    async def profiles(self, ctx, username: str=None):
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
                name = await hypixel.getname(uuid)
                if name is None:
                    embed = discord.Embed(title="Error", description="""Something went wrong. Please try again later.""", color=0xff0000)
                    await ctx.send(embed=embed)
                    return
            embeds, paginator = await sbembeds.SkyblockProfiles().generate(ctx, name, data, perms, uuid)
            await paginator.run(embeds)

    @skyblock.command(aliases=['ah'])
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def auctions(self, ctx, username: str=None, profile: str=None):
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
                    if data is None:
                        embed = discord.Embed(title="Error", description="""Something went wrong. Please try again later.""", color=0xff0000)
                        await ctx.send(embed=embed)
                        return
                    name = data
                    embed = discord.Embed(title = f"{name}'s Skyblock Auctions on {pname}", description=f"{name} has no auctions on profile {pname}.", color = color)
                    await ctx.send(embed=embed)
                    return
                name = await hypixel.getname(uuid)
                if name is None:
                    embed = discord.Embed(title="Error", description="""Something went wrong. Please try again later.""", color=0xff0000)
                    await ctx.send(embed=embed)
                    return
                msg1 = ''
                amnt = 0
                embed = discord.Embed(title=f"{name}'s Skyblock Auctions on {pname}", description=f"Collecting data, please wait.\nThis message will be edited once data is ready.", color=color)
                embed.set_footer(text='Unofficial Hypixel Discord Bot')
                message = await ctx.send(embed=embed)
                for auction in ah['auctions']:
                    msg1 += f"{auction['tier'].lower().capitalize()} {auction['item_name']} - ID: {auction['_id']}\n"
                    amnt += 1
                if msg1 == '':
                    msg1 = f"{name} has no auctions on {pname}"
                paste = await mystbin_client.post(msg1.replace('\\', ''), syntax="text")
                url = str(paste)
                embed = discord.Embed(title=f"{name}'s Skyblock Auctions on {pname}", description=f"{name} has {amnt} auctions on profile {pname}\nAuctions have been uploaded to {url}.", color=color)
                embed.set_footer(text='Unofficial Hypixel Discord Bot')
                await message.edit(embed=embed)
                embed = discord.Embed(title=f"Your data is ready!", description=f"I have collected all of {name}'s Skyblock auctions on their {pname} profile.\n[Jump to message]({message.jump_url})", color=color)
                embed.set_footer(text='Unofficial Hypixel Discord Bot')
                await message.send(f"{ctx.author.mention}", embed=embed)
                self.auctions.reset_cooldown(ctx)
    
    @skyblock.command(aliases=['a'])
    async def auction(self, ctx, username: str=None, profile: str=None, auction_id: str=None):
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
                if data is None:
                    embed = discord.Embed(title="Error", description="""Something went wrong. Please try again later.""", color=0xff0000)
                    await ctx.send(embed=embed)
                    return
                name = data
                embed = discord.Embed(title = f"{name}'s Skyblock Auction on {pname}", description=f"{name} has no auctions on profile {pname}.", color = color)
                await ctx.send(embed=embed)
                return
            i = await hypixel.getname(uuid)
            if i is None:
                embed = discord.Embed(title="Error", description="""Something went wrong. Please try again later.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
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
                    embed.set_footer(text='Unofficial Hypixel Discord Bot')
                    await ctx.send(embed=embed)
            if success == False:
                embed = discord.Embed(title = f"Error", description=f"Invalid auction.", color = 0xff0000)
                await ctx.send(embed=embed)
                return 

    @skyblock.command(aliases=['baz'])
    async def bazaar(self, ctx, *, item: str=None):
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
        if item is None:
            embed = discord.Embed(title="Error", description="""Please provide an item.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        data = await hypixel.skyblock.bazaar()
        _item = None
        for i in data['products']:
            if i.lower().replace('_', ' ') == item.lower():
                _item = data['products'][i]['quick_status']
                break
        if _item is None:
            embed = discord.Embed(title="Error", description="""Invalid item.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        try:
            time = datetime.fromtimestamp(data['lastUpdated']/1000.0)
            updated = time.strftime("%m/%d/%Y at %H:%M EST")
        except:
            updated = 'N/A'
        try:
            itemname = ''
            for i in _item['productId'].split('_'):
                itemname += i.lower().capitalize()
                itemname += ' '
        except:
            itemname = 'N/A'
        try:
            sellprice = f"${utils.comma(round((_item['sellPrice']), 2))}"
        except:
            sellprice = 'N/A'
        try:
            sellvolume = utils.comma(_item['sellVolume'])
        except:
            sellvolume = 'N/A'
        try:
            soldperweek = utils.comma(_item['sellMovingWeek'])
        except:
            soldperweek = 'N/A'
        try:
            sellorders = utils.comma(_item['sellOrders'])
        except:
            sellorders = 'N/A'
        try:
            buyprice = f"${utils.comma(round(_item['buyPrice'], 2))}"
        except:
            buyprice = 'N/A'
        try:
            buyvolume = utils.comma(_item['buyVolume'])
        except:
            buyvolume = 'N/A'
        try:
            buyperweek = utils.comma(_item['buyMovingWeek'])
        except:
            buyperweek = 'N/A'
        try:
            buyorders = utils.comma(_item['buyOrders'])
        except:
            buyorders = 'N/A'
        color=random.randint(1, 16777215)
        embed = discord.Embed(title="Hypixel Bazaar", color=color)
        embed.add_field(name='Item', value=itemname, inline=True)
        embed.add_field(name='Sell Value', value=sellprice, inline=True)
        embed.add_field(name='Buy Price', value=buyprice, inline=True)
        embed.add_field(name='Sell Orders', value=sellorders, inline=True)
        embed.add_field(name='Sell Volume', value=sellvolume, inline=True)
        embed.add_field(name='Sold per Week', value=soldperweek, inline=True)
        embed.add_field(name='Buy Orders', value=buyorders, inline=True)
        embed.add_field(name='Buy Volume', value=buyvolume, inline=True)
        embed.add_field(name='Bought per Week', value=buyperweek, inline=True)
        if updated != 'N/A':
            embed.set_footer(text=f"Unofficial Hypixel Discord Bot - Bazaar Updated {updated}")
        else:
            embed.set_footer(text=f"Unofficial Hypixel Discord Bot")
        await ctx.send(embed=embed)

    @skyblock.command()
    async def news(self, ctx, *, article: str=None):
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
        data = await hypixel.skyblock.news(article)
        if data is None:
            embed = discord.Embed(title="Error", description="""Invalid article.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        embeds, paginator = await sbembeds.News().generate(ctx, data, perms)
        await paginator.run(embeds)
        


def setup(bot):
    bot.add_cog(Skyblock(bot))