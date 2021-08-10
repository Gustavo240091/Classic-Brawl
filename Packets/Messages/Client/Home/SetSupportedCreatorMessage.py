from Database.DatabaseManager import DataBase
from Packets.Messages.Server.AvailableServerCommandMessage import AvailableServerCommandMessage
from Packets.Messages.Server.Home.SetSupportedCreatorResponseMessage import SetSupportedCreatorResponseMessage

from Utils.Reader import BSMessageReader

class SetSupportedCreatorMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.content_creator = self.read_string()

    def process(self):

        if self.player.content_creator.lower() in self.player.content_creator_codes or self.player.content_creator == '':
            DataBase.replaceValue(self, 'SupportedContentCreator', self.player.content_creator)
            AvailableServerCommandMessage(self.client, self.player, 215).send()
        else:
            SetSupportedCreatorResponseMessage(self.client, self.player).send()


