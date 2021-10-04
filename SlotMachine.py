from PlayerInformation import playerInfo
import random
import discord

class SlotMachineRep:

 def __init__(self,playerID,EmoteStyle):
  self._playerID=playerID
  self._EmoteStyle =EmoteStyle
  self._machineRepresentationMAT = [[self._EmoteStyle[str(random.randint(1,4))] for col in range (3)] for row in range(3)] 

 def __repr__(self):
     return(


             
         f"|{self._machineRepresentationMAT[0][0]:2}|{self._machineRepresentationMAT[0][1]:2}|{self._machineRepresentationMAT[0][2]:2}| \n" 
         f"|{self._machineRepresentationMAT[1][0]:2}|{self._machineRepresentationMAT[1][1]:2}|{self._machineRepresentationMAT[1][2]:2}| \n"
         f"|{self._machineRepresentationMAT[2][0]:2}|{self._machineRepresentationMAT[2][1]:2}|{self._machineRepresentationMAT[2][2]:2}| \n"
                         
             )




 @property #Discord ID of player
 def playerID(self):
    return self._playerID

 @playerID.setter #Returns Discord ID of player
 def playerID(self, val):
    self._playerID = val
    
 def spin(self):
  self._machineRepresentationMAT= [[self._EmoteStyle[str(random.randint(1,4))] for col in range (3)] for row in range(3)] 
 # print(self._machineRepresentationMAT[0][0]) #note print bug
  #return   self._machineRepresentationMAT
  return   
  #print(self._machineRepresentationMAT)

    #print(self._EmoteStyle["1"])
    ##return 
    
 def _displaytable(self):
     for x in self._machineRepresentationMAT:
      print (self._machineRepresentationMAT)
     return






    
