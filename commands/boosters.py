import discord
from discord.ext import commands
from configparser import ConfigParser

from win32con import EXCEPTION_ACCESS_VIOLATION
from utils.utils import utils, hypixel
import random
import os
from datetime import datetime

parser = ConfigParser()
parser.read('botconfig.ini')
API_KEY = parser.get('CONFIG', 'api_key')

class BoosterCMDs(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['boosts'])
    async def boosters(self, ctx, *, game:str=None):
        color=random.randint(1, 16777215)
        try:
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
            id = utils.gameidconverter(_game)
            msg = ''
            for booster in data:
                if booster['gameType'] == id:
                    user = await hypixel.getname(booster['purchaserUuid'])
                    msg = msg+f"{user} - ID: {booster['_id']}\n"
            if msg == '':
                msg = f"There are currently 0 {game.lower().capitalize()} boosters active."
            embed = discord.Embed(title="Hypixel Boosters", description=msg)
            embed.set_footer(text='Unofficial Hypixel Discord Bot')
            try:
                await ctx.send(embed=embed)
            except discord.HTTPException:
                msg = ''
                for booster in data:
                    if booster['gameType'] == id:
                        msg = msg+f"ID: {booster['_id']}\n"
                embed = discord.Embed(title="Hypixel Boosters", description=msg, color=color)
                embed.set_footer(text='Unofficial Hypixel Discord Bot')
                try:
                    await ctx.send(embed=embed)
                except discord.HTTPException:
                    fid = random.randint(766674, 478394367980)
                    with open(f'files\\boosters{fid}.txt', 'w', encoding='utf-8') as file:
                        content = ''
                        for booster in data:
                            if booster['gameType'] == id:
                                id = booster['_id']
                                user = await hypixel.getname(booster['purchaserUuid'])
                                content = content+f"{user} - ID: {id}\n"
                        file.write(content)
                    with open(f'files\\boosters{fid}.txt', 'r', encoding='utf-8') as file:
                        try:
                            await ctx.send(file=discord.File(file, f"Boosters.txt"))
                        except discord.Forbidden:
                            embed = discord.Embed(title="Error", description="""Cannot send files in this channel.""", color=0xff0000)
                            await ctx.send(embed=embed)
                            return
                        except discord.HTTPException:
                            embed = discord.Embed(title="Error", description="""Something went wrong.""", color=0xff0000)
                            await ctx.send(embed=embed)
                        if os.path.exists(f'files\\boosters{fid}.txt'):
                            os.remove(f'files\\boosters{fid}.txt')
        except discord.Forbidden:
            try:
                await ctx.send("Error: Cannot send embeds in this channel. Please contact a server administrator to fix this issue.")
                return
            except discord.Forbidden:
                try:
                    await ctx.author.send("Error: Cannot send messages in that channel. Please contact a server administrator to fix this issue.")
                except discord.Forbidden:
                    return
        
    @commands.command(aliases=['boost'])
    async def booster(self, ctx, booster: str=None):
        color=random.randint(1, 16777215)
        try:
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
            try:
                exp = 'N/A'
                seconds = int(float(info['length']))
                min, sec = divmod(seconds, 60) 
                hour, min = divmod(min, 60) 
                if hour == 0:
                    if min == 0:
                        exp = f'0:{sec}'
                    elif min > 0:
                        if len(min) == 1:
                            if len(sec) == 1:
                                exp = f"0{min}:0{sec}"
                            else:
                                exp = f"0{min}:{sec}"
                        else:
                            if len(sec) == 1:
                                exp = f"{min}:0{sec}"
                            else:
                                exp = f"{min}:{sec}"
                elif hour > 0:
                    if len(hour) == 1:
                        if len(min) == 1:
                            exp = f"0{hour}:0{min}"
                        else:
                            exp = f"0{hour}:{min}"
                    else:
                        exp = f"{hour}:{min}"
            except:
                exp = 'N/A'
            try:
                user = await hypixel.getname(info['purchaserUuid'])
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
                        if len(min) == 1:
                            if len(sec) == 1:
                                length = f"0{min}:0{sec}"
                            else:
                                length = f"0{min}:{sec}"
                        else:
                            if len(sec) == 1:
                                length = f"{min}:0{sec}"
                            else:
                                length = f"{min}:{sec}"
                elif hour > 0:
                    if len(hour) == 1:
                        if len(min) == 1:
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
            embed.set_thumbnail(url='https://crafatar.com/avatars/' + uuid)
            embed.add_field(name="Player", value=user)
            embed.add_field(name="Game", value=game)
            embed.add_field(name="Multiplier", value=multiplier)
            embed.add_field(name="Started", value=started)
            embed.add_field(name="Duration", value=length)
            embed.add_field(name="Time Remaining", value=exp)
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

def setup(bot):
    bot.add_cog(BoosterCMDs(bot))