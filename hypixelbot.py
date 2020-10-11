import discord
from discord.ext import commands
from discord.utils import get
import random
import asyncio
import requests
from mojang import MojangAPI
import math
from datetime import datetime



TOKEN = <Discord Bot Token>
API_KEY = <API key>


bot = commands.Bot(command_prefix = "h!", case_insensitive=True)
bot.remove_command('help')


delay = 30
async def statuses():
    while True:
        await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name="on the Hypixel Network."))
        await asyncio.sleep(delay)
        await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="commands."))
        await asyncio.sleep(delay)
        await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="plun1331's code."))
        await asyncio.sleep(delay)

@bot.event
async def on_ready():
    print('HypixelBot - Logged in as ' + bot.user.name + ' | ' + str(bot.user.id) + '.')
    await bot.loop.create_task(statuses())

@bot.command()
async def help(ctx):
    if ctx.channel.type == 'dm':
        return
    else:
        color=random.randint(1, 16777215)
        embed = discord.Embed(title="Help", description="""`h!help` - Displays this.
        `h!player <player>` - Returns the specified player's profile.
        `h!bedwars <player>` - Returns the specified player's Bedwars statistics.
        `h!skywars <player>` - Returns the specified player's Skywars statistics.""", color = color)
        embed.set_footer(text='Unofficial Hypixel Discord Bot')
        await ctx.send(embed=embed)

@bot.command(aliases=['p'])
async def player(ctx, username:str=None):
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
    r = requests.get(url = 'https://api.hypixel.net/player?key=' + API_KEY + '&uuid=' + uuid)
    data = r.json()
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
        try:
            #set rank to players rank
            rank = 'N/A'
            if "rank" in data["player"] and data["player"]["rank"] != "NORMAL":
                rank = data["player"]["rank"]
            elif "monthlyPackageRank" in data["player"]:
                if data['player']['monthlyPackageRank'] == "SUPERSTAR":
                    rank = "MVP++"
            elif "newPackageRank" in data["player"]:
                rank = data["player"]["newPackageRank"]
            elif "packageRank" in data["player"]:
                rank = data["player"]["packageRank"]
            else:
                rank = "Default"
            if rank == "VIP_PLUS":
                rank = "VIP+"
            elif rank == "MVP_PLUS":
                rank = "MVP+"
            elif rank == "YOUTUBER":
                rank = "YouTube"
            elif rank == "ADMIN":
                rank = "Administrator"
            elif rank == "MODERATOR":
                rank = "Moderator"
            elif rank == "HELPER":
                rank = "Helper"
            try:
                recent = data['player']['mostRecentGameType']
                if recent == "QUAKECRAFT":
                    recent = "Quake"
                elif recent == "WALLS":
                    recent = 'Walls'
                elif recent == 'PAINTBALL':
                    recent == 'paintball'
                elif recent == 'SURVIVAL_GAMES':
                    recent = 'Blitz Survival Games'
                elif recent == 'TNTGAMES':
                    recent = 'TNT Games'
                elif recent == 'VAMPIREZ':
                    recent = 'VampireZ'
                elif recent == 'WALLS3':
                    recent = 'Mega Walls'
                elif recent == 'ARCADE':
                    recent = 'Arcade'
                elif recent == 'ARENA':
                    recent = 'Arena'
                elif recent == 'UHC':
                    recent = 'UHC Champions'
                elif recent == 'MCGO':
                    recent = 'Cops and Crims'
                elif recent == 'BATTLEGROUND':
                    recent = 'Warlords'
                elif recent == 'SUPER_SMASH':
                    recent = 'Smash Heroes'
                elif recent == 'GINGERBREAD':
                    recent = 'Turbo Kart Racers'
                elif recent == 'HOUSING':
                    recent = 'Housing'
                elif recent == 'SKYWARS':
                    recent = 'Skywars'
                elif recent == 'TRUE_COMBAT':
                    recent = 'Crazy Walls'
                elif recent == 'SPEED_UHC':
                    recent = 'Speed UHC'
                elif recent == 'SKYCLASH':
                    recent = 'SkyClash'
                elif recent == 'LEGACY':
                    recent = 'Classic Games'
                elif recent == 'PROTOTYPE':
                    recent = 'Prototype'
                elif recent == 'BEDWARS':
                    recent = 'BedWars'
                elif recent == 'MURDER_MYSTERY':
                    recent = 'Murder Mystery'
                elif recent == 'BUILD_BATTLE':
                    recent = 'Build Battle'
                elif recent == 'DUELS':
                    recent = 'Duels'
                elif recent == 'SKYBLOCK':
                    recent = 'Skyblock'
                elif recent == 'PIT':
                    recent = 'The Pit'

            except:
                recent = 'N/A'
            try:
                karma = data["player"]["karma"] if "karma" in data["player"] else 0
            except:
                karma = 'N/A'
            try:
                if data['player']['lastLogin'] > data['player']['lastLogout']:
                    status = 'Online'
                elif data['player']['lastLogin'] < data['player']['lastLogout']:
                    time = datetime.fromtimestamp(data['player']['lastLogout']/1000.0)
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

                    date_time = time.strftime("%m/%d/%Y at %H:%M")
                    status = 'Offline - Last seen on ' + date + ' at ' + hour + ':' + minute + ' ' + ampm + ', EST'
                else:
                    status = 'N/A'
            except:
                status = 'N/A'
  
        except:
            embed = discord.Embed(title="Error", description="""An error occured while retriving data on """ + username + ". Please try again later.", color=0xff0000)
            await ctx.send(embed=embed)
            return
        
        color=random.randint(1, 16777215)
        r = requests.get(url = "https://sessionserver.mojang.com/session/minecraft/profile/" + uuid)
        data = r.json()
        embed = discord.Embed(title=data['name'] + "'s Profile", color=0xff0000)
        embed.set_thumbnail(url='https://crafatar.com/avatars/' + uuid)
        embed.add_field(name="Rank", value=str(rank), inline=True)
        embed.add_field(name="Karma", value=str(karma), inline=True)
        embed.add_field(name="Recently Played", value=str(recent), inline=True)
        embed.add_field(name="Status", value=str(status), inline=True)
        embed.set_footer(text='Unofficial Hypixel Discord Bot')
        await ctx.send(embed=embed)
    else:
        print(data['success'])

