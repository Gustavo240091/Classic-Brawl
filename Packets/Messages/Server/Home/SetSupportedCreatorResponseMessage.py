from Utils.Writer import Writer

class SetSupportedCreatorResponseMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 28686
        self.player = player

    def encode(self):
        self.writeVint(1)
        self.writeString(self.player.content_creator)