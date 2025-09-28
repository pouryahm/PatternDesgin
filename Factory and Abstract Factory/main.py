from abc import ABC, abstractmethod


class PlayerBase(ABC):
    @abstractmethod
    def move(self):
        pass


class HumanPlayer(PlayerBase):
    pass


class SytemPlayer(PlayerBase):
    pass


if __name__ == "__main__":
    pass
