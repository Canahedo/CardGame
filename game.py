"""
Game System Files
Card Game
Canahedo
2025
"""

from random import shuffle
from os import system


class BoardState:
    def __init__(self):
        self.reset()

    def reset(self):
        """
        Creates lists to represent various zones of the boardstate,
        generate and shuffle a deck, and deal the start of the game
        """

        # Generate Zones
        self.plr_hand = []
        self.plr_up = []
        self.plr_down = []
        self.opp_hand = []
        self.opp_up = []
        self.opp_down = []
        self.discard = []
        self.deck = []

        # Generate Deck
        for num in range(2, 11):
            for i in range(4):
                if num in [2, 7, 10]:
                    self.deck.append(str(num) + "*")
                else:
                    self.deck.append(str(num))
        for face in ["J", "Q", "K", "A"]:
            for i in range(4):
                self.deck.append(face)
        shuffle(self.deck)

        # Initial Deal
        for i in range(3):
            for x in [
                self.plr_hand,
                self.plr_up,
                self.plr_down,
                self.opp_hand,
                self.opp_up,
                self.opp_down,
            ]:
                self.deal(x)

    def deal(self, deal_to):
        # Removes one card from Deck and adds it to another Zone
        card = self.deck[0]
        deal_to.append(card)
        self.deck.remove(card)

    def mulligan(self, mull_1, mull_2):
        pass

    def display(self):
        """
        Displays current state of Board to screen
        """

        # Creates a dummy version of hidden info
        opp_hand_disp = []
        opp_down_disp = []
        plr_down_disp = []
        for i in range(len(self.opp_hand)):
            opp_hand_disp.append("X")
        for i in range(len(self.opp_down)):
            opp_down_disp.append("X")
        for i in range(len(self.plr_down)):
            plr_down_disp.append("X")

        # Creates a list of the last 3 played cards
        discard_disp = []
        if len(self.discard) == 1:
            discard_disp = self.discard
        elif len(self.discard) == 2:
            for card in [self.discard[-2], self.discard[-1]]:
                discard_disp.append(card)
        elif len(self.discard) >= 3:
            for card in [self.discard[-3], self.discard[-2], self.discard[-1]]:
                discard_disp.append(card)

        # Prints Board with hidden info obscured
        print("Opponent's Hand       ", end="")
        print(opp_hand_disp)
        print("Opponent's Face-Up    ", end="")
        print(self.opp_up)
        print("Opponent's Face-Down  ", end="")
        print(opp_down_disp)
        print("\n")
        print("Cards Left in Deck    ", end="")
        print(len(self.deck))
        print("Recently Played Cards ", end="")
        print(discard_disp)
        print("Cards in Discard Pile ", end="")
        print(len(self.discard))
        print("\n")
        print("Your Hand             ", end="")
        print(self.plr_up)
        print("Your Face-Up          ", end="")
        print(plr_down_disp)
        print("Your Face-Down        ", end="")
        print(self.plr_hand)


class Game:
    def __init__(self, board=BoardState()):

        # Display Start of Game Text
        splash()

        while True:

            # Lets Player swap Face-Up Cards at Start of Game
            self.offer_mull(board)
            system("clear||cls")

            # Run Game
            self.play(board)

            # Offer Replay, or End Game
            if self.replay():
                board.reset()
            else:
                break

    def offer_mull(self, board):
        mull_intro_text()

        # Choose Face-Up Cards to move to Hand
        # If no input entered, skips mulligan
        while True:
            mull_text_1()
            raw_1 = input()
            if len(raw_1) < 1:
                return
            mull_1 = sani_mull(raw_1)
            if mull_1 is not None:
                break

        # Choose Cards in Hand to be placed Face-Up
        # Requires that the same number of cards be chosen as in mull_1
        while True:
            mull_text_2(len(mull_1))
            raw_2 = input()
            if len(raw_2) < 1:
                continue
            mull_2 = sani_mull(raw_2)
            if mull_2 is not None and len(mull_1) == len(mull_2):
                break

        # Applies mulligan choices
        board.mulligan(mull_1, mull_2)
        system("clear||cls")

    def play(self, board):
        # For now, only displays board
        board.display()
        input()
        pass

    def replay(self):
        # Needs to be fleshed out
        while True:
            replay_input = input("\nPlay again?\n")
            if replay_input == "y":
                return True
            elif replay_input == "n":
                return False


def sani_mull(input):
    # Accepts raw player input and returns a list of cards
    valid_chars = "1234567890jJqQkKaA* "
    scratch = []
    output = []
    for char in input:
        if char not in valid_chars:
            return None
        if char == "*":
            continue
        if char in "jqka":
            scratch.append(char.capitalize())
        else:
            scratch.append(char)

    return output


def splash():
    # Replace with a spash screen for when game starts
    print("Splash Scren Placeholder")
    input("Press Enter to continue")
    system("clear||cls")


def mull_intro_text():
    print("At the beginning of the game, you have a chance to swap")
    print("face-up cards for cards in your hand. This can help get")
    print("lower cards into your hand, so you can play them sooner.\n")


def mull_text_1():
    print("Choose up to 3 of your face-up cards, seperated by a space.")


def mull_text_2(x):
    print(f"Choose exactly {x} cards from")
    print("your hand to be placed face-up.")
