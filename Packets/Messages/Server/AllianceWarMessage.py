from Utils.Writer import Writer


class AllianceWarMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24104
        self.player = player

    def encode(self):
        self.writeVint(0)
