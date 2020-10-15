# HypixelBot
A Hypixel Discord Bot

This bot will soon be heavily modified to implement the usage of discord.py's cogs.

To run this bot, change `<Discord Bot Token>` in hypixelbot.py to your Discord Bot Token, which can be retrieved from your Discord Developer Portal, and change `<API key>` in hypixelbot.py to your Hypixel API Key, which can be created by connecting to mc.hypixel.net and running the `/api new` command.

This bot retrieves stats from the official public [Hypixel API](https://api.hypixel.net). Documentation for the API can be found at [https://github.com/HypixelDev/PublicAPI/tree/master/Documentation](https://github.com/HypixelDev/PublicAPI/tree/master/Documentation)

Thanks to [@DimBis](https://github.com/DimBis) for helping me with this project.

## Requirements
mojang - `python -m pip install mojang`

requests - `pip install requests`

discord.py - `py -3 -m pip install -U discord.py`

## Commands
`h!help` - A list of commands.

`h!player <playername>` - Info on a specified player.

`h!bedwars <playername>` - Bedwars Stats for a specified player.

`h!skywars <playername>` - Skywars Stats for a specified player.

`h!guild <guild>` - Information on a specified guild.

## Invite
To add this bot to your server, click [here](https://discord.com/api/oauth2/authorize?client_id=764677833820995605&permissions=0&scope=bot).
