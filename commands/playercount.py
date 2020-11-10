import discord
from discord.ext import commands
from utils.utils import con, utils
from urllib.request import Request, urlopen
from configparser import ConfigParser
import json

parser = ConfigParser()
parser.read('botconfig.ini')
API_KEY = parser.get('CONFIG', 'api_key')

class OnReady(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['players','count'])
    async def playercount(self, ctx):
        try:
            req = Request('https://api.hypixel.net/gameCounts?key=' + API_KEY)
            req.add_header('plun1331', 'https://plun1331.github.io')
            content = urlopen(req)
            data = json.load(content) 
            if data['success'] == True:
                try:
                    lobby = data['games']['MAIN_LOBBY']
                except:
                    lobby = 'N/A'
                try:
                    tournament_lobby = data['games']['TOURNAMENT_LOBBY']
                except:
                    tournament_lobby = 'N/A'
                try:
                    arcade = data['games']['ARCADE']
                except:
                    arcade = 'N/A'
                try:
                    tnt_games = data['games']['TNTGAMES']
                except:
                    tnt_games = 'N/A'
                try:
                    classic_games = data['games']['LEGACY']
                except:
                    classic_games = 'N/A'
                try:
                    duels = data['games']['DUELS']
                except:
                    duels = 'N/A'
                try:
                    uhc = data['games']['UHC']
                except:
                    uhc = 'N/A'
                try:
                    warlords = data['games']['BATTLEGROUND']
                except:
                    warlords = 'N/A'
                try:
                    housing = data['games']['HOUSING']
                except:
                    housing = 'N/A'
                try:
                    bedwars = data['games']['BEDWARS']
                except:
                    bedwars = 'N/A'
                try:
                    smash_heroes = data['games']['SUPER_SMASH']
                except:
                    smash_heroes = 'N/A'
                try:
                    skyblock = data['games']['SKYBLOCK']
                except:
                    skyblock = 'N/A'
                try:
                    blitz_survival_games = data['games']['SURVIVAL_GAMES']
                except:
                    blitz_survival_games = 'N/A'
                try:
                    speed_uhc = data['games']['SPEED_UHC']
                except:
                    speed_uhc = 'N/A'
                try:
                    build_battle = data['games']['BUILD_BATTLE']
                except:
                    build_battle = 'N/A'
                try:
                    mega_walls = data['games']['WALLS3']
                except:
                    mega_walls = 'N/A'
                try:
                    murder_mystery = data['games']['MURDER_MYSTERY']
                except:
                    murder_mystery = 'N/A'
                try:
                    the_pit = data['games']['PIT']
                except:
                    the_pit = 'N/A'
                try:
                    skywars = data['games']['SKYWARS']
                except:
                    skywars = 'N/A'
                try:
                    replay = data['games']['REPLAY']
                except:
                    replay = 'N/A'
                try:
                    cops_and_crims = data['games']['MCGO']
                except:
                    cops_and_crims = 'N/A'
                try:
                    prototype = data['games']['PROTOTYPE']
                except:
                    prototype = 'N/A'
                try:
                    limbo = data['games']['LIMBO']
                except:
                    limbo = 'N/A'
                try:
                    idle = data['games']['IDLE']
                except:
                    idle = 'N/A'
                try:
                    queue = data['games']['QUEUE']
                except:
                    queue = 'N/A'
                try:
                    network = data['playerCount']
                except:
                    network = 'N/A'
                embed = discord.Embed(title="Hypixel Player Counts", color = 0xff0000)
                embed.add_field(name='Total', value=utils.comma(network))
                embed.add_field(name='Main Lobby', value=utils.comma(lobby))
                embed.add_field(name='Queue', value=utils.comma(queue))

                embed.add_field(name='Bedwars', value=utils.comma(bedwars))
                embed.add_field(name='Skywars', value=utils.comma(skywars))
                embed.add_field(name='Skyblock', value=utils.comma(skyblock))

                embed.add_field(name='Arcade', value=utils.comma(arcade))
                embed.add_field(name='Duels', value=utils.comma(duels))
                embed.add_field(name='UHC', value=utils.comma(uhc))

                embed.add_field(name='TNT Games', value=utils.comma(tnt_games))
                embed.add_field(name='Classic Games', value=utils.comma(classic_games))
                embed.add_field(name='Blitz Survival Games', value=utils.comma(blitz_survival_games))
                
                embed.add_field(name='Build Battle', value=utils.comma(build_battle))
                embed.add_field(name='Murder Mystery', value=utils.comma(murder_mystery))
                embed.add_field(name='Housing', value=utils.comma(housing))

                embed.add_field(name='Smash Heroes', value=utils.comma(smash_heroes))
                embed.add_field(name='Speed UHC', value=utils.comma(speed_uhc))
                embed.add_field(name='Mega Walls', value=utils.comma(mega_walls))

                embed.add_field(name='The Pit', value=utils.comma(the_pit))
                embed.add_field(name='Cops and Crims', value=utils.comma(cops_and_crims))
                embed.add_field(name='Warlords', value=utils.comma(warlords))

                embed.add_field(name='Prototype', value=utils.comma(prototype))
                embed.add_field(name='Limbo', value=utils.comma(limbo))
                embed.add_field(name='Replay', value=utils.comma(replay))

                embed.add_field(name='Idle', value=utils.comma(idle))
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