class WtfCommandMessage:
    def __init__(self, word, username):
        self.word = word
        self.username = username

    def __str__(self) -> str:
        return "(text={}, username={})".format(self.word, self.username)
