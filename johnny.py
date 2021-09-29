import discord
import os

client = discord.Client()



@client.event
async def on_ready(): #Refractor in larger ready check def later, for now this is fun.
    print("{0.user} is online".format(client))


@client.event
async def on_message(message):
    if message.author == client.user: #ignore my bots own messages
        return
    if message.content.startswith("!test"):
        await message.channel.send('This test was succesful')
    if message.content.lower() == "!slots":
        await message.channel.send('Slots is starting...')
    



'''
Todo put in a seris of ready check functions.
def readychecks():
    if not (client.is_ready):
        print("Bot isn't ready")
        client.st
'''



client.run(os.getenv("TOKEN")) #Setup an enviroment variable and pass it here



 