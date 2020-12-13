import discord
import DiscordUtils
import random
from utils.utils import *

other = """

For a more detailed list of commands, [click here](https://github.com/plun1331/HypixelBot/blob/main/COMMANDS.md).
If you require more assistance, [join the support server](https://discord.gg/gxB8mRC)."""

botinfo = """`h!help` - Returns a list of commands.
`h!info` - Returns some information and stats about the bot.
`h!ping` - Returns the bot's latency.
`h!invite` - Returns the bot's invite link."""

playerstats = """`h!player <player>` - Returns some general stats for the specified player.
`h!bedwars <player>` - Returns the specified player's Bedwars statistics.
`h!skywars <player>` - Returns the specified player's Skywars statistics.
`h!pit <player>` - Returns the specified player's Pit statistics.
`h!murdermystery <player>` - Returns the specified player's Murder Mystery statistics.
`h!buildbattle <player>` - Returns the specified player's Build Battle statistics.
`h!uhc <player>` - Returns the specified player's UHC Champions statistics.
`h!tntgames <player>` - Returns the specified player's TNT Games statistics."""

hypixelstats = """`h!leaderboard <game> <type>` - Returns the leaders on the specified leaderboard.
`h!guild <guild name>` - Returns information on the specified guild.
`h!playercount` - Returns Hypixel player counts.
`h!watchdog` - Returns Hypixel Watchdog statistics.
`h!boosters [game]` - Returns a list of boosters for the specified game, or the amount of boosters currently active if no game is specified.
`h!booster <id>` - Returns a info on the specified booster."""

minecraft = """`h!skin <player>` - Returns the player's skin"""

