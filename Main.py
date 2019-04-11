from GameEngine import GameEngine

class Main:
    def __init__(self):
        pass

    def main(self):
        game = GameEngine()
        game.start_game()
        game.play()


if __name__ == '__main__':
    Main().main()
