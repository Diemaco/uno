import random

from Bot import Bot
from IPlayer import IPlayer


class Players:
    players: list[IPlayer] = []

    direction: int = 1

    player_index = 0

    @staticmethod
    def fill(amount: int) -> None:
        """
        Create bots and add them to the list
        :param amount: Amount of bots to add
        """
        for i in range(amount):
            Players.players.append(Bot(f'Player {i + 1}'))

    @staticmethod
    def getNextPlayer(save: bool = True) -> IPlayer:
        """
        Get the player next up
        """
        if save:
            Players.player_index += Players.direction
            Players.player_index %= len(Players.players)
        return Players.players[Players.player_index]

    @staticmethod
    def setRandomPlayer() -> None:
        """
        Sets a random player to start
        """
        Players.player_index = random.randrange(0, len(Players.players))

    @staticmethod
    def switchDirection() -> None:
        """
        Switch the direction in which the next player is chosen
        """
        Players.direction = -Players.direction
