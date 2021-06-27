from Utils.Writer import Writer
from Logic.Player import Players

class StartLoadingMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20559;
        self.player = player

    def encode(self):
        self.writeInt(6) #6
        self.writeInt(0)
        self.writeInt(0)
        
        self.writeInt(6) #players count
        
        self.writeInt(0) #High ID
        self.writeInt(1) #Low ID
        self.writeString("Dudnik")
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeInt(30) #unk
        
        self.writeScId(16, 1)
        self.writeScId(29, 0)
        self.writeByte(0)
        
        self.writeInt(0) #High ID
        self.writeInt(3) #Low ID
        self.writeString("Land")
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(0)
        self.writeInt(30) #unk
        
        self.writeScId(16, 5)
        self.writeScId(29, 0)
        self.writeByte(0)
        
        self.writeInt(0) #High ID
        self.writeInt(4) #Low ID
        self.writeString("Polaris")
        self.writeVint(2)
        self.writeVint(0)
        self.writeVint(0)
        self.writeInt(30) #unk
        
        self.writeScId(16, 8)
        self.writeScId(29, 0)
        self.writeByte(0)
        
        self.writeInt(0) #High ID
        self.writeInt(5) #Low ID
        self.writeString("Mozhevelnik")
        self.writeVint(4)
        self.writeVint(1)
        self.writeVint(0)
        self.writeInt(30) #unk
        
        self.writeScId(16, 0)
        self.writeScId(29, 0)
        self.writeByte(0)
        
        self.writeInt(0) #High ID
        self.writeInt(6) #Low ID
        self.writeString("Guest")
        self.writeVint(5)
        self.writeVint(1)
        self.writeVint(0)
        self.writeInt(30) #unk
        
        self.writeScId(16, 9)
        self.writeScId(29, 0)
        self.writeByte(0)
        
        self.writeInt(0) #High ID
        self.writeInt(2) #Low ID
        self.writeString("Debil")
        self.writeVint(3)
        self.writeVint(1)
        self.writeVint(1)
        self.writeInt(30) #unk
        
        self.writeScId(16, 1)
        self.writeScId(29, 0)
        
        self.writeByte(0)
        
        #PLAYERS SLOT END#
        
        self.writeInt(2) #count...
        
        self.writeInt(0) #High ID
        self.writeInt(1) #Low ID
        
        self.writeInt(0) #High ID
        self.writeInt(2) #Low ID
        
        self.writeInt(1000) #unknown
        
        self.writeVint(1)
        self.writeVint(1) #DrawMap
        self.writeVint(1)
        
        self.writeByte(1) #2, 39 - Spectating
        
        self.writeScId(15, 7)
        