# HypixelBot
A Hypixel Discord Bot

To run this bot, change `<Discord Bot Token>` in hypixelbot.py to your Discord Bot Token, which can be retrieved from your Discord Developer Portal, and change `<API key>` in hypixelbot.py to your Hypixel API Key, which can be created by connecting to mc.hypixel.net and running the `/api new` command.

This bot retrieves stats from the official public [Hypixel API](https://api.hypixel.net). Documentation for the API can be found at [https://github.com/HypixelDev/PublicAPI/tree/master/Documentation](https://github.com/HypixelDev/PublicAPI/tree/master/Documentation)
## Requirements
mojang - `python -m pip install mojang`

requests - `pip install requests`

discord.py - `py -3 -m pip install -U discord.py`

## Commands
`/help` - A list of commands (will be made custom)

`/player <playername>` - Info on a specified player.

`/bedwars <playername>` - Bedwars Stats for a specified player.

## Invite
To add this bot to your server, click [here](https://discord.com/api/oauth2/authorize?client_id=764677833820995605&permissions=0&scope=bot).
