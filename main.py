import discord
import os
from replit import db
import random

token = os.environ['TOKEN']
client = discord.Client()

def learn(message):
  if 'words' not in db.keys():
    db['words'] = ['Hello']
    return db['words']
  else:
    words = db['words']
    if message not in words:
      words.append(message)
      db['words'] = words
    return words


def get_random_word(message):
  words = learn(message.replace('$', ''))
  return random.choice(words)


@client.event
async def on_ready():
  print(f'we have logged as {client.user}')


@client.event
async def on_message(message):
  if message.author == client.user :
    return 
  msg = message.content
  if msg.startswith('$hello'):
    await message.channel.send('Hello!')
  elif msg.startswith('$'):
    m = get_random_word(msg)
    await message.channel.send(m)



client.run(token)