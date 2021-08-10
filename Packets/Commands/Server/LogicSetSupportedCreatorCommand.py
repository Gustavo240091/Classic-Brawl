from Utils.Writer import Writer

class LogicSetSupportedCreatorCommand(Writer):

    def encode(self):
        self.writeVint(1)
        self.writeString(self.player.content_creator)
        self.writeVint(1)