@bot.command(aliases=['bw'])   
async def bedwars(ctx, username:str=None):
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
    r = requests.get(url = 'https://api.hypixel.net/player?key=' + API_KEY + '&uuid=' + uuid)
    data = r.json()
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
            level = data['player']['achievements']['bedwars_level']
        except:
            level = 'N/A'
        try:
            games_played = data['player']['stats']['Bedwars']['games_played_bedwars']
        except:
            games_played = 'N/A'
        try:
            exp = data['player']['stats']['Bedwars']['Experience']
        except:
            exp = 'N/A'
        try:
            final_deaths = data['player']['stats']['Bedwars']['final_deaths_bedwars']
        except:
            final_deaths = 'N/A'
        try:
            normal_deaths = data['player']['stats']['Bedwars']['deaths_bedwars']
        except:
            normal_deaths = 'N/A'
        try:
            total_deaths = final_deaths+normal_deaths
        except:
            total_deaths = 'N/A'
        try:
            beds_lost = data['player']['stats']['Bedwars']['beds_lost_bedwars']
        except:
            beds_lost = 'N/A'
        try:
            beds_broken = data['player']['stats']['Bedwars']['beds_broken_bedwars']
        except:
            beds_broken = 'N/A'
        try:
            normal_kills = data['player']['stats']['Bedwars']['kills_bedwars']
        except:
            normal_kills = 'N/A'
        try:
            final_kills = data['player']['stats']['Bedwars']['final_kills_bedwars']
        except:
            final_kills = 'N/A'
        try:
            total_kills = final_kills+normal_kills
        except:
            total_kills = 'N/A'
        try:
            wins = data['player']['stats']['Bedwars']['wins_bedwars']
        except:
            wins = 'N/A'
        try:
            losses = data['player']['stats']['Bedwars']['losses_bedwars']
        except:
            losses = 'N/A'
        try:
            winstreak = data['player']['stats']['Bedwars']['winstreak']
        except:
            winstreak = 'N/A'
        
        color=random.randint(1, 16777215)
        r = requests.get(url = "https://sessionserver.mojang.com/session/minecraft/profile/" + uuid)
        data = r.json()
        embed = discord.Embed(title=data['name'] + "'s Bedwars Stats", color=0xff0000)
        embed.set_thumbnail(url='https://crafatar.com/avatars/' + uuid)
        embed.add_field(name="Level", value=str(level), inline=True)
        embed.add_field(name="Games Played", value=str(games_played), inline=True)
        embed.add_field(name="Experience", value=str(round(exp, 0)), inline=True)
        embed.add_field(name="Normal Deaths", value=str(normal_deaths), inline=True)
        embed.add_field(name="Final Deaths", value=str(final_deaths), inline=True)
        embed.add_field(name="Total Deaths", value=str(total_deaths), inline=True)
        embed.add_field(name="Normal Kills", value=str(normal_kills), inline=True)
        embed.add_field(name="Final Kills", value=str(final_kills), inline=True)
        embed.add_field(name="Total Kills", value=str(total_kills), inline=True)
        embed.add_field(name="Normal K/D Ratio", value=str(round(normal_kills/normal_deaths, 2)), inline=True)
        embed.add_field(name="Final K/D Ratio", value=str(round(final_kills/final_deaths, 2)), inline=True)
        embed.add_field(name="K/D Ratio", value=str(round(total_kills/total_deaths, 2)), inline=True)
        embed.add_field(name="Wins", value=str(wins), inline=True)
        embed.add_field(name="Losses", value=str(losses), inline=True)
        embed.add_field(name="W/L Ratio", value=str(round(wins/losses, 2)), inline=True)
        embed.add_field(name="Beds Lost", value=str(beds_lost), inline=True)
        embed.add_field(name="Beds Broken", value=str(beds_broken), inline=True)
        embed.add_field(name="Winstreak", value=str(winstreak), inline=True)
        embed.set_footer(text='Unofficial Hypixel Discord Bot')
        await ctx.send(embed=embed)


