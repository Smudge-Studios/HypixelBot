print('Starting bot...')
print(' Importing Modules...')
import discord
from discord.ext import commands
import asyncio
from configparser import ConfigParser
print(' Modules imported.')


parser = ConfigParser()
parser.read('botconfig.ini')
TOKEN = parser.get('CONFIG', 'token')

def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    # Notice how you can use spaces in prefixes. Try to keep them simple though.
    prefixes = ['h!','H!']


    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)

bot = commands.Bot(command_prefix = get_prefix, case_insensitive=True)
bot.remove_command('help')

initial_extensions = ['commands.help',
                      'commands.player',
                      'commands.bedwars',
                      'commands.skywars',
                      'commands.guild',
                      'commands.ping',
                      'commands.owner.load',
                      'commands.owner.unload',
                      'commands.owner.reload',
                      'commands.owner.stop',
                      'events.commanderror',
                      'events.ready']

print(' Loading Cogs...')
if __name__ == '__main__':
    for extension in initial_extensions:
        print("     Loading extension " + extension + '...')
        bot.load_extension(extension)
        print('     Extension ' + extension + ' loaded.')
print(' Cogs loaded.')



print(' Logging In...')
try:
    bot.run(TOKEN, bot=True, reconnect=True)
except Exception as e:
    print(' ' + str(e))
