from Card import Card
from IPlayer import IPlayer


class Player(IPlayer):

    @staticmethod
    def getChosenColor() -> int:
        """
        Get the color the player has chosen to set
        :return: The chosen color
        """

        while True:
            answer = input('What is the next color? [1. Yellow, 2. Green, 3. Blue, 4. Red]\n')

            if answer.isdigit() and (0 < int(answer) < 5):
                return int(answer) - 1
            else:
                print('That is not an option')

    def play(self, topCards: list[Card], players: int, nextPlayer) -> Card:
        c: list[Card] = []

        topCard = topCards[-1]

        print(f'Top card: {topCard.getText()}')



        for card in self.cards:
            # Checking for same colors
            if card.color == topCard.color:
                c.append(card)
                continue

            # Checking for the same number
            if card.cardType == topCard.cardType:
                c.append(card)
                continue

            # Checking wild cards
            if card.color == 4 or topCard.color == 4:
                c.append(card)
                continue

        print('You have:')

        for card in self.cards:
            print(f'{card.getText():<26}', end='')
        print('')

        i = 1
        for card in c:
            print(f'{Card.getText(card):<26}', end='')
            i += 1

        while True:
            chosenCard = input(f'\nWhich card do you want to choose? [1-{len(c)}]')

            if chosenCard.isdigit():

                if 0 < int(chosenCard) <= len(c):
                    return c[int(chosenCard) - 1]
                else:
                    print('That was not an option')
            else:
                print('That is not a number...')
