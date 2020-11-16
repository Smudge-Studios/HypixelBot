from utils.utils import con
con.wipe()
con.log("Starting bot...")
import discord
import os
from discord.ext import commands
from configparser import ConfigParser

intents = discord.Intents.all()
intents.presences = False
parser = ConfigParser()
parser.read('botconfig.ini')
TOKEN = parser.get('CONFIG', 'token')

def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    # Notice how you can use spaces in prefixes. Try to keep them simple though.
    prefixes = ['h!','H!']


    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)

bot = commands.Bot(command_prefix = get_prefix, case_insensitive=True, intents=intents)
bot.remove_command('help')

def load_extension(extension):
    try:
        bot.load_extension(extension)
    except Exception as e:
        con.log(f"Couldn't load {extension}: {e}")

for file in os.listdir("commands"):
    if file.endswith(".py"):
        load_extension(f"commands.{file}".replace('.py',''))

for file in os.listdir("commands/owner"):
    if file.endswith(".py"):
        load_extension(f"commands.owner.{file}".replace('.py',''))

for file in os.listdir("events"):
    if file.endswith(".py"):
        load_extension(f"events.{file}".replace('.py',''))

for file in os.listdir("tasks"):
    if file.endswith(".py"):
        load_extension(f"tasks.{file}".replace('.py',''))

con.log('Logging In...')
try:
    bot.run(TOKEN, bot=True, reconnect=True)
except Exception as e:
    con.log(str(e))
