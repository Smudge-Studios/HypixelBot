from utils.utils import con
import discord
import os
from discord.ext import commands
from configparser import ConfigParser
con.start()
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
    ext = extension.replace('/', '.')
    try:
        bot.load_extension(ext)
        con.log(f"{ext} loaded.")
    except Exception as e:
        con.log(f"Couldn't load {ext}: {e}")


for dir_name in ["commands", "commands/owner", "events", "tasks"]:
    for file in os.listdir(dir_name):
        if file.endswith(".py"):
            load_extension(f"{dir_name}.{file}".replace('.py', ''))

con.log('Logging In...')
try:
    bot.run(TOKEN, bot=True, reconnect=True)
except Exception as e:
    con.log(str(e))
