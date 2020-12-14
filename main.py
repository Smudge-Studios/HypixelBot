from utils.utils import con
import discord
import os
from discord.ext import commands
from configparser import ConfigParser
con.wipe()
con.log("Starting bot...")

intents = discord.Intents.default()
parser = ConfigParser()
parser.read('config.ini')
TOKEN = parser.get('CONFIG', 'token')


def get_prefix(bots, message):
    prefixes = ['h!', 'H!', 'h1', 'H1']
    return commands.when_mentioned_or(*prefixes)(bots, message)


bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True, intents=intents)
bot.remove_command('help')


def load_extension(extension):
    try:
        bot.load_extension(extension)
        con.log(f"{extension} loaded.")
    except Exception as e:
        con.log(f"Couldn't load {extension}: {e}")


for file in os.listdir("commands"):
    if file.endswith(".py"):
        load_extension(f"commands.{file}".replace('.py', ''))

for file in os.listdir("commands/owner"):
    if file.endswith(".py"):
        load_extension(f"commands.owner.{file}".replace('.py', ''))

for file in os.listdir("events"):
    if file.endswith(".py"):
        load_extension(f"events.{file}".replace('.py', ''))

for file in os.listdir("tasks"):
    if file.endswith(".py"):
        load_extension(f"tasks.{file}".replace('.py', ''))

con.log('Logging In...')
try:
    bot.run(TOKEN, bot=True, reconnect=True)
except Exception as e:
    con.log(str(e))
