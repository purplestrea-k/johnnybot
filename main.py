from Slots import Slots
from CasinoGames import CasinoGamesBaseCMDS
from johnny import JohnnyClient
import os

def  main():
 bot = JohnnyClient(command_prefix='!')
 
 #cogSlot = CasinoGamesBaseCMDS(bot)
 print("Reached")
 #bot.add_cog(cogSlot)
 bot.add_cog(Slots(bot))

 bot.run(os.getenv("TOKEN"))
 


if __name__ == '__main__':
    main()