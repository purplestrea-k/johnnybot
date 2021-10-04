class playerInfo:

    def __init__(self,playerID,balance):

     self._playerID=playerID
     self._wonAmt=0
     self._lostAmt=0
     self._newbalance=balance
     
     @property #Discord ID of player
     def playerID(self):
          return self._playerID

     @playerID.setter #Returns Discord ID of player
     def playerID(self, val):
         self._playerID = val

    @property #Getting amount won during duration of game.
    def wonAmt(self):
        return self._wonAmt

    @wonAmt.setter #Setting amont won during duraction of game.
    def wonAmt (self, val):
      self._wonAmt=val
    

     
    @property
    def lostAmt(self): #Getting amount lost during duration of game
          return self._lostAmt
    
    @lostAmt.setter   #Setting amont lost during duraction of game
    def lostAmt(self, val):
          self._lostAmt=val
    
    @property          #returns current balance
    def newbalance(self):
      return self._newbalance

    @newbalance.setter #sets balance. This is later saved in DB via a cog call.
    def playerID(self, val):
         self._newbalance = val












