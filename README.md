# Discord Bot

## Crear Bot

https://discord.com/developers/applications

1. New application
2. Name -> Create
3. Bot -> Add Bot
4. OAuth2 -> Tick "Bot" -> Tick desired permissions
5. Copy link -> Go to linked web -> Select server

> **Important!!** Copy and save the bot token from "Bot" section. We will use it to run it in the main function.

## Bot basico


Este es el código básico para correr un bot de discord:

  ```
  import discord

  @client.event
  async def on_ready():
    """What to do when the bot initializes."""  

  @client.event
  async def on_message(message):
    """What to do when bot recives a message."""

  client = discord.Client()
  client.run(TOKEN)
  ```

> TOKEN: bot token that we have saved before

## Resources:

Git repository: https://github.com/indigarci/Boteba-Joselena

Youtube video: https://www.youtube.com/watch?v=SPTfmiYiuok

Online IDE: https://replit.com/

Discord for developers: https://discord.com/developers/applications/887397005213708369/bot

Discord API: https://discordpy.readthedocs.io/en/latest/api.html#client
