from abc import ABC, abstractmethod
from random import choice


class PlayerBase(ABC):
    choices = ["r", "p", "s"]

    @abstractmethod
    def move(self):
        pass


class HumanPlayer(PlayerBase):
    def move(self):
        m = input("choose your next move ....")
        return m


class SytemPlayer(PlayerBase):
    def move(self):
        return choice(self.choices)


class Game:
    def start_game(self, game_type):
        if game_type == 's':
            p1 = HumanPlayer()
            p2 = SytemPlayer()
        elif game_type == 'm':
            p1 = HumanPlayer()
            p2 = HumanPlayer()
        else:
            print('invalid input')
            p1 = None
            p2 = None
        return p1, p2


if __name__ == "__main__":
    game = Game()
    game_type = input('select game type ( "S" for single player "M" for multiplayer )')
    game.start_game(game_type)
