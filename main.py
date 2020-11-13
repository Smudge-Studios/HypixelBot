from utils.utils import con
con.log("Starting bot...")
import discord
from discord.ext import commands
import asyncio
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

initial_extensions = ['commands.help',
                      'commands.info',
                      'commands.ping',

                      'commands.player',
                      'commands.bedwars',
                      'commands.skywars',
                      'commands.pit',
                      'commands.murdermystery',
                      'commands.guild',
                      'commands.buildbattle',
                      'commands.uhc',
                      'commands.leaderboards',

                      'commands.playercount',
                      'commands.watchdog',

                      'commands.owner.load',
                      'commands.owner.unload',
                      'commands.owner.reload',
                      'commands.owner.stop',

                      'events.commanderror',
                      'events.ready',
                      
                      'tasks.botlists',
                      'tasks.statuses']

for extension in initial_extensions:
    try:
        bot.load_extension(extension)
    except Exception as e:
        con.log(f"Couldn't load {extension}: {e}")

con.log('Logging In...')
try:
    bot.run(TOKEN, bot=True, reconnect=True)
except Exception as e:
    con.log(str(e))