class Embeds:
    class Bedwars:
        async def main(self, name, color, data):
            try:
                level = str(utils.comma(int(data['player']['achievements']['bedwars_level']))) + ' ⭐'
            except:
                level = 'N/A'
            try:
                games_played = data['player']['stats']['Bedwars']['games_played_bedwars']
            except:
                games_played = 'N/A'
            try:
                exp = data['player']['stats']['Bedwars']['Experience']
            except:
                exp = 'N/A'
            try:
                final_deaths = data['player']['stats']['Bedwars']['final_deaths_bedwars']
            except:
                final_deaths = 'N/A'
            try:
                normal_deaths = data['player']['stats']['Bedwars']['deaths_bedwars']
            except:
                normal_deaths = 'N/A'
            try:
                total_deaths = final_deaths+normal_deaths
                if total_deaths == 'N/AN/A':
                    raise ValueError
            except:
                total_deaths = 'N/A'
            try:
                beds_lost = data['player']['stats']['Bedwars']['beds_lost_bedwars']
            except:
                beds_lost = 'N/A'
            try:
                beds_broken = data['player']['stats']['Bedwars']['beds_broken_bedwars']
            except:
                beds_broken = 'N/A'
            try:
                normal_kills = data['player']['stats']['Bedwars']['kills_bedwars']
            except:
                normal_kills = 'N/A'
            try:
                final_kills = data['player']['stats']['Bedwars']['final_kills_bedwars']
            except:
                final_kills = 'N/A'
            try:
                total_kills = final_kills+normal_kills
                if total_kills == 'N/AN/A':
                    raise ValueError
            except:
                total_kills = 'N/A'
            try:
                wins = data['player']['stats']['Bedwars']['wins_bedwars']
            except:
                wins = 'N/A'
            try:
                losses = data['player']['stats']['Bedwars']['losses_bedwars']
            except:
                losses = 'N/A'
            try:
                winstreak = data['player']['stats']['Bedwars']['winstreak']
            except:
                winstreak = 'N/A'
            embed = discord.Embed(title=name + "'s Bedwars Stats - Overall", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            embed.add_field(name="Bedwars Level", value=str(level), inline=True)
            try:
                embed.add_field(name="Bedwars Experience", value=str(utils.comma(round(exp, 0))), inline=True)
            except:
                embed.add_field(name="Bedwars Experience", value=str('N/A'), inline=True)
            embed.add_field(name="Games Played", value=str(utils.comma(games_played)), inline=True)
            embed.add_field(name="Normal Deaths", value=str(utils.comma(normal_deaths)), inline=True)
            embed.add_field(name="Final Deaths", value=str(utils.comma(final_deaths)), inline=True)
            embed.add_field(name="Total Deaths", value=str(utils.comma(total_deaths)), inline=True)
            embed.add_field(name="Normal Kills", value=str(utils.comma(normal_kills)), inline=True)
            embed.add_field(name="Final Kills", value=str(utils.comma(final_kills)), inline=True)
            embed.add_field(name="Total Kills", value=str(utils.comma(total_kills)), inline=True)
            try:
                embed.add_field(name="Normal K/D Ratio", value=str(utils.comma(round(normal_kills/normal_deaths, 2))), inline=True)
            except:
                embed.add_field(name="Normal K/D Ratio", value=str('N/A'), inline=True)
            try:
                embed.add_field(name="Final K/D Ratio", value=str(utils.comma(round(final_kills/final_deaths, 2))), inline=True)
            except:
                embed.add_field(name="Final K/D Ratio", value=str('N/A'), inline=True)
            try:
                embed.add_field(name="K/D Ratio", value=str(utils.comma(round(total_kills/total_deaths, 2))), inline=True)
            except:
                embed.add_field(name="K/D Ratio", value=str('N/A'), inline=True)
            embed.add_field(name="Wins", value=str(utils.comma(wins)), inline=True)
            embed.add_field(name="Losses", value=str(utils.comma(losses)), inline=True)
            try:
                embed.add_field(name="W/L Ratio", value=str(utils.comma(round(wins/losses, 2))), inline=True)
            except:
                embed.add_field(name="W/L Ratio", value=str('N/A'), inline=True)
            embed.add_field(name="Beds Lost", value=str(utils.comma(beds_lost)), inline=True)
            embed.add_field(name="Beds Broken", value=str(utils.comma(beds_broken)), inline=True)
            embed.add_field(name="Winstreak", value=str(utils.comma(winstreak)), inline=True)
            embed.set_footer(text='Unofficial Hypixel Discord Bot - Page 1/6')
            return embed
        
        async def solo(self, name, color, data):
            try:
                level = str(utils.comma(int(data['player']['achievements']['bedwars_level']))) + ' ⭐'
            except:
                level = 'N/A'
            try:
                games_played = data['player']['stats']['Bedwars']['eight_one_games_played_bedwars']
            except:
                games_played = 'N/A'
            try:
                exp = data['player']['stats']['Bedwars']['Experience']
            except:
                exp = 'N/A'
            try:
                final_deaths = data['player']['stats']['Bedwars']['eight_one_final_deaths_bedwars']
            except:
                final_deaths = 'N/A'
            try:
                normal_deaths = data['player']['stats']['Bedwars']['eight_one_deaths_bedwars']
            except:
                normal_deaths = 'N/A'
            try:
                total_deaths = final_deaths+normal_deaths
                if total_deaths == 'N/AN/A':
                    raise ValueError
            except:
                total_deaths = 'N/A'
            try:
                beds_lost = data['player']['stats']['Bedwars']['eight_one_beds_lost_bedwars']
            except:
                beds_lost = 'N/A'
            try:
                beds_broken = data['player']['stats']['Bedwars']['eight_one_beds_broken_bedwars']
            except:
                beds_broken = 'N/A'
            try:
                normal_kills = data['player']['stats']['Bedwars']['eight_one_kills_bedwars']
            except:
                normal_kills = 'N/A'
            try:
                final_kills = data['player']['stats']['Bedwars']['eight_one_final_kills_bedwars']
            except:
                final_kills = 'N/A'
            try:
                total_kills = final_kills+normal_kills
                if total_kills == 'N/AN/A':
                    raise ValueError
            except:
                total_kills = 'N/A'
            try:
                wins = data['player']['stats']['Bedwars']['eight_one_wins_bedwars']
            except:
                wins = 'N/A'
            try:
                losses = data['player']['stats']['Bedwars']['eight_one_losses_bedwars']
            except:
                losses = 'N/A'
            try:
                winstreak = data['player']['stats']['Bedwars']['eight_one_winstreak']
            except:
                winstreak = 'N/A'
            embed = discord.Embed(title=name + "'s Bedwars Stats - Solo", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            embed.add_field(name="Bedwars Level", value=str(level), inline=True)
            try:
                embed.add_field(name="Bedwars Experience", value=str(utils.comma(round(exp, 0))), inline=True)
            except:
                embed.add_field(name="Bedwars Experience", value=str('N/A'), inline=True)
            embed.add_field(name="Games Played", value=str(utils.comma(games_played)), inline=True)
            embed.add_field(name="Normal Deaths", value=str(utils.comma(normal_deaths)), inline=True)
            embed.add_field(name="Final Deaths", value=str(utils.comma(final_deaths)), inline=True)
            embed.add_field(name="Total Deaths", value=str(utils.comma(total_deaths)), inline=True)
            embed.add_field(name="Normal Kills", value=str(utils.comma(normal_kills)), inline=True)
            embed.add_field(name="Final Kills", value=str(utils.comma(final_kills)), inline=True)
            embed.add_field(name="Total Kills", value=str(utils.comma(total_kills)), inline=True)
            try:
                embed.add_field(name="Normal K/D Ratio", value=str(utils.comma(round(normal_kills/normal_deaths, 2))), inline=True)
            except:
                embed.add_field(name="Normal K/D Ratio", value=str('N/A'), inline=True)
            try:
                embed.add_field(name="Final K/D Ratio", value=str(utils.comma(round(final_kills/final_deaths, 2))), inline=True)
            except:
                embed.add_field(name="Final K/D Ratio", value=str('N/A'), inline=True)
            try:
                embed.add_field(name="K/D Ratio", value=str(utils.comma(round(total_kills/total_deaths, 2))), inline=True)
            except:
                embed.add_field(name="K/D Ratio", value=str('N/A'), inline=True)
            embed.add_field(name="Wins", value=str(utils.comma(wins)), inline=True)
            embed.add_field(name="Losses", value=str(utils.comma(losses)), inline=True)
            try:
                embed.add_field(name="W/L Ratio", value=str(utils.comma(round(wins/losses, 2))), inline=True)
            except:
                embed.add_field(name="W/L Ratio", value=str('N/A'), inline=True)
            embed.add_field(name="Beds Lost", value=str(utils.comma(beds_lost)), inline=True)
            embed.add_field(name="Beds Broken", value=str(utils.comma(beds_broken)), inline=True)
            embed.add_field(name="Winstreak", value=str(utils.comma(winstreak)), inline=True)
            embed.set_footer(text='Unofficial Hypixel Discord Bot - Page 2/7')
            return embed

        async def doubles(self, name, color, data):
            try:
                level = str(utils.comma(int(data['player']['achievements']['bedwars_level']))) + ' ⭐'
            except:
                level = 'N/A'
            try:
                games_played = data['player']['stats']['Bedwars']['eight_two_games_played_bedwars']
            except:
                games_played = 'N/A'
            try:
                exp = data['player']['stats']['Bedwars']['Experience']
            except:
                exp = 'N/A'
            try:
                final_deaths = data['player']['stats']['Bedwars']['eight_two_final_deaths_bedwars']
            except:
                final_deaths = 'N/A'
            try:
                normal_deaths = data['player']['stats']['Bedwars']['eight_two_deaths_bedwars']
            except:
                normal_deaths = 'N/A'
            try:
                total_deaths = final_deaths+normal_deaths
                if total_deaths == 'N/AN/A':
                    raise ValueError
            except:
                total_deaths = 'N/A'
            try:
                beds_lost = data['player']['stats']['Bedwars']['eight_two_beds_lost_bedwars']
            except:
                beds_lost = 'N/A'
            try:
                beds_broken = data['player']['stats']['Bedwars']['eight_two_beds_broken_bedwars']
            except:
                beds_broken = 'N/A'
            try:
                normal_kills = data['player']['stats']['Bedwars']['eight_two_kills_bedwars']
            except:
                normal_kills = 'N/A'
            try:
                final_kills = data['player']['stats']['Bedwars']['eight_two_final_kills_bedwars']
            except:
                final_kills = 'N/A'
            try:
                total_kills = final_kills+normal_kills
                if total_kills == 'N/AN/A':
                    raise ValueError
            except:
                total_kills = 'N/A'
            try:
                wins = data['player']['stats']['Bedwars']['eight_two_wins_bedwars']
            except:
                wins = 'N/A'
            try:
                losses = data['player']['stats']['Bedwars']['eight_two_losses_bedwars']
            except:
                losses = 'N/A'
            try:
                winstreak = data['player']['stats']['Bedwars']['eight_two_winstreak']
            except:
                winstreak = 'N/A'
            embed = discord.Embed(title=name + "'s Bedwars Stats - Doubles", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            embed.add_field(name="Bedwars Level", value=str(level), inline=True)
            try:
                embed.add_field(name="Bedwars Experience", value=str(utils.comma(round(exp, 0))), inline=True)
            except:
                embed.add_field(name="Bedwars Experience", value=str('N/A'), inline=True)
            embed.add_field(name="Games Played", value=str(utils.comma(games_played)), inline=True)
            embed.add_field(name="Normal Deaths", value=str(utils.comma(normal_deaths)), inline=True)
            embed.add_field(name="Final Deaths", value=str(utils.comma(final_deaths)), inline=True)
            embed.add_field(name="Total Deaths", value=str(utils.comma(total_deaths)), inline=True)
            embed.add_field(name="Normal Kills", value=str(utils.comma(normal_kills)), inline=True)
            embed.add_field(name="Final Kills", value=str(utils.comma(final_kills)), inline=True)
            embed.add_field(name="Total Kills", value=str(utils.comma(total_kills)), inline=True)
            try:
                embed.add_field(name="Normal K/D Ratio", value=str(utils.comma(round(normal_kills/normal_deaths, 2))), inline=True)
            except:
                embed.add_field(name="Normal K/D Ratio", value=str('N/A'), inline=True)
            try:
                embed.add_field(name="Final K/D Ratio", value=str(utils.comma(round(final_kills/final_deaths, 2))), inline=True)
            except:
                embed.add_field(name="Final K/D Ratio", value=str('N/A'), inline=True)
            try:
                embed.add_field(name="K/D Ratio", value=str(utils.comma(round(total_kills/total_deaths, 2))), inline=True)
            except:
                embed.add_field(name="K/D Ratio", value=str('N/A'), inline=True)
            embed.add_field(name="Wins", value=str(utils.comma(wins)), inline=True)
            embed.add_field(name="Losses", value=str(utils.comma(losses)), inline=True)
            try:
                embed.add_field(name="W/L Ratio", value=str(utils.comma(round(wins/losses, 2))), inline=True)
            except:
                embed.add_field(name="W/L Ratio", value=str('N/A'), inline=True)
            embed.add_field(name="Beds Lost", value=str(utils.comma(beds_lost)), inline=True)
            embed.add_field(name="Beds Broken", value=str(utils.comma(beds_broken)), inline=True)
            embed.add_field(name="Winstreak", value=str(utils.comma(winstreak)), inline=True)
            embed.set_footer(text='Unofficial Hypixel Discord Bot - Page 3/6')
            return embed

        async def threes(self, name, color, data):
            try:
                level = str(utils.comma(int(data['player']['achievements']['bedwars_level']))) + ' ⭐'
            except:
                level = 'N/A'
            try:
                games_played = data['player']['stats']['Bedwars']['four_three_games_played_bedwars']
            except:
                games_played = 'N/A'
            try:
                exp = data['player']['stats']['Bedwars']['Experience']
            except:
                exp = 'N/A'
            try:
                final_deaths = data['player']['stats']['Bedwars']['four_three_final_deaths_bedwars']
            except:
                final_deaths = 'N/A'
            try:
                normal_deaths = data['player']['stats']['Bedwars']['four_three_deaths_bedwars']
            except:
                normal_deaths = 'N/A'
            try:
                total_deaths = final_deaths+normal_deaths
                if total_deaths == 'N/AN/A':
                    raise ValueError
            except:
                total_deaths = 'N/A'
            try:
                beds_lost = data['player']['stats']['Bedwars']['four_three_beds_lost_bedwars']
            except:
                beds_lost = 'N/A'
            try:
                beds_broken = data['player']['stats']['Bedwars']['four_three_beds_broken_bedwars']
            except:
                beds_broken = 'N/A'
            try:
                normal_kills = data['player']['stats']['Bedwars']['four_three_kills_bedwars']
            except:
                normal_kills = 'N/A'
            try:
                final_kills = data['player']['stats']['Bedwars']['four_three_final_kills_bedwars']
            except:
                final_kills = 'N/A'
            try:
                total_kills = final_kills+normal_kills
                if total_kills == 'N/AN/A':
                    raise ValueError
            except:
                total_kills = 'N/A'
            try:
                wins = data['player']['stats']['Bedwars']['four_three_wins_bedwars']
            except:
                wins = 'N/A'
            try:
                losses = data['player']['stats']['Bedwars']['four_three_losses_bedwars']
            except:
                losses = 'N/A'
            try:
                winstreak = data['player']['stats']['Bedwars']['four_three_winstreak']
            except:
                winstreak = 'N/A'
            embed = discord.Embed(title=name + "'s Bedwars Stats - 3v3v3v3", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            embed.add_field(name="Bedwars Level", value=str(level), inline=True)
            try:
                embed.add_field(name="Bedwars Experience", value=str(utils.comma(round(exp, 0))), inline=True)
            except:
                embed.add_field(name="Bedwars Experience", value=str('N/A'), inline=True)
            embed.add_field(name="Games Played", value=str(utils.comma(games_played)), inline=True)
            embed.add_field(name="Normal Deaths", value=str(utils.comma(normal_deaths)), inline=True)
            embed.add_field(name="Final Deaths", value=str(utils.comma(final_deaths)), inline=True)
            embed.add_field(name="Total Deaths", value=str(utils.comma(total_deaths)), inline=True)
            embed.add_field(name="Normal Kills", value=str(utils.comma(normal_kills)), inline=True)
            embed.add_field(name="Final Kills", value=str(utils.comma(final_kills)), inline=True)
            embed.add_field(name="Total Kills", value=str(utils.comma(total_kills)), inline=True)
            try:
                embed.add_field(name="Normal K/D Ratio", value=str(utils.comma(round(normal_kills/normal_deaths, 2))), inline=True)
            except:
                embed.add_field(name="Normal K/D Ratio", value=str('N/A'), inline=True)
            try:
                embed.add_field(name="Final K/D Ratio", value=str(utils.comma(round(final_kills/final_deaths, 2))), inline=True)
            except:
                embed.add_field(name="Final K/D Ratio", value=str('N/A'), inline=True)
            try:
                embed.add_field(name="K/D Ratio", value=str(utils.comma(round(total_kills/total_deaths, 2))), inline=True)
            except:
                embed.add_field(name="K/D Ratio", value=str('N/A'), inline=True)
            embed.add_field(name="Wins", value=str(utils.comma(wins)), inline=True)
            embed.add_field(name="Losses", value=str(utils.comma(losses)), inline=True)
            try:
                embed.add_field(name="W/L Ratio", value=str(utils.comma(round(wins/losses, 2))), inline=True)
            except:
                embed.add_field(name="W/L Ratio", value=str('N/A'), inline=True)
            embed.add_field(name="Beds Lost", value=str(utils.comma(beds_lost)), inline=True)
            embed.add_field(name="Beds Broken", value=str(utils.comma(beds_broken)), inline=True)
            embed.add_field(name="Winstreak", value=str(utils.comma(winstreak)), inline=True)
            embed.set_footer(text='Unofficial Hypixel Discord Bot - Page 4/6')
            return embed

        async def fours(self, name, color, data):
            try:
                level = str(utils.comma(int(data['player']['achievements']['bedwars_level']))) + ' ⭐'
            except:
                level = 'N/A'
            try:
                games_played = data['player']['stats']['Bedwars']['four_four_games_played_bedwars']
            except:
                games_played = 'N/A'
            try:
                exp = data['player']['stats']['Bedwars']['Experience']
            except:
                exp = 'N/A'
            try:
                final_deaths = data['player']['stats']['Bedwars']['four_four_final_deaths_bedwars']
            except:
                final_deaths = 'N/A'
            try:
                normal_deaths = data['player']['stats']['Bedwars']['four_four_deaths_bedwars']
            except:
                normal_deaths = 'N/A'
            try:
                total_deaths = final_deaths+normal_deaths
                if total_deaths == 'N/AN/A':
                    raise ValueError
            except:
                total_deaths = 'N/A'
            try:
                beds_lost = data['player']['stats']['Bedwars']['four_four_beds_lost_bedwars']
            except:
                beds_lost = 'N/A'
            try:
                beds_broken = data['player']['stats']['Bedwars']['four_four_beds_broken_bedwars']
            except:
                beds_broken = 'N/A'
            try:
                normal_kills = data['player']['stats']['Bedwars']['four_four_kills_bedwars']
            except:
                normal_kills = 'N/A'
            try:
                final_kills = data['player']['stats']['Bedwars']['four_four_final_kills_bedwars']
            except:
                final_kills = 'N/A'
            try:
                total_kills = final_kills+normal_kills
                if total_kills == 'N/AN/A':
                    raise ValueError
            except:
                total_kills = 'N/A'
            try:
                wins = data['player']['stats']['Bedwars']['four_four_wins_bedwars']
            except:
                wins = 'N/A'
            try:
                losses = data['player']['stats']['Bedwars']['four_four_losses_bedwars']
            except:
                losses = 'N/A'
            try:
                winstreak = data['player']['stats']['Bedwars']['four_four_winstreak']
            except:
                winstreak = 'N/A'
            embed = discord.Embed(title=name + "'s Bedwars Stats - 4v4v4v4", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            embed.add_field(name="Bedwars Level", value=str(level), inline=True)
            try:
                embed.add_field(name="Bedwars Experience", value=str(utils.comma(round(exp, 0))), inline=True)
            except:
                embed.add_field(name="Bedwars Experience", value=str('N/A'), inline=True)
            embed.add_field(name="Games Played", value=str(utils.comma(games_played)), inline=True)
            embed.add_field(name="Normal Deaths", value=str(utils.comma(normal_deaths)), inline=True)
            embed.add_field(name="Final Deaths", value=str(utils.comma(final_deaths)), inline=True)
            embed.add_field(name="Total Deaths", value=str(utils.comma(total_deaths)), inline=True)
            embed.add_field(name="Normal Kills", value=str(utils.comma(normal_kills)), inline=True)
            embed.add_field(name="Final Kills", value=str(utils.comma(final_kills)), inline=True)
            embed.add_field(name="Total Kills", value=str(utils.comma(total_kills)), inline=True)
            try:
                embed.add_field(name="Normal K/D Ratio", value=str(utils.comma(round(normal_kills/normal_deaths, 2))), inline=True)
            except:
                embed.add_field(name="Normal K/D Ratio", value=str('N/A'), inline=True)
            try:
                embed.add_field(name="Final K/D Ratio", value=str(utils.comma(round(final_kills/final_deaths, 2))), inline=True)
            except:
                embed.add_field(name="Final K/D Ratio", value=str('N/A'), inline=True)
            try:
                embed.add_field(name="K/D Ratio", value=str(utils.comma(round(total_kills/total_deaths, 2))), inline=True)
            except:
                embed.add_field(name="K/D Ratio", value=str('N/A'), inline=True)
            embed.add_field(name="Wins", value=str(utils.comma(wins)), inline=True)
            embed.add_field(name="Losses", value=str(utils.comma(losses)), inline=True)
            try:
                embed.add_field(name="W/L Ratio", value=str(utils.comma(round(wins/losses, 2))), inline=True)
            except:
                embed.add_field(name="W/L Ratio", value=str('N/A'), inline=True)
            embed.add_field(name="Beds Lost", value=str(utils.comma(beds_lost)), inline=True)
            embed.add_field(name="Beds Broken", value=str(utils.comma(beds_broken)), inline=True)
            embed.add_field(name="Winstreak", value=str(utils.comma(winstreak)), inline=True)
            embed.set_footer(text='Unofficial Hypixel Discord Bot - Page 5/6')
            return embed

        async def fourfour(self, name, color, data):
            try:
                level = str(utils.comma(int(data['player']['achievements']['bedwars_level']))) + ' ⭐'
            except:
                level = 'N/A'
            try:
                games_played = data['player']['stats']['Bedwars']['two_four_games_played_bedwars']
            except:
                games_played = 'N/A'
            try:
                exp = data['player']['stats']['Bedwars']['Experience']
            except:
                exp = 'N/A'
            try:
                final_deaths = data['player']['stats']['Bedwars']['two_four_final_deaths_bedwars']
            except:
                final_deaths = 'N/A'
            try:
                normal_deaths = data['player']['stats']['Bedwars']['two_four_deaths_bedwars']
            except:
                normal_deaths = 'N/A'
            try:
                total_deaths = final_deaths+normal_deaths
                if total_deaths == 'N/AN/A':
                    raise ValueError
            except:
                total_deaths = 'N/A'
            try:
                beds_lost = data['player']['stats']['Bedwars']['two_four_beds_lost_bedwars']
            except:
                beds_lost = 'N/A'
            try:
                beds_broken = data['player']['stats']['Bedwars']['two_four_beds_broken_bedwars']
            except:
                beds_broken = 'N/A'
            try:
                normal_kills = data['player']['stats']['Bedwars']['two_four_kills_bedwars']
            except:
                normal_kills = 'N/A'
            try:
                final_kills = data['player']['stats']['Bedwars']['two_four_final_kills_bedwars']
            except:
                final_kills = 'N/A'
            try:
                total_kills = final_kills+normal_kills
                if total_kills == 'N/AN/A':
                    raise ValueError
            except:
                total_kills = 'N/A'
            try:
                wins = data['player']['stats']['Bedwars']['two_four_wins_bedwars']
            except:
                wins = 'N/A'
            try:
                losses = data['player']['stats']['Bedwars']['two_four_losses_bedwars']
            except:
                losses = 'N/A'
            try:
                winstreak = data['player']['stats']['Bedwars']['two_four_winstreak']
            except:
                winstreak = 'N/A'
            embed = discord.Embed(title=name + "'s Bedwars Stats - 4v4", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            embed.add_field(name="Bedwars Level", value=str(level), inline=True)
            try:
                embed.add_field(name="Bedwars Experience", value=str(utils.comma(round(exp, 0))), inline=True)
            except:
                embed.add_field(name="Bedwars Experience", value=str('N/A'), inline=True)
            embed.add_field(name="Games Played", value=str(utils.comma(games_played)), inline=True)
            embed.add_field(name="Normal Deaths", value=str(utils.comma(normal_deaths)), inline=True)
            embed.add_field(name="Final Deaths", value=str(utils.comma(final_deaths)), inline=True)
            embed.add_field(name="Total Deaths", value=str(utils.comma(total_deaths)), inline=True)
            embed.add_field(name="Normal Kills", value=str(utils.comma(normal_kills)), inline=True)
            embed.add_field(name="Final Kills", value=str(utils.comma(final_kills)), inline=True)
            embed.add_field(name="Total Kills", value=str(utils.comma(total_kills)), inline=True)
            try:
                embed.add_field(name="Normal K/D Ratio", value=str(utils.comma(round(normal_kills/normal_deaths, 2))), inline=True)
            except:
                embed.add_field(name="Normal K/D Ratio", value=str('N/A'), inline=True)
            try:
                embed.add_field(name="Final K/D Ratio", value=str(utils.comma(round(final_kills/final_deaths, 2))), inline=True)
            except:
                embed.add_field(name="Final K/D Ratio", value=str('N/A'), inline=True)
            try:
                embed.add_field(name="K/D Ratio", value=str(utils.comma(round(total_kills/total_deaths, 2))), inline=True)
            except:
                embed.add_field(name="K/D Ratio", value=str('N/A'), inline=True)
            embed.add_field(name="Wins", value=str(utils.comma(wins)), inline=True)
            embed.add_field(name="Losses", value=str(utils.comma(losses)), inline=True)
            try:
                embed.add_field(name="W/L Ratio", value=str(utils.comma(round(wins/losses, 2))), inline=True)
            except:
                embed.add_field(name="W/L Ratio", value=str('N/A'), inline=True)
            embed.add_field(name="Beds Lost", value=str(utils.comma(beds_lost)), inline=True)
            embed.add_field(name="Beds Broken", value=str(utils.comma(beds_broken)), inline=True)
            embed.add_field(name="Winstreak", value=str(utils.comma(winstreak)), inline=True)
            embed.set_footer(text='Unofficial Hypixel Discord Bot - Page 6/6')
            return embed

        async def generate(self, ctx, name, data, perms): 
            color=random.randint(1, 16777215)
            main = await self.main(name, color, data)
            solo = await self.solo(name, color, data)
            doubles = await self.doubles(name, color, data)
            threes = await self.threes(name, color, data)
            fours = await self.fours(name, color, data)
            fourfour = await self.fourfour(name, color, data)
            paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, timeout=60, remove_reactions=False)
            if perms is not None:
                if perms.manage_messages:
                    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, timeout=60, remove_reactions=True)
            paginator.add_reaction('⏮️', "first")
            paginator.add_reaction('⏪', "back")
            paginator.add_reaction('⏹', "lock")
            paginator.add_reaction('⏩', "next")
            paginator.add_reaction('⏭️', "last")
            embeds = [main, solo, doubles, threes, fours, fourfour]
            return embeds, paginator

    class Skywars:
        async def main(self, name, color, data):
            try:
                level = 'N/A'
                xp = data['player']['stats']['SkyWars']['skywars_experience']
                xps = [0, 20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000]
                if xp >= 15000:
                    level = (xp - 15000) / 10000. + 12
                else:
                    for i in range(len(xps)):
                        if xp < xps[i]:
                            level = str(utils.comma(int(round(int(1 + i + float(xp - xps[i-1]) / (xps[i] - xps[i-1], 0)))))) + ' ⭐'
            except:
                level = 'N/A'
            try:
                games_played = data['player']['stats']['SkyWars']['games_played_skywars']
            except:
                games_played = 'N/A'
            try:
                winstreak = data['player']['stats']['SkyWars']['win_streak']
            except:
                winstreak = 'N/A'
            try:
                kills = data['player']['stats']['SkyWars']['kills']
            except:
                kills = 'N/A'
            try:
                deaths = data['player']['stats']['SkyWars']['deaths']
            except:
                deaths = 'N/A'
            try:
                top_winstreak = data['player']['stats']['SkyWars']['highestWinstreak']
            except:
                top_winstreak = 'N/A'
            try:
                coins = int(data['player']['stats']['SkyWars']['coins'])
            except:
                coins = 'N/A'
            try:
                souls = data['player']['stats']['SkyWars']['souls']
            except:
                souls = 'N/A'
            try:
                wins = data['player']['stats']['SkyWars']['wins']
            except:
                wins = 'N/A'
            try:
                losses = data['player']['stats']['SkyWars']['losses']
            except:
                losses = 'N/A'
            embed = discord.Embed(title=name + "'s Skywars Stats - Overall", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            try:
                embed.add_field(name="Skywars Level", value=str(int(level))+' ⭐', inline=True)
            except:
                embed.add_field(name="Skywars Level", value='N/A', inline=True)
            embed.add_field(name="Skywars Coins", value=str(utils.comma(coins)), inline=True)
            embed.add_field(name="Skywars Souls", value=str(utils.comma(souls)), inline=True)
            embed.add_field(name="Skywars Games Played", value=str(utils.comma(round(games_played, 0))), inline=True)
            embed.add_field(name="Skywars Winstreak", value=str(utils.comma(winstreak)), inline=True)
            embed.add_field(name="Skywars Highest Winstreak", value=str(utils.comma(top_winstreak)), inline=True)
            embed.add_field(name="Kills", value=str(utils.comma(kills)), inline=True)
            embed.add_field(name="Deaths", value=str(utils.comma(deaths)), inline=True)
            try:
                embed.add_field(name="K/D Ratio", value=str(utils.comma(round(int(kills)/int(deaths), 2))), inline=True)
            except:
                embed.add_field(name="K/D Ratio", value='N/A', inline=True)
            embed.add_field(name="Wins", value=str(utils.comma(wins)), inline=True)
            embed.add_field(name="Losses", value=str(utils.comma(losses)), inline=True)
            try:
                embed.add_field(name="W/L Ratio", value=str(utils.comma(round(int(wins)/int(losses), 2))), inline=True)
            except:
                embed.add_field(name="W/L Ratio", value='N/A', inline=True)
            embed.set_footer(text='Unofficial Hypixel Discord Bot - Page 1/6')
            return embed

        async def solon(self, name, color, data):
            try:
                level = 'N/A'
                xp = data['player']['stats']['SkyWars']['skywars_experience']
                xps = [0, 20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000]
                if xp >= 15000:
                    level = (xp - 15000) / 10000. + 12
                else:
                    for i in range(len(xps)):
                        if xp < xps[i]:
                            level = str(utils.comma(int(round(int(1 + i + float(xp - xps[i-1]) / (xps[i] - xps[i-1], 0)))))) + ' ⭐'
            except:
                level = 'N/A'
            try:
                games_played = data['player']['stats']['SkyWars']['games_played_skywars']
            except:
                games_played = 'N/A'
            try:
                winstreak = data['player']['stats']['SkyWars']['win_streak']
            except:
                winstreak = 'N/A'
            try:
                kills = data['player']['stats']['SkyWars']['kills_solo_normal']
            except:
                kills = 'N/A'
            try:
                deaths = data['player']['stats']['SkyWars']['deaths_solo_normal']
            except:
                deaths = 'N/A'
            try:
                top_winstreak = data['player']['stats']['SkyWars']['highestWinstreak']
            except:
                top_winstreak = 'N/A'
            try:
                coins = int(data['player']['stats']['SkyWars']['coins'])
            except:
                coins = 'N/A'
            try:
                souls = data['player']['stats']['SkyWars']['souls']
            except:
                souls = 'N/A'
            try:
                wins = data['player']['stats']['SkyWars']['wins_solo_normal']
            except:
                wins = 'N/A'
            try:
                losses = data['player']['stats']['SkyWars']['losses_solo_normal']
            except:
                losses = 'N/A'
            embed = discord.Embed(title=name + "'s Skywars Stats - Solo Normal", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            try:
                embed.add_field(name="Skywars Level", value=str(int(level))+' ⭐', inline=True)
            except:
                embed.add_field(name="Skywars Level", value='N/A', inline=True)
            embed.add_field(name="Skywars Coins", value=str(utils.comma(coins)), inline=True)
            embed.add_field(name="Skywars Souls", value=str(utils.comma(souls)), inline=True)
            embed.add_field(name="Skywars Games Played", value=str(utils.comma(round(games_played, 0))), inline=True)
            embed.add_field(name="Skywars Winstreak", value=str(utils.comma(winstreak)), inline=True)
            embed.add_field(name="Skywars Highest Winstreak", value=str(utils.comma(top_winstreak)), inline=True)
            embed.add_field(name="Kills", value=str(utils.comma(kills)), inline=True)
            embed.add_field(name="Deaths", value=str(utils.comma(deaths)), inline=True)
            try:
                embed.add_field(name="K/D Ratio", value=str(utils.comma(round(int(kills)/int(deaths), 2))), inline=True)
            except:
                embed.add_field(name="K/D Ratio", value='N/A', inline=True)
            embed.add_field(name="Wins", value=str(utils.comma(wins)), inline=True)
            embed.add_field(name="Losses", value=str(utils.comma(losses)), inline=True)
            try:
                embed.add_field(name="W/L Ratio", value=str(utils.comma(round(int(wins)/int(losses), 2))), inline=True)
            except:
                embed.add_field(name="W/L Ratio", value='N/A', inline=True)
            embed.set_footer(text='Unofficial Hypixel Discord Bot - Page 2/6')
            return embed

        async def soloi(self, name, color, data):
            try:
                level = 'N/A'
                xp = data['player']['stats']['SkyWars']['skywars_experience']
                xps = [0, 20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000]
                if xp >= 15000:
                    level = (xp - 15000) / 10000. + 12
                else:
                    for i in range(len(xps)):
                        if xp < xps[i]:
                            level = str(utils.comma(int(round(int(1 + i + float(xp - xps[i-1]) / (xps[i] - xps[i-1], 0)))))) + ' ⭐'
            except:
                level = 'N/A'
            try:
                games_played = data['player']['stats']['SkyWars']['games_played_skywars']
            except:
                games_played = 'N/A'
            try:
                winstreak = data['player']['stats']['SkyWars']['win_streak']
            except:
                winstreak = 'N/A'
            try:
                kills = data['player']['stats']['SkyWars']['kills_solo_insane']
            except:
                kills = 'N/A'
            try:
                deaths = data['player']['stats']['SkyWars']['deaths_solo_insane']
            except:
                deaths = 'N/A'
            try:
                top_winstreak = data['player']['stats']['SkyWars']['highestWinstreak']
            except:
                top_winstreak = 'N/A'
            try:
                coins = int(data['player']['stats']['SkyWars']['coins'])
            except:
                coins = 'N/A'
            try:
                souls = data['player']['stats']['SkyWars']['souls']
            except:
                souls = 'N/A'
            try:
                wins = data['player']['stats']['SkyWars']['wins_solo_insane']
            except:
                wins = 'N/A'
            try:
                losses = data['player']['stats']['SkyWars']['losses_solo_insane']
            except:
                losses = 'N/A'
            embed = discord.Embed(title=name + "'s Skywars Stats - Solo Insane", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            try:
                embed.add_field(name="Skywars Level", value=str(int(level))+' ⭐', inline=True)
            except:
                embed.add_field(name="Skywars Level", value='N/A', inline=True)
            embed.add_field(name="Skywars Coins", value=str(utils.comma(coins)), inline=True)
            embed.add_field(name="Skywars Souls", value=str(utils.comma(souls)), inline=True)
            embed.add_field(name="Skywars Games Played", value=str(utils.comma(round(games_played, 0))), inline=True)
            embed.add_field(name="Skywars Winstreak", value=str(utils.comma(winstreak)), inline=True)
            embed.add_field(name="Skywars Highest Winstreak", value=str(utils.comma(top_winstreak)), inline=True)
            embed.add_field(name="Kills", value=str(utils.comma(kills)), inline=True)
            embed.add_field(name="Deaths", value=str(utils.comma(deaths)), inline=True)
            try:
                embed.add_field(name="K/D Ratio", value=str(utils.comma(round(int(kills)/int(deaths), 2))), inline=True)
            except:
                embed.add_field(name="K/D Ratio", value='N/A', inline=True)
            embed.add_field(name="Wins", value=str(utils.comma(wins)), inline=True)
            embed.add_field(name="Losses", value=str(utils.comma(losses)), inline=True)
            try:
                embed.add_field(name="W/L Ratio", value=str(utils.comma(round(int(wins)/int(losses), 2))), inline=True)
            except:
                embed.add_field(name="W/L Ratio", value='N/A', inline=True)
            embed.set_footer(text='Unofficial Hypixel Discord Bot - Page 3/6')
            return embed

        async def doublesn(self, name, color, data):
            try:
                level = 'N/A'
                xp = data['player']['stats']['SkyWars']['skywars_experience']
                xps = [0, 20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000]
                if xp >= 15000:
                    level = (xp - 15000) / 10000. + 12
                else:
                    for i in range(len(xps)):
                        if xp < xps[i]:
                            level = str(utils.comma(int(round(int(1 + i + float(xp - xps[i-1]) / (xps[i] - xps[i-1], 0)))))) + ' ⭐'
            except:
                level = 'N/A'
            try:
                games_played = data['player']['stats']['SkyWars']['games_played_skywars']
            except:
                games_played = 'N/A'
            try:
                winstreak = data['player']['stats']['SkyWars']['win_streak']
            except:
                winstreak = 'N/A'
            try:
                kills = data['player']['stats']['SkyWars']['kills_team_normal']
            except:
                kills = 'N/A'
            try:
                deaths = data['player']['stats']['SkyWars']['deaths_team_normal']
            except:
                deaths = 'N/A'
            try:
                top_winstreak = data['player']['stats']['SkyWars']['highestWinstreak']
            except:
                top_winstreak = 'N/A'
            try:
                coins = int(data['player']['stats']['SkyWars']['coins'])
            except:
                coins = 'N/A'
            try:
                souls = data['player']['stats']['SkyWars']['souls']
            except:
                souls = 'N/A'
            try:
                wins = data['player']['stats']['SkyWars']['wins_team_normal']
            except:
                wins = 'N/A'
            try:
                losses = data['player']['stats']['SkyWars']['losses_team_normal']
            except:
                losses = 'N/A'
            embed = discord.Embed(title=name + "'s Skywars Stats - Doubles Normal", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            try:
                embed.add_field(name="Skywars Level", value=str(int(level))+' ⭐', inline=True)
            except:
                embed.add_field(name="Skywars Level", value='N/A', inline=True)
            embed.add_field(name="Skywars Coins", value=str(utils.comma(coins)), inline=True)
            embed.add_field(name="Skywars Souls", value=str(utils.comma(souls)), inline=True)
            embed.add_field(name="Skywars Games Played", value=str(utils.comma(round(games_played, 0))), inline=True)
            embed.add_field(name="Skywars Winstreak", value=str(utils.comma(winstreak)), inline=True)
            embed.add_field(name="Skywars Highest Winstreak", value=str(utils.comma(top_winstreak)), inline=True)
            embed.add_field(name="Kills", value=str(utils.comma(kills)), inline=True)
            embed.add_field(name="Deaths", value=str(utils.comma(deaths)), inline=True)
            try:
                embed.add_field(name="K/D Ratio", value=str(utils.comma(round(int(kills)/int(deaths), 2))), inline=True)
            except:
                embed.add_field(name="K/D Ratio", value='N/A', inline=True)
            embed.add_field(name="Wins", value=str(utils.comma(wins)), inline=True)
            embed.add_field(name="Losses", value=str(utils.comma(losses)), inline=True)
            try:
                embed.add_field(name="W/L Ratio", value=str(utils.comma(round(int(wins)/int(losses), 2))), inline=True)
            except:
                embed.add_field(name="W/L Ratio", value='N/A', inline=True)
            embed.set_footer(text='Unofficial Hypixel Discord Bot - Page 4/6')
            return embed

        async def doublesi(self, name, color, data):
            try:
                level = 'N/A'
                xp = data['player']['stats']['SkyWars']['skywars_experience']
                xps = [0, 20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000]
                if xp >= 15000:
                    level = (xp - 15000) / 10000. + 12
                else:
                    for i in range(len(xps)):
                        if xp < xps[i]:
                            level = str(utils.comma(int(round(int(1 + i + float(xp - xps[i-1]) / (xps[i] - xps[i-1], 0)))))) + ' ⭐'
            except:
                level = 'N/A'
            try:
                games_played = data['player']['stats']['SkyWars']['games_played_skywars']
            except:
                games_played = 'N/A'
            try:
                winstreak = data['player']['stats']['SkyWars']['win_streak']
            except:
                winstreak = 'N/A'
            try:
                kills = data['player']['stats']['SkyWars']['kills_team_insane']
            except:
                kills = 'N/A'
            try:
                deaths = data['player']['stats']['SkyWars']['deaths_team_insane']
            except:
                deaths = 'N/A'
            try:
                top_winstreak = data['player']['stats']['SkyWars']['highestWinstreak']
            except:
                top_winstreak = 'N/A'
            try:
                coins = int(data['player']['stats']['SkyWars']['coins'])
            except:
                coins = 'N/A'
            try:
                souls = data['player']['stats']['SkyWars']['souls']
            except:
                souls = 'N/A'
            try:
                wins = data['player']['stats']['SkyWars']['wins_team_insane']
            except:
                wins = 'N/A'
            try:
                losses = data['player']['stats']['SkyWars']['losses_team_insane']
            except:
                losses = 'N/A'
            embed = discord.Embed(title=name + "'s Skywars Stats - Doubles Insane", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            try:
                embed.add_field(name="Skywars Level", value=str(int(level))+' ⭐', inline=True)
            except:
                embed.add_field(name="Skywars Level", value='N/A', inline=True)
            embed.add_field(name="Skywars Coins", value=str(utils.comma(coins)), inline=True)
            embed.add_field(name="Skywars Souls", value=str(utils.comma(souls)), inline=True)
            embed.add_field(name="Skywars Games Played", value=str(utils.comma(round(games_played, 0))), inline=True)
            embed.add_field(name="Skywars Winstreak", value=str(utils.comma(winstreak)), inline=True)
            embed.add_field(name="Skywars Highest Winstreak", value=str(utils.comma(top_winstreak)), inline=True)
            embed.add_field(name="Kills", value=str(utils.comma(kills)), inline=True)
            embed.add_field(name="Deaths", value=str(utils.comma(deaths)), inline=True)
            try:
                embed.add_field(name="K/D Ratio", value=str(utils.comma(round(int(kills)/int(deaths), 2))), inline=True)
            except:
                embed.add_field(name="K/D Ratio", value='N/A', inline=True)
            embed.add_field(name="Wins", value=str(utils.comma(wins)), inline=True)
            embed.add_field(name="Losses", value=str(utils.comma(losses)), inline=True)
            try:
                embed.add_field(name="W/L Ratio", value=str(utils.comma(round(int(wins)/int(losses), 2))), inline=True)
            except:
                embed.add_field(name="W/L Ratio", value='N/A', inline=True)
            embed.set_footer(text='Unofficial Hypixel Discord Bot - Page 5/6')
            return embed

        async def lab(self, name, color, data):
            try:
                level = 'N/A'
                xp = data['player']['stats']['SkyWars']['skywars_experience']
                xps = [0, 20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000]
                if xp >= 15000:
                    level = (xp - 15000) / 10000. + 12
                else:
                    for i in range(len(xps)):
                        if xp < xps[i]:
                            level = str(utils.comma(int(round(int(1 + i + float(xp - xps[i-1]) / (xps[i] - xps[i-1], 0)))))) + ' ⭐'
            except:
                level = 'N/A'
            try:
                games_played = data['player']['stats']['SkyWars']['games_played_skywars']
            except:
                games_played = 'N/A'
            try:
                winstreak = data['player']['stats']['SkyWars']['win_streak']
            except:
                winstreak = 'N/A'
            try:
                kills = data['player']['stats']['SkyWars']['kills_lab']
            except:
                kills = 'N/A'
            try:
                deaths = data['player']['stats']['SkyWars']['deaths_lab']
            except:
                deaths = 'N/A'
            try:
                top_winstreak = data['player']['stats']['SkyWars']['highestWinstreak']
            except:
                top_winstreak = 'N/A'
            try:
                coins = int(data['player']['stats']['SkyWars']['coins'])
            except:
                coins = 'N/A'
            try:
                souls = data['player']['stats']['SkyWars']['souls']
            except:
                souls = 'N/A'
            try:
                wins = data['player']['stats']['SkyWars']['wins_lab']
            except:
                wins = 'N/A'
            try:
                losses = data['player']['stats']['SkyWars']['losses_lab']
            except:
                losses = 'N/A'
            embed = discord.Embed(title=name + "'s Skywars Stats - Laboratory", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            try:
                embed.add_field(name="Skywars Level", value=str(int(level))+' ⭐', inline=True)
            except:
                embed.add_field(name="Skywars Level", value='N/A', inline=True)
            embed.add_field(name="Skywars Coins", value=str(utils.comma(coins)), inline=True)
            embed.add_field(name="Skywars Souls", value=str(utils.comma(souls)), inline=True)
            embed.add_field(name="Skywars Games Played", value=str(utils.comma(round(games_played, 0))), inline=True)
            embed.add_field(name="Skywars Winstreak", value=str(utils.comma(winstreak)), inline=True)
            embed.add_field(name="Skywars Highest Winstreak", value=str(utils.comma(top_winstreak)), inline=True)
            embed.add_field(name="Kills", value=str(utils.comma(kills)), inline=True)
            embed.add_field(name="Deaths", value=str(utils.comma(deaths)), inline=True)
            try:
                embed.add_field(name="K/D Ratio", value=str(utils.comma(round(int(kills)/int(deaths), 2))), inline=True)
            except:
                embed.add_field(name="K/D Ratio", value='N/A', inline=True)
            embed.add_field(name="Wins", value=str(utils.comma(wins)), inline=True)
            embed.add_field(name="Losses", value=str(utils.comma(losses)), inline=True)
            try:
                embed.add_field(name="W/L Ratio", value=str(utils.comma(round(int(wins)/int(losses), 2))), inline=True)
            except:
                embed.add_field(name="W/L Ratio", value='N/A', inline=True)
            embed.set_footer(text='Unofficial Hypixel Discord Bot - Page 6/6')
            return embed

        async def generate(self, ctx, name, data, perms): 
            color=random.randint(1, 16777215)
            main = await self.main(name, color, data)
            solon = await self.solon(name, color, data)
            soloi = await self.soloi(name, color, data)
            doublesn = await self.doublesn(name, color, data)
            doublesi = await self.doublesi(name, color, data)
            lab = await self.lab(name, color, data)
            paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, timeout=60, remove_reactions=False)
            if perms is not None:
                if perms.manage_messages:
                    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, timeout=60, remove_reactions=True)
            paginator.add_reaction('⏮️', "first")
            paginator.add_reaction('⏪', "back")
            paginator.add_reaction('⏹', "lock")
            paginator.add_reaction('⏩', "next")
            paginator.add_reaction('⏭️', "last")
            embeds = [main, solon, soloi, doublesn, doublesi, lab]
            return embeds, paginator

    class Duels:
        async def main(self, name, color, data):
            pass

        async def bow(self, name, color, data):
            pass

    class TNT:
        async def main(self, name, color, data):
            try:
                coins = utils.comma(int(data['player']['stats']['TNTGames']['coins']))
            except:
                coins = 'N/A'
            try:
                winstreak = utils.comma(int(data['player']['stats']['TNTGames']['winstreak']))
            except:
                winstreak = 'N/A'
            try:
                wins = utils.comma(int(data['player']['stats']['TNTGames']['wins']))
            except:
                wins = 'N/A'
            embed = discord.Embed(title=f"{name}'s TNT Games Stats - Overall", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            embed.add_field(name='TNT Games Coins', value=coins, inline=True)
            embed.add_field(name='Winstreak', value=winstreak, inline=True)
            embed.add_field(name='Wins', value=wins, inline=True)
            embed.set_footer(text="Unofficial Hypixel Discord Bot - Page 1/5")
            return embed

        async def tntrun(self, name, color, data):
            try:
                deaths = utils.comma(int(data['player']['stats']['TNTGames']['deaths_tntrun']))
            except:
                deaths = 'N/A'
            try:
                wins = utils.comma(int(data['player']['stats']['TNTGames']['wins_tntrun']))
            except:
                wins = 'N/A'
            try:
                record = int(data['player']['stats']['TNTGames']['record_tntrun'])
                min, sec = divmod(record, 60) 
                hour, min = divmod(min, 60) 
                if hour == 0:
                    if min == 0:
                        record = f'{sec} seconds'
                    elif min > 0:
                        record = f"{min} minutes, {sec} seconds"
                elif hour > 0:
                    record = f"{hour} hours, {min} minutes, {sec} seconds"
            except:
                record = 'N/A'
            embed = discord.Embed(title=f"{name}'s TNT Games Stats - TNT Run", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            embed.add_field(name='Longest Time Survived', value=record, inline=True)
            embed.add_field(name="Wins", value=wins, inline=True)
            embed.add_field(name="Deaths", value=deaths, inline=True)
            embed.set_footer(text="Unofficial Hypixel Discord Bot - Page 2/5")
            return embed

        async def tnttag(self, name, color, data):
            try:
                kills = utils.comma(int(data['player']['stats']['TNTGames']['kills_tntag']))
            except:
                kills = 'N/A'
            try:
                wins = utils.comma(int(data['player']['stats']['TNTGames']['wins_tntag']))
            except:
                wins = 'N/A'
            embed = discord.Embed(title=f"{name}'s TNT Games Stats - TNT Tag", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            embed.add_field(name="Wins", value=wins, inline=True)
            embed.add_field(name="Kills", value=kills, inline=True)
            embed.set_footer(text="Unofficial Hypixel Discord Bot - Page 3/5")
            return embed

        async def bowspleef(self, name, color, data):
            try:
                tags = utils.comma(int(data['player']['stats']['TNTGames']['tags_bowspleef']))
            except:
                tags = 'N/A'
            try:
                deaths = utils.comma(int(data['player']['stats']['TNTGames']['deaths_bowspleef']))
            except:
                deaths = 'N/A'
            try:
                wins = utils.comma(int(data['player']['stats']['TNTGames']['wins_bowspleef']))
            except:
                wins = 'N/A'
            embed = discord.Embed(title=f"{name}'s TNT Games Stats - Bow Spleef", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            embed.add_field(name="Wins", value=wins, inline=True)
            embed.add_field(name="Deaths", value=deaths, inline=True)
            embed.add_field(name="Tags", value=tags, inline=True)
            embed.set_footer(text="Unofficial Hypixel Discord Bot - Page 4/5")
            return embed

        async def pvprun(self, name, color, data):
            try:
                deaths = utils.comma(int(data['player']['stats']['TNTGames']['deaths_pvprun']))
            except:
                deaths = 'N/A'
            try:
                wins = utils.comma(int(data['player']['stats']['TNTGames']['wins_pvprun']))
            except:
                wins = 'N/A'
            try:
                record = int(data['player']['stats']['TNTGames']['record_pvprun'])
                min, sec = divmod(record, 60) 
                hour, min = divmod(min, 60) 
                if hour == 0:
                    if min == 0:
                        record = f'{sec} seconds'
                    elif min > 0:
                        record = f"{min} minutes, {sec} seconds"
                elif hour > 0:
                    record = f"{hour} hours, {min} minutes, {sec} seconds"
            except:
                record = 'N/A'
            try:
                kills = utils.comma(int(data['player']['stats']['TNTGames']['kills_pvprun']))
            except:
                kills = 'N/A'
            try:
                kdr = utils.comma(data['player']['stats']['TNTGames']['kills_pvprun']/data['player']['stats']['TNTGames']['deaths_pvprun'])
            except:
                kdr = 'N/A'
            embed = discord.Embed(title=f"{name}'s TNT Games Stats - PvP Run", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            embed.add_field(name='Kills', value=kills, inline=True)
            embed.add_field(name="Deaths", value=deaths, inline=True)
            embed.add_field(name="K/D Ratio", value=kdr, inline=True)
            embed.add_field(name='Longest Time Survived', value=record, inline=True)
            embed.add_field(name="Wins", value=wins, inline=True)
            embed.set_footer(text="Unofficial Hypixel Discord Bot - Page 5/5")
            return embed

        async def generate(self, ctx, name, data, perms):
            color=random.randint(1, 16777215)
            main = await self.main(name, color, data)
            tntrun = await self.tntrun(name, color, data)
            tnttag = await self.tnttag(name, color, data)
            bowspleef = await self.bowspleef(name, color, data)
            pvprun = await self.pvprun(name, color, data)
            paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, timeout=60, remove_reactions=False)
            if perms is not None:
                if perms.manage_messages:
                    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, timeout=60, remove_reactions=True)
            paginator.add_reaction('⏮️', "first")
            paginator.add_reaction('⏪', "back")
            paginator.add_reaction('⏹', "lock")
            paginator.add_reaction('⏩', "next")
            paginator.add_reaction('⏭️', "last")
            embeds = [main, tntrun, tnttag, bowspleef, pvprun]
            return embeds, paginator

    class Help:
        async def botinfo(self, color):
            embed = discord.Embed(title='Help - Bot Info', description=botinfo + other, color=color)
            embed.set_footer(text='Unofficial Hypixel Discord Bot - Page 1/3')
            return embed
        
        async def playerstats(self, color):
            embed = discord.Embed(title='Help - Player Stats', description=playerstats + other, color=color)
            embed.set_footer(text='Unofficial Hypixel Discord Bot - Page 2/3')
            return embed

        async def hypixelstats(self, color):
            embed = discord.Embed(title='Help - Hypixel Stats', description=hypixelstats + other, color=color)
            embed.set_footer(text='Unofficial Hypixel Discord Bot - Page 3/3')
            return embed

        async def mc(self, color):
            embed = discord.Embed(title='Help - Minecraft', description=minecraft + other, color=color)
            embed.set_footer(text='Unofficial Hypixel Discord Bot - Page 3/3')
            return embed

        async def generate(self, ctx, perms):
            color=random.randint(1, 16777215)
            one = await self.botinfo(color)
            two = await self.playerstats(color)
            three = await self.hypixelstats(color)
            paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, timeout=60, remove_reactions=False)
            if perms is not None:
                if perms.manage_messages:
                    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, timeout=60, remove_reactions=True)
            paginator.add_reaction('⏮️', "first")
            paginator.add_reaction('⏪', "back")
            paginator.add_reaction('⏹', "lock")
            paginator.add_reaction('⏩', "next")
            paginator.add_reaction('⏭️', "last")
            embeds = [one, two, three]
            return embeds, paginator

    class PlayerCount:
        async def pages(self, color, data):
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
            embeds = []
            embed = discord.Embed(title="Hypixel Player Counts", color = color)
            embed.add_field(name='Total', value=str(utils.comma(network)))
            embed.add_field(name='Main Lobby', value=str(utils.comma(lobby)))
            embed.add_field(name='Tournament Lobby', value=str(utils.comma(tournament_lobby)))
            embed.set_footer(text='Unofficial Hypixel Discord Bot - Page 1/9')
            embeds.append(embed)

            embed = discord.Embed(title="Hypixel Player Counts", color = color)
            embed.add_field(name='Bedwars', value=str(utils.comma(bedwars)))
            embed.add_field(name='Skywars', value=str(utils.comma(skywars)))
            embed.add_field(name='Skyblock', value=str(utils.comma(skyblock)))
            embed.set_footer(text='Unofficial Hypixel Discord Bot - Page 2/9')
            embeds.append(embed)

            embed = discord.Embed(title="Hypixel Player Counts", color = color)
            embed.add_field(name='Arcade', value=str(utils.comma(arcade)))
            embed.add_field(name='Duels', value=str(utils.comma(duels)))
            embed.add_field(name='UHC', value=str(utils.comma(uhc)))
            embed.set_footer(text='Unofficial Hypixel Discord Bot - Page 3/9')
            embeds.append(embed)

            embed = discord.Embed(title="Hypixel Player Counts", color = color)
            embed.add_field(name='TNT Games', value=str(utils.comma(tnt_games)))
            embed.add_field(name='Classic Games', value=str(utils.comma(classic_games)))
            embed.add_field(name='Blitz Survival Games', value=str(utils.comma(blitz_survival_games)))
            embed.set_footer(text='Unofficial Hypixel Discord Bot - Page 4/9')
            embeds.append(embed)
            
            embed = discord.Embed(title="Hypixel Player Counts", color = color)
            embed.add_field(name='Build Battle', value=str(utils.comma(build_battle)))
            embed.add_field(name='Murder Mystery', value=str(utils.comma(murder_mystery)))
            embed.add_field(name='Housing', value=str(utils.comma(housing)))
            embed.set_footer(text='Unofficial Hypixel Discord Bot - Page 5/9')
            embeds.append(embed)

            embed = discord.Embed(title="Hypixel Player Counts", color = color)
            embed.add_field(name='Smash Heroes', value=str(utils.comma(smash_heroes)))
            embed.add_field(name='Speed UHC', value=str(utils.comma(speed_uhc)))
            embed.add_field(name='Mega Walls', value=str(utils.comma(mega_walls)))
            embed.set_footer(text='Unofficial Hypixel Discord Bot - Page 6/9')
            embeds.append(embed)

            embed = discord.Embed(title="Hypixel Player Counts", color = color)
            embed.add_field(name='The Pit', value=str(utils.comma(the_pit)))
            embed.add_field(name='Cops and Crims', value=str(utils.comma(cops_and_crims)))
            embed.add_field(name='Warlords', value=str(utils.comma(warlords)))
            embed.set_footer(text='Unofficial Hypixel Discord Bot - Page 7/9')
            embeds.append(embed)

            embed = discord.Embed(title="Hypixel Player Counts", color = color)
            embed.add_field(name='Prototype', value=str(utils.comma(prototype)))
            embed.add_field(name='Limbo', value=str(utils.comma(limbo)))
            embed.add_field(name='Replay', value=str(utils.comma(replay)))
            embed.set_footer(text='Unofficial Hypixel Discord Bot - Page 8/9')
            embeds.append(embed)

            embed = discord.Embed(title="Hypixel Player Counts", color = color)
            embed.add_field(name='Idle', value=str(utils.comma(idle)))
            embed.add_field(name='Queue', value=str(utils.comma(queue)))
            embed.set_footer(text='Unofficial Hypixel Discord Bot - Page 9/9')
            embeds.append(embed)
            return embeds

        async def generate(self, ctx, data, perms):
            color=random.randint(1, 16777215)
            embeds = await self.pages(color, data)
            paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, timeout=60, remove_reactions=False)
            if perms is not None:
                if perms.manage_messages:
                    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, timeout=60, remove_reactions=True)
            paginator.add_reaction('⏮️', "first")
            paginator.add_reaction('⏪', "back")
            paginator.add_reaction('⏹', "lock")
            paginator.add_reaction('⏩', "next")
            paginator.add_reaction('⏭️', "last")
            return embeds, paginator

    class Player:
        async def general(self, name, color, data):
            try:
                #set rank to players rank
                rank = 'N/A'
                if "rank" in data["player"] and data["player"]["rank"] != "NORMAL":
                    rank = data["player"]["rank"]
                elif "monthlyPackageRank" in data["player"]:
                    if data['player']['monthlyPackageRank'] == "SUPERSTAR":
                        rank = "MVP++"
                elif "newPackageRank" in data["player"]:
                    rank = data["player"]["newPackageRank"]
                elif "packageRank" in data["player"]:
                    rank = data["player"]["packageRank"]
                else:
                    rank = "Default"
                if rank == "VIP_PLUS":
                    rank = "VIP+"
                elif rank == "MVP_PLUS":
                    rank = "MVP+"
                elif rank == "YOUTUBER":
                    rank = "YouTube"
                elif rank == "ADMIN":
                    rank = "Administrator"
                elif rank == "MODERATOR":
                    rank = "Moderator"
                elif rank == "HELPER":
                    rank = "Helper"
                else:
                    rank = 'N/A'
            except:
                rank = 'N/A'
            try:
                recent = utils.gameconverter(data['player']['mostRecentGameType'])
            except:
                recent = 'N/A'
            try:
                karma = data["player"]["karma"] if "karma" in data["player"] else 0
            except:
                karma = 'N/A'
            try:
                lastlogin = data['player']['lastLogin']
                lastlogout = data['player']['lastLogout']
                status = utils.timeconverter(lastlogin, lastlogout)
                if status is None:
                    status = 'N/A'
            except:
                status = 'N/A'
            try:
                level = utils.networklevel(data['player']['networkExp'])
            except:
                level = 'N/A'
            try:
                guild = await hypixel.playerguild(data['player']['_id'])
            except:
                guild = 'N/A'
            embed = discord.Embed(title=name + "'s Profile - General Info", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            embed.add_field(name="Rank", value=str(rank), inline=True)
            embed.add_field(name="Karma", value=str(utils.comma(karma)), inline=True)
            embed.add_field(name="Guild", value=str(utils.comma(guild)), inline=True)
            embed.add_field(name="Level", value=str(utils.comma(level)), inline=True)
            embed.add_field(name="Recently Played", value=str(recent), inline=True)
            embed.add_field(name="Status", value=str(status), inline=True)
            embed.set_footer(text='Unofficial Hypixel Discord Bot - Page 1/3')
            return embed

        async def social(self, name, color, data):
            try:
                forums = data['player']['socialMedia']['links']['HYPIXEL']
            except:
                forums = 'None'
            try:
                discorda = data['player']['socialMedia']['links']['DISCORD']
            except:
                discorda = 'None'
            try:
                twitch = data['player']['socialMedia']['links']['TWITCH']
            except:
                twitch = 'None'
            try:
                ig = data['player']['socialMedia']['links']['INSTAGRAM']
            except:
                ig = 'None'
            try:
                youtube = data['player']['socialMedia']['links']['YOUTUBE']
            except:
                youtube = 'None'
            try:
                twitter = data['player']['socialMedia']['links']['TWITTER']
            except:
                twitter = 'None'
            embed = discord.Embed(title=name + "'s Profile - Social", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            embed.add_field(name="Hypixel Forums", value=str(forums), inline=False)
            embed.add_field(name="Discord", value=str(discorda), inline=False)
            embed.add_field(name="YouTube", value=str(youtube), inline=False)
            embed.add_field(name="Twitch", value=str(twitch), inline=False)
            embed.add_field(name="Twitter", value=str(twitter), inline=False)
            embed.add_field(name="Instagram", value=str(ig), inline=False)
            embed.set_footer(text='Unofficial Hypixel Discord Bot - Page 2/3')
            return embed

        async def other(self, name, color, data):
            try:
                version = data['player']['mcVersionRp']
            except:
                version = 'N/A'
            try:
                achievementpoints = data['player']['achievementPoints']
            except:
                achievementpoints = 'N/A'
            try:
                pet = ''
                e = data['player']['currentPet'].lower().split('_')
                for i in e:
                    y = i.capitalize()
                    pet += f'{y} '
            except:
                pet = 'N/A'
            try:
                time = datetime.fromtimestamp(data['player']['firstLogin']/1000.0)
                first = time.strftime("%m/%d/%Y")
            except:
                first = 'N/A'
            try:
                aliases = ''
                for alias in data['player']['knownAliases']:
                    aliases += f"{alias}\n"
            except:
                aliases = 'N/A'
            try:
                uuid = data['player']['_id']
            except:
                uuid = 'N/A'
            embed = discord.Embed(title=name + "'s Profile - Social", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            embed.add_field(name="First Joined", value=str(first), inline=True)
            embed.add_field(name="UUID", value=str(uuid), inline=True)
            embed.add_field(name="Recently Played Version", value=str(version), inline=True)
            embed.add_field(name="Achievement Points", value=str(utils.comma(achievementpoints)), inline=True)
            embed.add_field(name="Current Pet", value=str(pet), inline=True)
            embed.add_field(name="Known Aliases", value=str(aliases), inline=True)
            embed.set_footer(text='Unofficial Hypixel Discord Bot - Page 3/3')
            return embed

        async def generate(self, ctx, name, data, perms):
            color=random.randint(1, 16777215)
            general = await self.general(name, color, data)
            social = await self.social(name, color, data)
            other = await self.other(name, color, data)
            paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, timeout=60, remove_reactions=False)
            if perms is not None:
                if perms.manage_messages:
                    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, timeout=60, remove_reactions=True)
            paginator.add_reaction('⏮️', "first")
            paginator.add_reaction('⏪', "back")
            paginator.add_reaction('⏹', "lock")
            paginator.add_reaction('⏩', "next")
            paginator.add_reaction('⏭️', "last")
            embeds = [general, social, other]
            return embeds, paginator

    class Skyblock:
        class SkyblockProfiles:
            async def main(self, name, color, data, length):
                try:
                    msg = ''
                    for profile in data['player']['stats']['SkyBlock']['profiles']:
                        profile = data['player']['stats']['SkyBlock']['profiles'][profile]
                        msg = msg+f"{profile['cute_name']}\n"
                    if msg == '':
                        msg = "This player has no skyblock profiles."
                except:
                    msg = 'N/A'
                embed = discord.Embed(title=f"{name}'s Skyblock Profile - List", description=msg + "\n\nSome data may be unavailable because of the player's API settings.", color=color)
                embed.set_footer(text=f'Unofficial Hypixel Discord Bot - Page 1/{length}')
                return embed
            
            async def profilelist(self, name, color, data, uuid):
                profiles = {}
                embeds = []
                length = len(data['player']['stats']['SkyBlock']['profiles'])+1
                for profile1 in data['player']['stats']['SkyBlock']['profiles']:
                    profile1 = data['player']['stats']['SkyBlock']['profiles'][profile1]
                    pname = profile1['cute_name']
                    profiles[pname] = {}
                    profiles[pname]['data'] = (await hypixel.skyblock.profile(profile1['profile_id']))
                p = 1
                for profile in profiles:
                    p += 1
                    profiledata = profiles[profile]['data']
                    try:
                        members = len(profiledata['profile']['members'])
                    except:
                        members = 'N/A'
                    try:
                        bank = round(profiledata['profile']['banking']['balance'], 2)
                    except:
                        bank = 'N/A'
                    memberdata = profiledata['profile']['members'][uuid]
                    try:
                        first_join = memberdata['first_join']
                        time = datetime.fromtimestamp(first_join/1000.0)
                        date = time.strftime("%m/%d/%Y")
                        first_join = str(date)
                    except:
                        first_join = 'N/A'
                    try:
                        deaths = int(memberdata['stats']['deaths'])
                    except:
                        deaths = 'N/A'
                    try:
                        kills = int(memberdata['stats']['kills'])
                    except:
                        kills = 'N/A'
                    try:
                        bids = int(memberdata['stats']['auctions_bids'])
                    except:
                        bids = 'N/A'
                    try:
                        topbid = int(memberdata['stats']['auctions_highest_bid'])
                    except:
                        topbid = 'N/A'
                    try:
                        awon = int(memberdata['stats']['auctions_won'])
                    except:
                        awon = 'N/A'
                    try:
                        purse = round(memberdata['coin_purse'], 2)
                    except:
                        purse = 'N/A'
                    embed = discord.Embed(title = f"{name}'s Skyblock Profile - {profile}", description="Some data may be unavailable because of the player's API settings.", color = color)
                    embed.add_field(name="Profile Members", value=utils.comma(members))
                    embed.add_field(name="Profile Bank", value=utils.comma(bank))
                    embed.add_field(name="First Join", value=first_join)
                    embed.add_field(name="Kills", value=utils.comma(kills))
                    embed.add_field(name="Deaths", value=utils.comma(deaths))
                    try:
                        embed.add_field(name="K/D Ratio", value=utils.comma(round(kills/deaths, 2)))
                    except:
                        embed.add_field(name="K/D Ratio", value='N/A')
                    embed.add_field(name="Bids", value=utils.comma(bids))
                    embed.add_field(name="Highest Bid", value=utils.comma(topbid))
                    embed.add_field(name="Auctions Won", value=utils.comma(awon))
                    embed.add_field(name="Purse", value=utils.comma(purse))
                    embed.set_footer(text=f'Unofficial Hypixel Discord Bot - Page {p}/{length}')
                    embeds.append(embed)
                return embeds, length

            async def generate(self, ctx, name, data, perms, uuid):
                color=random.randint(1, 16777215)
                profiles, length = await self.profilelist(name, color, data, uuid)
                main = await self.main(name, color, data, length)
                paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, timeout=60, remove_reactions=False)
                if perms is not None:
                    if perms.manage_messages:
                        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, timeout=60, remove_reactions=True)
                paginator.add_reaction('⏮️', "first")
                paginator.add_reaction('⏪', "back")
                paginator.add_reaction('⏹', "lock")
                paginator.add_reaction('⏩', "next")
                paginator.add_reaction('⏭️', "last")
                embeds = [main]
                for embed in profiles:
                    embeds.append(embed)
                return embeds, paginator

        class News:
            async def embeds(self, color, data):
                length = len(data)
                embeds = []
                i = 0
                for article in data:
                    i += 1
                    try:
                        url = article['link']
                    except:
                        url = 'https://hypixel.net/'
                    try:
                        title = article['title']
                    except:
                        title = 'N/A'
                    try:
                        text = article['text']
                    except:
                        text = 'N/A'
                    embed=discord.Embed(title=title, url=url, description=text, color=color)
                    embed.set_footer(text=f"Unofficial Hypixel Discord Bot - Page {i}/{length}")
                    embeds.append(embed)
                return embeds

            async def generate(self, ctx, data, perms):
                color=random.randint(1, 16777215)
                embeds = await self.embeds(color, data)
                paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, timeout=60, remove_reactions=False)
                if perms is not None:
                    if perms.manage_messages:
                        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, timeout=60, remove_reactions=True)
                paginator.add_reaction('⏮️', "first")
                paginator.add_reaction('⏪', "back")
                paginator.add_reaction('⏹', "lock")
                paginator.add_reaction('⏩', "next")
                paginator.add_reaction('⏭️', "last")
                return embeds, paginator