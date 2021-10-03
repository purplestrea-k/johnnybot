#import mysql.connector
from discord.ext import commands

#class CasinoGamesBaseCMDS(commands.Cog, name = 'CbaseCMDMod' ):

class CasinoGamesBaseCog(commands.Cog, name ='casompgamesBaseCog'): 
    #connection =mysql.connector.connect()
    #clientInfo = discord.client()

    casinogametable = []

    

    
    def __init__(self,bot):
     self.bot=bot #Client vairable for holding discord information.
#self.casinogametable = []
    # self.msg=self.client.guilds.message
     print("Casino Intilalized")
     #self.earning
     #connection info here

    def returnbalance(self): #ID will be taking from client and then connected to mysql.
     return 100

    
    @commands.command(name="earnings")
    async def earn(self, ctx):
     #selfearning = self.returnbalance()
     await ctx.send(self.returnbalance())

    @commands.command(name="clr")
    async def clr(self, ctx):
     #selfearning = self.returnbalance()
     await ctx.send("clears all active games and deactives bot")
    
    '''
    async def on_message(self,msg):
        print("2/4")
        if msg.content.lower() == "!returnbalance": 
           # balance = message.author
            #balance = returnbalance()
            await msg.channel.send('Isa has 100' )
        elif msg.content.lower() == "stopgame":
            await msg.channel.send(CasinoGames.text + " has ended")
        else:
            return
    '''


    

    

 
   
    




    

