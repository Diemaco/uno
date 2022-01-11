from termcolor import colored


class Card:

    def __init__(self, color: int, cardType: int):
        self.color = color
        self.cardType = cardType

    def getText(self) -> str:
        return colored(
            self._getCardType(),
            self.getColor(self.color)
        )

    def _getCardType(self) -> str:
        return ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+2', 'Skip', 'Direction Change', 'Wild +4',
                'Wild Color Change'][self.cardType]

    @staticmethod
    def getColor(color: int) -> str:
        return ['yellow', 'green', 'blue', 'red', 'cyan'][color]

