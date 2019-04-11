from Player import Player
from DiceCup import DiceCup


class GameEngine:
    player1 = Player("player 1")
    player2 = Player("player 2")
    diceCup = DiceCup()
    players = []

    def __init__(self):
        pass

    def get_curPlayer(self):
        return self.curPlayer

    def set_curPlayer(self, player):
        self.curPlayer = player

    def start_game(self):
        player1 = Player("Player1")
        self.players.append(player1)
        player2 = Player("Player2")
        self.players.append(player2)
        # input_string = str(input("Select number of players"))
        #
        # for x in range(1, int(input_string) + 1):
        #     name = str(input("Enter name for player " + str(x)))
        #     player = Player(name)
        #     self.players.append(player)

    def play(self):
        print("Let the game begin!")
        curPlayer = self.players[0]
        while True:

            str(input('It\'s ' + curPlayer.get_name() + '\'s turn! \nPres enter to throw the dice!'))
            self.diceCup.roll()
            print("Roll is :" + str(self.diceCup.sum))
            curPlayer.set_sum(self.diceCup.sum)
            print(curPlayer.get_name() + "'s current sum is " + str(curPlayer.get_sum()) + '\n')

            if curPlayer.get_sum() >= 30:
                print(curPlayer.get_name() + ' has won the game!')
                break

            curPlayer = self.decide_cur_player(curPlayer)

    def decide_cur_player(self, player):
        index = self.players.index(player)
        if index + 1 == len(self.players):
            return self.players[0]
        else:
            return self.players[index + 1]

    def main(self):
        game = GameEngine()
        game.start_game()
        game.play()


#   print(len(game.players))


if __name__ == '__main__':
    GameEngine.main(GameEngine)