@bot.command(aliases=['sw'])   
async def skywars(ctx, username:str=None):
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
    r = requests.get(url = 'https://api.hypixel.net/player?key=' + API_KEY + '&uuid=' + uuid)
    data = r.json()
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
            try:
                xp = data['player']['stats']['SkyWars']['skywars_experience']
                xps = [0, 20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000]
                if xp >= 15000:
                    level = (xp - 15000) / 10000. + 12
                else:
                    for i in range(len(xps)):
                        if xp < xps[i]:
                            level = 1 + i + float(xp - xps[i-1]) / (xps[i] - xps[i-1])
            except:
                level = 'N/A'
            try:
                games_played = data['player']['stats']['SkyWars']['games_played_skywars']
            except:
                games_played = 'N/A'
            try:
                winstreak = data['player']['stats']['SkyWars']['win_streak']
            except:
                winstreak = 'N/A'
            try:
                kills = data['player']['stats']['SkyWars']['kills']
            except:
                kills = 'N/A'
            try:
                deaths = data['player']['stats']['SkyWars']['deaths']
            except:
                deaths = 'N/A'
            try:
                top_winstreak = data['player']['stats']['SkyWars']['highestWinstreak']
            except:
                top_winstreak = 'N/A'
            try:
                coins = data['player']['stats']['SkyWars']['coins']
            except:
                coins = 'N/A'
            try:
                souls = data['player']['stats']['SkyWars']['souls']
            except:
                souls = 'N/A'
            try:
                wins = data['player']['stats']['SkyWars']['wins']
            except:
                wins = 'N/A'
            try:
                losses = data['player']['stats']['SkyWars']['losses']
            except:
                losses = 'N/A'
            
            color=random.randint(1, 16777215)
            r = requests.get(url = "https://sessionserver.mojang.com/session/minecraft/profile/" + uuid)
            data = r.json()
            embed = discord.Embed(title=data['name'] + "'s Skywars Stats", color=0xff0000)
            embed.set_thumbnail(url='https://crafatar.com/avatars/' + uuid)
            try:
                embed.add_field(name="Level", value=str(round(level, 0)), inline=True)
            except:
                embed.add_field(name="Level", value='N/A', inline=True)
            embed.add_field(name="Games Played", value=str(games_played), inline=True)
            embed.add_field(name="Coins", value=str(coins), inline=True)
            embed.add_field(name="Souls", value=str(souls), inline=True)
            embed.add_field(name="Winstreak", value=str(winstreak), inline=True)
            embed.add_field(name="Highest Winstreak", value=str(top_winstreak), inline=True)
            embed.add_field(name="Kills", value=str(kills), inline=True)
            embed.add_field(name="Deaths", value=str(deaths), inline=True)
            try:
                embed.add_field(name="K/D Ratio", value=str(round(int(kills)/int(deaths), 2)), inline=True)
            except:
                embed.add_field(name="K/D Ratio", value='N/A', inline=True)
            embed.add_field(name="Wins", value=str(wins), inline=True)
            embed.add_field(name="Losses", value=str(losses), inline=True)
            try:
                embed.add_field(name="W/L Ratio", value=str(round(int(wins)/int(losses), 2)), inline=True)
            except:
                embed.add_field(name="W/L Ratio", value='N/A', inline=True)
            embed.set_footer(text='Unofficial Hypixel Discord Bot')
            await ctx.send(embed=embed)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="Error", description="""Missing Required Argument.""", color=0xff0000)
        await ctx.send(embed=embed)
        return
    else:
        embed = discord.Embed(title="Error", description="""An unknown error occurred. This error has been reported.""", color=0xff0000)
        await ctx.send(embed=embed)
        print("---------------")
        print("An unknown error occurred.")
        print("")
        print("=====(BEGIN ERROR OUTPUT)=====")
        raise(error)
        print("=====(END ERROR OUTPUT)=====")
        return


bot.run(TOKEN)