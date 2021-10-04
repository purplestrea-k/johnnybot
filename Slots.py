#from CasinoGames import CasinoGamesBaseCMDS
from discord.ext import commands
from SlotMachine import SlotMachineRep
from CasinoGamesCog import CasinoGamesBaseCog
import json



class Slots(CasinoGamesBaseCog, name="slotsCog"):
    
    with open("debugEmotes.json","r") as read_file:
           EmoteStyle=json.load(read_file)         

    def __init__(self, bot):
        print("Slots Intialized")
        
        
        super().__init__(bot)

    ''' 
    def __init__(self, bot):
        self.bot = bot
        self.slotScreenReprsentationMat = []
        # self.gamerepresentation = [[0] * 3 for row in 3]
    '''



    @commands.command(name="paytable")
    async def pt(self, ctx):
     await ctx.send("Hook up PT strings and formating")

    #if player is not active, start, else ignore.
    @commands.command(name="startslot")
    async def joinslots(self, ctx):
     ##super().casinogametable.append(ctx.author)
     super().casinogametable.append(SlotMachineRep(ctx.author,self.EmoteStyle))    
     #print(ctx.author)
     #super().casinogametable[0].spin()
     #()

     await ctx.send(super().casinogametable[0])

      #TODO-implement isactive checking. If a player has an active game, ignore startslots



    @commands.command(name="bet5")
    async def bet5(self, ctx):
     super().casinogametable[0].spin() 
     await ctx.send(super().casinogametable[0])


    '''
    @commands.command(name="stopslots")
    async def stopslot(self, ctx):
     await ctx.send("Hook up funcintailty to stop all slot games")
    '''

    #A play can only close thier active game. So they both havet o be active and have a game. Ignore elsewhere
    @commands.command(name="leaveslots")
    async def leaveslot(self, ctx):
     await ctx.send("Hook up funcanilty to leave game")

