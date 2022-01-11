import random

from Card import Card
from IPlayer import IPlayer


class Bot(IPlayer):

    def play(self, topCards: list[Card], players: int, nextPlayer) -> Card:
        """
        Make the player play a card
        """

        cards: dict[Card, int] = dict.fromkeys(self.cards, -100)

        for card in cards:

            # Check if the card is actually playable otherwise ignore it
            if super().canPlay(topCards, [card]):
                cards[card] = 0
            else:
                continue

            # Direction change card
            if card.cardType == 12:
                cards[card] = 10

            # Two players
            if players == 2:

                # Skip card
                if card.cardType == 11:
                    cards[card] = 50

                # Direction change card
                if card.cardType == 12:
                    cards[card] = 0

            # +2 card
            if card.cardType == 10:

                # Next player has less than 6 cards
                if len(nextPlayer.cards) < 6:
                    cards[card] = 80

            # +4 card
            if card.cardType == 13:

                # Next player has less than 4 cards
                if len(nextPlayer.cards) < 4:
                    cards[card] = 150

            for i in topCards:

                if i.color == card.color:
                    cards[card] -= 4

                if i.cardType == card.cardType:
                    cards[card] -= 4

        # Choose the card with the biggest number
        chosenCard = None
        for i in cards:
            if chosenCard is None or cards.get(chosenCard) < cards.get(i):
                chosenCard = i

        return chosenCard

    @staticmethod
    def getChosenColor() -> int:
        """
        Get the color the player has chosen to set
        :return: The chosen color
        """
        return random.randrange(4)
