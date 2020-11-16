import datetime
from datetime import datetime
from aiohttp import ClientSession
from configparser import ConfigParser

parser = ConfigParser()
parser.read('botconfig.ini')
API_KEY = parser.get('CONFIG', 'api_key')

class con:
    def log(text):
        with open('utils\\logs\\bot.log', 'a') as logfile:
            now = datetime.now()
            time = now.strftime("%m/%d/%Y %H:%M")
            logfile.write(f"{time}: {text}\n\n")
        print(f"{time}: {text}")
    
    def wipe():
        with open('utils\\logs\\bot.log', 'w'):
            pass

class utils:
    def comma(self, num):
        '''Add comma to every 3rd digit. Takes int or float and
        returns string.'''
        if type(num) == int:
            return '{:,}'.format(num)
        elif type(num) == float:
            return '{:,.2f}'.format(num) # Rounds to 2 decimal places
        elif type(num) == str:
            return num

    def guildlevel(self, xp):
        """ Return a guild's level from XP. """
        REQ_EXP = [
        100000,
        150000,
        250000,
        500000,
        750000,
        1000000,
        1250000,
        1500000,
        2000000,
        2500000,
        2500000,
        2500000,
        2500000,
        2500000,
        3000000
        ]
        lvl = 0
        for i in range(1000):
            needed = 0
            if  i >= len(REQ_EXP):
                needed = REQ_EXP[len(REQ_EXP) - 1]
            else:
                needed = REQ_EXP[i]
            xp -= needed
            if xp < 0:
                return int(lvl)
            else:
                lvl += 1
        return 'N/A'

    def gameconverter(self, game):
        """ Convert a Hypixel game to a readable format. """
        if game == "QUAKECRAFT":
            game = "Quake"
        elif game == "WALLS":
            game = 'Walls'
        elif game == 'PAINTBALL':
            game == 'paintball'
        elif game == 'SURVIVAL_GAMES':
            game = 'Blitz Survival Games'
        elif game == 'TNTGAMES':
            game = 'TNT Games'
        elif game == 'VAMPIREZ':
            game = 'VampireZ'
        elif game == 'WALLS3':
            game = 'Mega Walls'
        elif game == 'ARCADE':
            game = 'Arcade'
        elif game == 'ARENA':
            game = 'Arena'
        elif game == 'UHC':
            game = 'UHC Champions'
        elif game == 'MCGO':
            game = 'Cops and Crims'
        elif game == 'BATTLEGROUND':
            game = 'Warlords'
        elif game == 'SUPER_SMASH':
            game = 'Smash Heroes'
        elif game == 'GINGERBREAD':
            game = 'Turbo Kart Racers'
        elif game == 'HOUSING':
            game = 'Housing'
        elif game == 'SKYWARS':
            game = 'Skywars'
        elif game == 'TRUE_COMBAT':
            game = 'Crazy Walls'
        elif game == 'SPEED_UHC':
            game = 'Speed UHC'
        elif game == 'SKYCLASH':
            game = 'SkyClash'
        elif game == 'LEGACY':
            game = 'Classic Games'
        elif game == 'PROTOTYPE':
            game = 'Prototype'
        elif game == 'BEDWARS':
            game = 'BedWars'
        elif game == 'MURDER_MYSTERY':
            game = 'Murder Mystery'
        elif game == 'BUILD_BATTLE':
            game = 'Build Battle'
        elif game == 'DUELS':
            game = 'Duels'
        elif game == 'SKYBLOCK':
            game = 'Skyblock'
        elif game == 'PIT':
            game = 'The Pit'
        else:
            game = 'N/A'
        return game

    def timeconverter(self, login, logout):
        """ Converts Hypixel login/out time to the appropriate format. """
        try:
            if login > logout:
                status = 'Online'
            elif login < logout:
                time = datetime.fromtimestamp(logout/1000.0)
                date = time.strftime("%m/%d/%Y")
                status = 'Offline - Last seen on ' + str(date)
                return status
            else:
                return 'N/A'
        except Exception as e:
            return 'N/A'

    def networklevel(self, exp):
        """ Gets a user's Network level from their network xp. """
        try:
            network_level = (((2 * exp) + 30625)**(1/2) / 50) - 2.5
            level = round(network_level, 0)
            return int(level)
        except:
            return 'N/A'

class hypixel:
    """ Class for interacting with Hypixel's API """
    def __init__(self):
        self.session = ClientSession() # Define aiohttp session. 

    async def player(self, uuid):
        """ Get Hypixel player data. """
        async with self.session.get('https://api.hypixel.net/player?key=' + API_KEY + '&uuid=' + uuid) as response:
            return await response.json()

    async def counts(self):
        """ Get Hypixel server counts. """
        async with self.session.get('https://api.hypixel.net/gameCounts?key=' + API_KEY ) as response:
            return await response.json()

    async def leaderboards(self):
        """ Get Hypixel leaderboards. """
        async with self.session.get('https://api.hypixel.net/leaderboards?key=' + API_KEY) as response:
            return await response.json()

    async def key(self):
        """ Get info on your Hypixel API key. """
        async with self.session.get('https://api.hypixel.net/key?key=' + API_KEY) as response:
            return await response.json()

    async def watchdog(self):
        """ Get Hypixel Watchdog stats. """
        async with self.session.get('https://api.hypixel.net/watchdogstats?key=' + API_KEY) as response:
            return await response.json()

    async def guild(self, name):
        """ Find a guild by name and return guild data. """
        async with self.session.get('https://api.hypixel.net/findGuild?key=' + API_KEY + '&byName=' + name) as response:
            data = await response.json()
            gid = data['guild']
        if gid is None:
            raise ValueError
        async with ClientSession() as session:
            async with session.get('https://api.hypixel.net/guild?key=' + API_KEY + '&id=' + gid) as response:
                return await response.json()

    async def getname(self, uuid):
        """ Get a player's name using Mojang API. """
        async with self.session.get("https://sessionserver.mojang.com/session/minecraft/profile/" + uuid) as response:
            return await response.json()

    async def playerguild(self, uuid):
        """ Get the name of the guild a player is in. """
        async with self.session.get('https://api.hypixel.net/guild?key=' + API_KEY + '&player=' + uuid) as response:
            data = await response.json()
            if data['guild'] is None:
                return 'None'
            return data['guild']['name']

    class skyblock:
        """ Class for interacting with Hypixel's Skyblock API. """
        def __init__(self):
            self.session = ClientSession()

        async def profile(self, profile):
            async with self.session.get('https://api.hypixel.net/skyblock/profile?key=' + API_KEY + '&profile=' + profile) as response:
                return await response.json()
        
        async def auctions(self, profile):
            async with self.session.get('https://api.hypixel.net/skyblock/auction?key=' + API_KEY + '&profile=' + profile) as response:
                return await response.json()

utils = utils()
hypixel = hypixel()
hypixel.skyblock = hypixel.skyblock()