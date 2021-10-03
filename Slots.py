#from CasinoGames import CasinoGamesBaseCMDS
from discord.ext import commands

from CasinoGames import CasinoGamesBaseCMDS


class Slots(CasinoGamesBaseCMDS, name="slotsCog"):
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

   
    @commands.command(name="joinslots")
    async def joinslots(self, ctx):
     super().casinogametable.append(ctx.author)   
     #print(ctx.author)
     print(super().casinogametable[0])
     await ctx.send("Hook funcanilty for joing active seesion")


    @commands.command(name="stopslots")
    async def stopslot(self, ctx):
     await ctx.send("Hook up funcintailty to stop all slot games")

    @commands.command(name="leaveslots")
    async def leaveslot(self, ctx):
     await ctx.send("Hook up funcanilty to leave game")

