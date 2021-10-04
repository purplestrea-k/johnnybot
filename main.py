from Slots import Slots
from johnny import JohnnyClient
from CasinoGamesCog import CasinoGamesBaseCog
import os 
#import json

def  main():


 bot = JohnnyClient(command_prefix='!')


## with open("emotes.json","r") as read_file:
  #   emotedict=json.load(read_file)

 '''
 print(list(emotedict))   
 print(emotedict)
 print(int("2"))
 '''
 
 #cogSlot = CasinoGamesBaseCMDS(bot)
 print("Reached")
 #bot.add_cog(cogSlot)
 bot.add_cog(Slots(bot))

 bot.run(os.getenv("TOKEN"))
 


if __name__ == '__main__':
    main()