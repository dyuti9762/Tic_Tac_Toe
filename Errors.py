class PositionNotValidError(Exception):

    def __init__(self, position):
        self.position = position

    def __str__(self):
        return "The Position {} is Invalid".format(self.position)
