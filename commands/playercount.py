import discord
from discord.ext import commands
from utils.utils import utils
from aiohttp import ClientSession
from configparser import ConfigParser
import random

parser = ConfigParser()
parser.read('botconfig.ini')
API_KEY = parser.get('CONFIG', 'api_key')

class OnReady(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.session = ClientSession()

    @commands.command(aliases=['players','count'])
    async def playercount(self, ctx):
        try:
            async with self.session.get('https://api.hypixel.net/gameCounts?key=' + API_KEY) as response:
                data = await response.json()
            if data['success'] == True:
                try:
                    lobby = data['games']['MAIN_LOBBY']['players']
                except:
                    lobby = 'N/A'
                try:
                    tournament_lobby = data['games']['TOURNAMENT_LOBBY']['players']
                except:
                    tournament_lobby = 'N/A'
                try:
                    arcade = data['games']['ARCADE']['players']
                except:
                    arcade = 'N/A'
                try:
                    tnt_games = data['games']['TNTGAMES']['players']
                except:
                    tnt_games = 'N/A'
                try:
                    classic_games = data['games']['LEGACY']['players']
                except:
                    classic_games = 'N/A'
                try:
                    duels = data['games']['DUELS']['players']
                except:
                    duels = 'N/A'
                try:
                    uhc = data['games']['UHC']['players']
                except:
                    uhc = 'N/A'
                try:
                    warlords = data['games']['BATTLEGROUND']['players']
                except:
                    warlords = 'N/A'
                try:
                    housing = data['games']['HOUSING']['players']
                except:
                    housing = 'N/A'
                try:
                    bedwars = data['games']['BEDWARS']['players']
                except:
                    bedwars = 'N/A'
                try:
                    smash_heroes = data['games']['SUPER_SMASH']['players']
                except:
                    smash_heroes = 'N/A'
                try:
                    skyblock = data['games']['SKYBLOCK']['players']
                except:
                    skyblock = 'N/A'
                try:
                    blitz_survival_games = data['games']['SURVIVAL_GAMES']['players']
                except:
                    blitz_survival_games = 'N/A'
                try:
                    speed_uhc = data['games']['SPEED_UHC']['players']
                except:
                    speed_uhc = 'N/A'
                try:
                    build_battle = data['games']['BUILD_BATTLE']['players']
                except:
                    build_battle = 'N/A'
                try:
                    mega_walls = data['games']['WALLS3']['players']
                except:
                    mega_walls = 'N/A'
                try:
                    murder_mystery = data['games']['MURDER_MYSTERY']['players']
                except:
                    murder_mystery = 'N/A'
                try:
                    the_pit = data['games']['PIT']['players']
                except:
                    the_pit = 'N/A'
                try:
                    skywars = data['games']['SKYWARS']['players']
                except:
                    skywars = 'N/A'
                try:
                    replay = data['games']['REPLAY']['players']
                except:
                    replay = 'N/A'
                try:
                    cops_and_crims = data['games']['MCGO']['players']
                except:
                    cops_and_crims = 'N/A'
                try:
                    prototype = data['games']['PROTOTYPE']['players']
                except:
                    prototype = 'N/A'
                try:
                    limbo = data['games']['LIMBO']['players']
                except:
                    limbo = 'N/A'
                try:
                    idle = data['games']['IDLE']['players']
                except:
                    idle = 'N/A'
                try:
                    queue = data['games']['QUEUE']['players']
                except:
                    queue = 'N/A'
                try:
                    network = data['playerCount']
                except:
                    network = 'N/A'
                color=random.randint(1, 16777215)
                embed = discord.Embed(title="Hypixel Player Counts", color = color)
                embed.add_field(name='Total', value=str(utils.comma(network)))
                embed.add_field(name='Main Lobby', value=str(utils.comma(lobby)))
                embed.add_field(name='Tournament Lobby', value=str(utils.comma(tournament_lobby)))

                embed.add_field(name='Bedwars', value=str(utils.comma(bedwars)))
                embed.add_field(name='Skywars', value=str(utils.comma(skywars)))
                embed.add_field(name='Skyblock', value=str(utils.comma(skyblock)))

                embed.add_field(name='Arcade', value=str(utils.comma(arcade)))
                embed.add_field(name='Duels', value=str(utils.comma(duels)))
                embed.add_field(name='UHC', value=str(utils.comma(uhc)))

                embed.add_field(name='TNT Games', value=str(utils.comma(tnt_games)))
                embed.add_field(name='Classic Games', value=str(utils.comma(classic_games)))
                embed.add_field(name='Blitz Survival Games', value=str(utils.comma(blitz_survival_games)))
                
                embed.add_field(name='Build Battle', value=str(utils.comma(build_battle)))
                embed.add_field(name='Murder Mystery', value=str(utils.comma(murder_mystery)))
                embed.add_field(name='Housing', value=str(utils.comma(housing)))

                embed.add_field(name='Smash Heroes', value=str(utils.comma(smash_heroes)))
                embed.add_field(name='Speed UHC', value=str(utils.comma(speed_uhc)))
                embed.add_field(name='Mega Walls', value=str(utils.comma(mega_walls)))

                embed.add_field(name='The Pit', value=str(utils.comma(the_pit)))
                embed.add_field(name='Cops and Crims', value=str(utils.comma(cops_and_crims)))
                embed.add_field(name='Warlords', value=str(utils.comma(warlords)))

                embed.add_field(name='Prototype', value=str(utils.comma(prototype)))
                embed.add_field(name='Limbo', value=str(utils.comma(limbo)))
                embed.add_field(name='Replay', value=str(utils.comma(replay)))

                embed.add_field(name='Idle', value=str(utils.comma(idle)))
                embed.add_field(name='Queue', value=str(utils.comma(queue)))
                embed.set_footer(text='Unofficial Hypixel Discord Bot')
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="Error", description="""Couldn't retrieve Hypixel player counts. Please try again later.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
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
    bot.add_cog(OnReady(bot))