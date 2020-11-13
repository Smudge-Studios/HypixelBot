import discord
from discord.ext import commands
import asyncio
from urllib.request import Request, urlopen
import json
from utils.utils import *

class OnReady(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        con.log('Successfully logged in as ' + self.bot.user.name + ' | ' + str(self.bot.user.id) + '.')

def setup(bot):
    bot.add_cog(OnReady(bot))