from random import *
from Database.DatabaseManager import DataBase
from Packets.Messages.Server.OutOfSyncMessage import OutOfSyncMessage
from Logic.Boxes import Boxes

from Utils.Writer import Writer


class LogicSkinDataCommand(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.player = player
        self.BoxData = Boxes.boxes

    def encode(self):
        self.writeVint(203) # Command
        self.writeVint(0)
        self.writeVint(1) # Multipler
        self.writeVint(10) # Box ID
        self.writeVint(1) # Reward Count

        self.writeVint(1) # Value
        self.writeVint(0) # ScId
        self.writeVint(9) # Reward ID
        self.writeScId(29, 0) # ScId
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(0)
        