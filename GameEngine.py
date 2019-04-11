from Player import Player
import random


class GameEngine:

    def __init__(self):
        self.players = []
        self.face_value1 = 0
        self.face_value2 = 0
        self.curPlayer = None
        self.player1 = None
        self.player2 = None

    def get_curPlayer(self):
        return self.curPlayer

    def set_curPlayer(self, player):
        self.curPlayer = player

    def start_game(self):
        input_string = str(input("Select number of players"))

        for x in range(1, int(input_string) + 1):
            name = str(input("Enter name for player " + str(x)))
            player = Player(name)
            self.players.append(player)

    def play(self):
        print("Let the game begin!")
        self.curPlayer = self.players[0]
        while True:
            str(input('It\'s ' + self.curPlayer.get_name() + '\'s turn! \nPres enter to throw the dice!'))
            self.roll_dice_cup()
            self.eval_roll()

            if self.curPlayer.get_sum() >= 30 or self.curPlayer.get_won():
                print(self.curPlayer.get_name() + ' has won the game!')
                break

            self.curPlayer = self.decide_cur_player(self.curPlayer)

    def decide_cur_player(self, player):
        index = self.players.index(player)
        if index + 1 == len(self.players):
            return self.players[0]
        else:
            return self.players[index + 1]

    def eval_roll(self):
        if self.face_value1 == self.face_value2 and self.face_value1 != 1:
            str(input(("Double roll! " + self.curPlayer.get_name() + " press enter to roll again!")))
            if self.face_value1 == 6 and self.face_value2 == 6:
                self.roll_dice_cup()
                if self.face_value1 == 6 and self.face_value2 == 6:
                    self.curPlayer.set_won(True)
                    print(self.curPlayer + " got two double six'! and have won the game!")
                else:
                    self.eval_roll()

            self.roll_dice_cup()
            self.eval_roll()

        elif self.face_value1 == 1 and self.face_value2 == 1:
            print("Double 1! " + self.curPlayer.get_name() + " lose all points!\n")
            self.curPlayer.delete_sum
        else:
            print(self.curPlayer.get_name() + " now have " + str(self.curPlayer.get_sum())+"\n")

    def roll_dice_cup(self):
        self.face_value1 = random.randint(1, 6)
        self.face_value2 = random.randint(1, 6)
        self.curPlayer.set_sum(self.face_value1 + self.face_value2)
        print("Die 1 rolls :" + str(self.face_value1) + '\n' + "Die 2 rolls :" + str(self.face_value2))

