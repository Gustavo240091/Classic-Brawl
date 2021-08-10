from Utils.Writer import Writer
from Utils.Helpers import Helpers
#from Protocol.Commands.Server.LogicChangeAvatarNameCommand import #LogicChangeAvatarNameCommand
from Packets.Commands.Server.LogicSetSupportedCreatorCommand import LogicSetSupportedCreatorCommand
#from Packets.Commands.Server.LogicGiveDeliveryItemsCommand import LogicGiveDeliveryItemsCommand

class AvailableServerCommandMessage(Writer):

    def __init__(self, client, player, commandID):
        super().__init__(client)
        self.id = 24111
        self.player = player
        self.commandID = commandID

    def encode(self):

        commands = {
            #201: LogicChangeAvatarNameCommand,
            #203: LogicGiveDeliveryItemsCommand,
            215: LogicSetSupportedCreatorCommand
        }

        if self.commandID in commands:

            self.writeVint(self.commandID)
            commands[self.commandID].encode(self)
        else:
            print(f"[SERVER] Cannot create command! ID: {self.commandID}")