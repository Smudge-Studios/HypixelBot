import discord
from discord.ext import commands
from mojang import MojangAPI
from utils.utils import hypixel, utils
from utils.embeds import Embeds
import random
import datetime
import time as thyme
import mystbin

mystbin_client = mystbin.MystbinClient()

class ServerStats(commands.Cog):
    def _init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['lb'])   
    async def leaderboard(self, ctx, game: str=None, *, type: str=None):
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
        if game is None:
            embed = discord.Embed(title="Error", description="""Please provide a game.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        if type is None:
            embed = discord.Embed(title="Error", description="""Please provide a leaderboard.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        #send request
        data = await hypixel.leaderboards()
        #errors
        if data['success'] == False:
            embed = discord.Embed(title="Error", description="""Something went wrong.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        #it worked!
        elif data['success'] == True:
            game = game.upper()
            type = type.lower()
            leaders = None
            path = None
            for lb in data['leaderboards']:
                if lb == game.upper():
                    for reekid in data['leaderboards'][lb]:
                        if reekid['path'].replace('_', ' ') == type:
                            path = reekid['path']
                            leaders = reekid['leaders']
                            break
            if leaders is None:
                embed = discord.Embed(title='Error', description='Invalid leaderboard.', color=0xff0000)
                await ctx.send(embed=embed)
                return
            msg = ''
            num = 0
            async with ctx.channel.typing():
                for uid in leaders:
                    uid = uid.replace('-','')
                    name = await hypixel.getname(uid)
                    if name is None:
                        name = 'N/A'
                    num += 1
                    msg += f"{num}: {name}\n"
                color=random.randint(1, 16777215)
                path = path.capitalize()
                path = path.replace('_', ' ')
                embed = discord.Embed(title=f'{game.lower().capitalize()}: {path} leaderboard', description=msg, color=color)
                embed.set_footer(text='Unofficial Hypixel Discord Bot')
                await ctx.send(embed=embed)

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
            embeds, paginator = await Embeds().PlayerCount().generate(ctx, data, perms)
            await paginator.run(embeds)
        else:
            embed = discord.Embed(title="Error", description="""Couldn't retrieve Hypixel player counts. Please try again later.""", color=0xff0000)
            await ctx.send(embed=embed)
            return

    @commands.command(aliases=['g'])
    async def guild(self, ctx, *, guildname:str=None):
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
        if guildname is None:
            embed = discord.Embed(title="Error", description='Please provide a guild to search for.', color=0xff0000)
            await ctx.send(embed=embed)
            return
        gnamesearch = guildname.replace(' ','%20')
        try:
            data = await hypixel.guild(gnamesearch)
        except ValueError:
            embed = discord.Embed(title="Error", description="""The guild """ + guildname + ' does not exist.', color=0xff0000)
            await ctx.send(embed=embed)
            return
        try:
            glevel = utils.guildlevel(xp=data['guild']['exp'])
        except:
            glevel = 'N/A'
        try:
            gname = data['guild']['name']
        except:
            gname = 'N/A'
        try:
            time = datetime.fromtimestamp(data['guild']['created']/1000.0)
            date = time.strftime("%m/%d/%Y")
            minute = time.strftime("%M")
            if int(time.strftime('%H')) == 12:
                ampm = 'PM'
                hour = time.strftime('%H')
            elif int(time.strftime('%H')) > 12:
                hour = int(time.strftime('%H')) - 12
                ampm = 'PM'
            elif int(time.strftime('%H')) < 12:
                ampm = 'AM'
                hour = time.strftime('%H')
            else: #this should never happen
                hour = None
                ampm = None
            created = str(date) + ' at ' + str(hour) + ':' + str(minute) + ' ' + ampm + ', EST'
        except:
            created = 'N/A'
        try:
            desc = data['guild']['description']
        except:
            desc = 'N/A'
        try:
            tag = data['guild']['tag']
        except:
            tag = 'N/A'
        try:
            mbrs = len(data['guild']['members'])
        except:
            mbrs = 'N/A'
        try:
            gmuuid = data['guild']['members'][0]['uuid']
            gm = await hypixel.getname(gmuuid)
            if gm is None:
                gm = 'N/A'
        except:
            gm = 'N/A'
        color=random.randint(1, 16777215)
        embed = discord.Embed(title='Guild Info', color=color)
        embed.add_field(name="Guild Name", value=str(gname), inline=True)
        embed.add_field(name="Guild Manager", value=str(gm), inline=True)
        embed.add_field(name="Members", value=str(utils.comma(mbrs)), inline=True)
        embed.add_field(name="Created On", value=str(created), inline=True)
        embed.add_field(name="Guild Level", value=str(utils.comma(glevel)), inline=True)
        embed.add_field(name="Guild Description", value=str(desc), inline=True)
        embed.add_field(name="Guild Tag", value=str(tag), inline=True)
        embed.set_footer(text='Unofficial Hypixel Discord Bot')
        await ctx.send(embed=embed)

    @commands.command(aliases=['wd'])
    async def watchdog(self, ctx):
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

    @commands.command(aliases=['boosts'])
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def boosters(self, ctx, *, game:str=None):
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
        if game is None:
            try:
                number = await hypixel.boosters()
            except ValueError:
                embed = discord.Embed(title="Hypixel Boosters", description=f"There are currently 0 boosters active on the network.", color=color)
                await ctx.send(embed=embed)
                return
            embed = discord.Embed(title="Hypixel Boosters", description=f"There are {utils.comma(number)} boosters on the Hypixel Network.\nFor boosters for a specific gamemode, please run `h!boosters <game>`.", color=color)
            await ctx.send(embed=embed)
            return
        try:
            data = await hypixel.boosters('id')
        except ValueError:
            embed = discord.Embed(title="Hypixel Boosters", description=f"There are currently 0 boosters active on the network.", color=color)
            await ctx.send(embed=embed)
            return
        _game = game.replace(' ','_')
        try:
            id = utils.gameidconverter(_game)
        except ValueError:
            embed = discord.Embed(title="Error", description=f"Invalid game.", color=0xff0000)
            await ctx.send(embed=embed)
            return
        msg1 = ''
        amnt = 0
        embed = discord.Embed(title="Hypixel Boosters", description=f"Collecting data, please wait.\nThis message will be edited once data is ready.", color=color)
        embed.set_footer(text='Unofficial Hypixel Discord Bot')
        message = await ctx.send(embed=embed)
        for booster in data:
            if booster['gameType'] == id:
                user = await hypixel.getname(booster['purchaserUuid'])
                msg1 += f"{user} - ID: {booster['_id']}\n"
                amnt += 1
        if msg1 == '':
            msg1 = f"There are currently 0 {game.lower().capitalize()} boosters active."
        paste = await mystbin_client.post(msg1.replace('\\', ''), syntax="text")
        url = str(paste)
        embed = discord.Embed(title="Hypixel Boosters", description=f"There are {amnt} {game.lower().capitalize()} boosters on the network.\nBoosters have been uploaded to {url}.", color=color)
        embed.set_footer(text='Unofficial Hypixel Discord Bot')
        await message.edit(embed=embed)
        embed = discord.Embed(title=f"Your data is ready!", description=f"I have collected all of the {game.lower().capitalize()} boosters.\n[Jump to message]({message.jump_url})", color=color)
        embed.set_footer(text='Unofficial Hypixel Discord Bot')
        await message.send(f"{ctx.author.mention}", embed=embed)
        self.boosters.reset_cooldown(ctx)
        
    @commands.command(aliases=['boost'])
    async def booster(self, ctx, booster: str=None):
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
        current = int(thyme.time())
        if booster is None:
            embed = discord.Embed(title="Error", description="""Please provide a booster ID.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        try:
            data = await hypixel.boosters('all')
        except discord.NotFound:
            embed = discord.Embed(title="Hypixel Boosters", description=f"There are currently 0 boosters active on the network.", color=color)
            await ctx.send(embed=embed)
            return
        info = ''
        for i in data:
            if i['_id'] == booster:
                info = i
                break
        if info == '':
            embed = discord.Embed(title="Hypixel Boosters", description=f"Invalid booster.", color=0xff0000)
            await ctx.send(embed=embed)
            return
        exp = 'N/A'
        passed = current-(info['dateActivated']/1000)
        remaining = info['length']-passed
        seconds = int(float(remaining))
        min, sec = divmod(seconds, 60) 
        hour, min = divmod(min, 60) 
        if hour == 0:
            if min == 0:
                exp = f'{sec} seconds'
            elif min > 0:
                if len(str(min)) == 1:
                    if len(str(sec)) == 1:
                        exp = f"0:0{min}:0{sec}"
                    else:
                        exp = f"0:0{min}:{sec}"
                else:
                    if len(str(sec)) == 1:
                        exp = f"0:{min}:0{sec}"
                    else:
                        exp = f"0:{min}:{sec}"
        elif hour > 0:
            if len(str(hour)) == 1:
                if len(str(min)) == 1:
                    exp = f"0{hour}:0{min}"
                else:
                    exp = f"0{hour}:{min}"
            else:
                exp = f"{hour}:{min}"
        try:
            user = await hypixel.getname(info['purchaserUuid'])
            if user is None:
                embed = discord.Embed(title="Error", description="""Something went wrong. Please try again later.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
        except:
            user = 'N/A'
        try:
            uuid = info['purchaserUuid']
        except:
            uuid = 'N/A'
        try:
            multiplier = info['amount']
        except:
            multiplier = 'N/A'
        try:
            length = 'N/A'
            seconds = int(float(info['originalLength']))
            min, sec = divmod(seconds, 60) 
            hour, min = divmod(min, 60) 
            if hour == 0:
                if min == 0:
                    length = f'0:{sec}'
                elif min > 0:
                    if len(str(min)) == 1:
                        if len(str(sec)) == 1:
                            length = f"0:0{min}:0{sec}"
                        else:
                            length = f"0:0{min}:{sec}"
                    else:
                        if len(str(sec)) == 1:
                            length = f"0:{min}:0{sec}"
                        else:
                            length = f"0:{min}:{sec}"
            elif hour > 0:
                if len(str(hour)) == 1:
                    if len(str(min)) == 1:
                        length = f"0{hour}:0{min}"
                    else:
                        length = f"0{hour}:{min}"
                else:
                    length = f"{hour}:{min}"
        except:
            length = 'N/A'
        try:
            time = datetime.fromtimestamp(info['dateActivated']/1000.0)
            started = time.strftime("%m/%d/%Y at %H:%M EST")
        except:
            started = 'N/A'
        try:
            game = utils.idtogameconverter(int(info['gameType']))
        except:
            game = 'N/A'
        color=random.randint(1, 16777215)
        embed = discord.Embed(title=f"{user}'s {game} booster", color = color)
        embed.set_thumbnail(url='https://crafatar.com/renders/head/' + uuid)
        embed.add_field(name="Player", value=user)
        embed.add_field(name="Game", value=game)
        embed.add_field(name="Multiplier", value=multiplier)
        embed.add_field(name="Started", value=started)
        embed.add_field(name="Duration", value=length)
        embed.add_field(name="Time Remaining", value=exp)
        embed.set_footer(text='Unofficial Hypixel Discord Bot')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(ServerStats(bot))
