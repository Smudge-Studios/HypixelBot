# HypixelBot
[![TOP.GG](https://top.gg/api/widget/764677833820995605.svg)](https://top.gg/bot/764677833820995605)
[![Discord Bot List](https://discordbotlist.com/bots/764677833820995605/widget)](https://discordbotlist.com/bots/764677833820995605)

A Hypixel Discord Bot made purely for displaying Hypixel statistics.

To run this bot, change `<TOKEN>` in `botconfig.ini` to your Discord Bot Token, which can be retrieved from your Discord Developer Portal, and change `<API KEY>`, also in `botconfig.ini` to your Hypixel API Key, which can be created by connecting to mc.hypixel.net and running the `/api new` command.

This bot retrieves statistics from the official public [Hypixel API](https://api.hypixel.net). Documentation for the API can be found [here](https://github.com/HypixelDev/PublicAPI/tree/master/Documentation).

Thanks to [@DimBis](https://dimmy.xyz) for helping me with this project.

This bot is currently in development, there may be some bugs.

## License
[plun1331/HypixelBot](https://github.com/plun1331/HypixelBot) is licensed under the MIT License. This license can be viewed [here](https://github.com/plun1331/HypixelBot/blob/main/LICENSE).

## Requirements
- mojang

- discord.py

## Commands

### Public Commands

These commands can be used by anyone.

#### Bot Info

- `h!help` - Displays this.

- `h!ping` - Displays the bot's latency.

- `h!info` - Displays some info and stats about the bot.

#### Hypixel Stats

- `h!player <player>` - Returns the specified player's profile.

- `h!bedwars <player>` - Returns the specified player's Bedwars statistics.

- `h!skywars <player>` - Returns the specified player's Skywars statistics.

- `h!pit <player>` - Returns the specified player's Pit statistics.

- `h!murdermystery <player>` - Returns the specified player's Murder Mystery statistics.

- `h!guild <guild name>` - Returns information on the specified guild.

#### Hypixel Info

- `h!playercount` - Returns Hypixel player counts.

- `h!watchdog` - Returns Hypixel Watchdog statistics.

### Restricted Commands

These commands can only be used by a bot owner.

- `h!load <extension>` - Load a discord.py extension.

- `h!unload <extension>` - Unload a discord.py extension.

- `h!reload <extension>` - Reload a discord.py extension.

- `h!stop` - Shutdown the bot.

## Invite
To add this bot to your server, click [here](https://discord.com/api/oauth2/authorize?client_id=764677833820995605&permissions=0&scope=bot).
