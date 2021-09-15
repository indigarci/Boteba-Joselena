import discord 
import os
import json
from pathlib import Path


client = discord.Client()
with open(Path(os.getcwd() + '/lores.json')) as json_file:
  lores = json.load(json_file)

@client.event
async def on_ready():
  print(f'Boteba en marcha! Id: {client.user}')
  print(f'\n Workdir: {os.getcwd()}')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  # Joder a Mitx
  print(message.author)
  if str(message.author).startswith('Avetch'):
    await message.channel.send('La gorda de sailor Moon')

  msg = message.content

  # Commands
  if msg.startswith('$hello'):
    await message.channel.send('hola')
 
  # JSON key checking 
  coincidences = get_coincidences(msg.split(" "), lores.keys())
  for key in coincidences:
    await message.channel.send(f"\nDetectado: {key}\nRespuesta: {lores[key]}")


def get_coincidences(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

client.run(os.getenv('TOKEN'))