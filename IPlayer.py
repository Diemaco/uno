from Card import Card


class IPlayer:
    def __init__(self, name):
        # Player cards
        self.cards: list[Card] = []

        # Player name
        self.name = name

    def giveCards(self, cards: list[Card]) -> None:
        """
        Give cards to the player
        :param cards: The cards to give
        """
        self.cards += cards

    def removeCard(self, card: Card) -> None:
        """
        Removes a card from the player's inventory
        :param card: The card to remove
        """
        self.cards.pop(self.cards.index(card))

    @staticmethod
    def canPlay(topCards: list[Card], cards: list[Card]) -> bool:
        """
        Check if the player can play
        :param cards: Held cards
        :param topCards: The discard pile
        """
        topCard = topCards[-1]

        for card in cards:
            # Checking for same colors
            if card.color == topCard.color:
                return True

            # Checking for the same number
            if card.cardType == topCard.cardType:
                return True

            # Checking wild cards
            if card.color == 4 or topCard.color == 4:
                return True

        return False

    @staticmethod
    def getChosenColor() -> int:
        """
        Get the color the player has chosen to set
        :return: The chosen color
        """
        pass

    def play(self, topCards: list[Card], players: int, nextPlayer) -> Card:
        """
        Make the player play a card
        """
        pass
