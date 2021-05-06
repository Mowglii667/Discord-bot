import discord
import os
import requests
import json
from replit import db
from keep_alive import keep_alive
client = discord.Client()




if "responding" not in db.keys():
  db["responding"] = True

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragment(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if msg.startswith("parzival"):
    await message.channel.send("ta mere la pute parzival")
  
  if msg.startswith("Parzival"):
    await message.channel.send("ta mere la pute parzival")
  if msg.startswith("Qui pour une game"):
    await message.channel.send("Ferme ta gueule")

  if msg.startswith("caca"):
    await message.channel.send("fils de pute")

  if msg.startswith("Twitter"):
    await message.channel.send("https://twitter.com/lekarmalegentil")

  if msg.startswith("twitter"):
    await message.channel.send("https://twitter.com/lekarmalegentil")

    if msg.startswith ("Jacques"):
      await message.channel.send("jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay jacques est gay")
  if msg.startswith ("jacques"):
    await message.channel.send("Jacques est un joueur dit pro sur valorant,pourtant,sur un chargeur de 30 balles,il arrive à en mettre qu'une seul.Si mes calculs sont bon,une balle divisé par 30,Jacques metterais 0,3 balles,une vrai merde.")
  if msg.startswith("Twitch"):
    await message.channel.send("https://www.twitch.tv/mowgliiaucromis")

  if msg.startswith("twitch"):
     await message.channel.send("https://www.twitch.tv/mowgliiaucromis")

  if msg.startswith("le pire joueur?"):
    await message.channel.send("jacque el backisto")
  
  if msg.startswith("brevet"):
     await message.channel.send("frr on a les brevets blanc rend pas fou")
  
  if msg.startswith("Test"):
    await message.channel.send("Oue")
  
  if msg.startswith("mowglii"):
    await message.channel.send("Mowglii est un pro player valorant née le 8 octobre 2006 à Antony.Il a commencé sa carrière sur minecraft,puis sur call of duty,ensuite gta,enfin fortnite,et depuis joue à Valorant en tant que chienne de Riot game.Riot game est une companie de merde meritant la mort ayant crée les jeux les plus ragants jamais crée.")
  
  if msg.startswith("Mowglii"):
    await message.channel.send("Mowglii est un pro player valorant née le 8 octobre 2006 à Antony.Il a commencé sa carrière sur minecraft,puis sur call of duty,ensuite gta,enfin fortnite,et depuis joue à Valorant en tant que chienne de Riot game.Riot game est une companie de merde meritant la mort ayant crée les jeux les plus ragants jamais crée.")
  
  if msg.startswith("Gabin"):
    await message.channel.send("Inscrit dans le livre des records,Gabin est le premier homophobe gay.")
  
  if msg.startswith("Lotfi"):
    await message.channel.send("brrr brrr gang bavette en y la mala est gangx")   

keep_alive()
client.run(os.getenv('TOKEN'))
