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
                return lvl
            else:
                lvl += 1
        return 'N/A'

    def gameconverter(self, game):
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
        try:
            if login > logout:
                status = 'Online'
            elif login < logout:
                time = datetime.fromtimestamp(logout/1000.0)
                date = time.strftime("%m/%d/%Y")
                minute = time.strftime("%M")
                if int(time.strftime('%H')) == 12:
                    ampm = 'PM'
                    hour = time.strftime('%H')
                elif int(time.strftime('%H')) > 12:
                    hour = int(time.strftime('%H')) - 12
                    ampm = 'PM'
                elif int(time.strftime('%H')) < 12:
                    ampm = 'AM'
                    hour = time.strftime('%H')
                else: # should never happen
                    hour = None
                    ampm = None

                date_time = time.strftime("%m/%d/%Y at %H:%M")
                status = 'Offline - Last seen on ' + str(date) + ' at ' + str(hour) + ':' + str(minute) + ' ' + ampm + ', EST'
            else:
                status = 'N/A'
        except Exception as e:
            status = 'N/A'

    def networklevel(self, exp):
        try:
            network_level = (((2 * exp) + 30625)**(1/2) / 50) - 2.5
            level = round(network_level, 0)
            level = int(level)
        except:
            level = 'N/A'

class hypixel:
    def __init__(self):
        self.session = ClientSession()

    async def player(self, uuid):
        async with self.session.get('https://api.hypixel.net/player?key=' + API_KEY + '&uuid=' + uuid) as response:
            return await response.json()

    async def counts(self):
        async with self.session.get('https://api.hypixel.net/gameCounts?key=' + API_KEY ) as response:
            return await response.json()

    async def leaderboards(self):
        async with self.session.get('https://api.hypixel.net/leaderboards?key=' + API_KEY) as response:
            return await response.json()

    async def key(self):
        async with self.session.get('https://api.hypixel.net/key?key=' + API_KEY) as response:
            return await response.json()

    async def watchdog(self):
        async with self.session.get('https://api.hypixel.net/watchdogstats?key=' + API_KEY) as response:
            return await response.json()

    async def guild(self, name):
        async with self.session.get('https://api.hypixel.net/findGuild?key=' + API_KEY + '&byName=' + name) as response:
            data = await response.json()
            gid = data['guild']
        if gid is None:
            raise ValueError
        async with ClientSession() as session:
            async with session.get('https://api.hypixel.net/guild?key=' + API_KEY + '&id=' + gid) as response:
                return await response.json()

utils = utils()
hypixel = hypixel()