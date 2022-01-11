import random

from Card import Card


class CardDeck:
    deck: list[Card] = []

    @staticmethod
    def getCards(amount: int) -> list[Card]:
        """
        Get cards from the deck
        :param amount: amount of cards to get (Must me less or equal to the amount of cards in the deck)
        """

        if amount > len(CardDeck.deck):
            CardDeck.fill()

        cards = CardDeck.deck[:amount]
        CardDeck.deck = CardDeck.deck[amount:]
        return cards

    @staticmethod
    def fill() -> None:
        """
        Fills the deck with the default cards
        """

        for color in range(4):
            for numbers in range(19):
                CardDeck.deck.append(Card(color, numbers % 10))  # 1-9  - Default color cards

            for x in range(2):
                CardDeck.deck.append(Card(color, 10))   # 10    - +2
                CardDeck.deck.append(Card(color, 11))   # 11    - Skip
                CardDeck.deck.append(Card(color, 12))   # 12    - Direction change

        for x in range(4):
            CardDeck.deck.append(Card(4, 13))           # 13    - Wild +4
            CardDeck.deck.append(Card(4, 14))           # 14    - Wild Color change

    @staticmethod
    def shuffle() -> None:
        """
        Shuffle the dack randomly
        """
        random.shuffle(CardDeck.deck)
