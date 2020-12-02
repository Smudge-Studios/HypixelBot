import asyncio
import discord
from discord.ext import commands
from configparser import ConfigParser
from utils.utils import utils, hypixel
import random
import os
from datetime import datetime
import mystbin
import time as thyme

mystbin_client = mystbin.MystbinClient()
parser = ConfigParser()
parser.read('botconfig.ini')
API_KEY = parser.get('CONFIG', 'api_key')

class BoosterCMDs(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['boosts'])
    @commands.cooldown(1, 3600, commands.BucketType.user)
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
            await asyncio.sleep(2)
            paste = await mystbin_client.post(msg1, syntax="text")
            url = str(paste)
            embed = discord.Embed(title="Hypixel Boosters", description=f"There are {amnt} {game.lower().capitalize()} boosters on the network.\nBoosters have been uploaded to {url}.", color=color)
            embed.set_footer(text='Unofficial Hypixel Discord Bot')
            await message.edit(embed=embed)
            embed = discord.Embed(title=f"Your data is ready!", description=f"I have collected all of the {game.lower().capitalize()} boosters.\n[Jump to message]({message.jump_url})", color=color)
            embed.set_footer(text='Unofficial Hypixel Discord Bot')
            await ctx.send(f"{ctx.author.mention}", embed=embed)
            self.boosters.reset_cooldown(ctx)
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
        current = int(thyme.time())
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