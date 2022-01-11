from termcolor import colored

from CardDeck import *
from Player import Player
from Players import *

if __name__ == '__main__':

    # Setup players
    Players.fill(1)

    Players.players += [Player("DimCo")]

    # Setup the card deck
    CardDeck.fill()
    CardDeck.shuffle()

    # Giving each player 7 cards
    for player in Players.players:
        player.giveCards(CardDeck.getCards(7))

    # Random player starts
    Players.setRandomPlayer()

    # The top card
    discardPile: list[Card] = CardDeck.getCards(1)

    # Show the top card
    print(f'The first card is {Card.getText(discardPile[-1])}')

    playedNothing = False

    # Game loop
    while True:

        # The current player
        currentPlayer = Players.getNextPlayer()

        if not playedNothing:

            # If the previous card is a wild 4 give the current player 4 cards
            if discardPile[-1].cardType == 13:
                print(currentPlayer.name, colored('has to draw 4 cards', 'red'))
                currentPlayer.giveCards(CardDeck.getCards(4))

            # Check for a +2 card
            if discardPile[-1].cardType == 10:
                print(currentPlayer.name, colored('has to draw 2 cards', 'red'))
                currentPlayer.giveCards(CardDeck.getCards(2))

        print(f'{currentPlayer.name} is next and has {len(currentPlayer.cards)} cards')

        # Card played by the player
        playedCard = None

        # Checking if the player can actually play
        if currentPlayer.canPlay(discardPile, currentPlayer.cards):

            # Make the player play its card
            playedCard = currentPlayer.play(discardPile, len(Players.players), Players.getNextPlayer(False))
        else:

            print('They can\'t play and draw a card')

            # Player can't play so we will give it a card from the draw pile
            currentPlayer.giveCards(CardDeck.getCards(1))

            # Check if the player can now play
            if currentPlayer.canPlay(discardPile, currentPlayer.cards):
                # Make the player play its card
                playedCard = currentPlayer.play(discardPile, len(Players.players), Players.getNextPlayer(False))

        if playedCard is not None:
            print(f'They play {Card.getText(playedCard)}')

            # Remove the played card from the players inventory
            currentPlayer.removeCard(playedCard)

            # Add the played card to the DISCARD pile
            discardPile.append(playedCard)

            # Change the playedCard color to the chosen color
            if playedCard.cardType == 14:  # or playedCard.cardType == 13:
                # The chosen color
                chosenColor = currentPlayer.getChosenColor()

                discardPile[-1].color = chosenColor
                print(f'The new color is {colored(Card.getColor(chosenColor), Card.getColor(chosenColor))}')

            # Reverse the play direction
            if playedCard.cardType == 12:
                Players.switchDirection()

            # Skip the next player
            if playedCard.cardType == 11:
                print(colored(f'\n{Players.getNextPlayer().name} skipped\n', 'red'))

            if playedCard.cardType == 12 and len(Players.players) == 2:
                print(colored(f'\n{Players.getNextPlayer().name} skipped\n', 'red'))

            playedNothing = False
        else:
            playedNothing = True

        input('')
        print('\n' * 20)

        # Checking if the player has won
        if len(currentPlayer.cards) == 0:
            print(f'{currentPlayer.name} has won the game!')
            exit(0)
