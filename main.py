from Slots import Slots
from johnny import JohnnyClient
from CasinoGamesCog import CasinoGamesBaseCog
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