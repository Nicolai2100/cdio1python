class Player:

    numberOfPlayers = 0

    def __init__(self, name):
        self.__name = name
        self.__number = Player.numberOfPlayers
        Player.numberOfPlayers += 1
        self.__num = self.numberOfPlayers
        self.__sum = 0
        self.__won = False

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_sum(self, sum):
        self.__sum += sum

    def delete_sum(self):
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def set_won(self, value):
        self.__won = value

    def get_won(self):
        return self.__won

# print(help(str))
#print(dir(play1.get_name()))

