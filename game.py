"""
Game System Files
Card Game
Canahedo
2025
"""

import random
import os


class Game:
    def __init__(self, board: object):
        self.splash()
        while True:
            self.mulligan()
            self.play(board)
            if self.replay():
                board.reset()
            else:
                break

    def splash(self):
        # Replace with a spash screen for when game starts
        print("Splash Scren Placeholder")
        input("Press Enter to continue")
        os.system("clear||cls")

    def mulligan(self):
        print("Placeholder for mulligan")
        input("Press Enter to continue")
        os.system("clear||cls")

    def play(self, board):
        board.display()
        pass

    def replay(self):
        # Needs to be fleshed out
        while True:
            replay_input = input("\nPlay again?\n")
            if replay_input == "y":
                return True
            elif replay_input == "n":
                return False


class BoardState:
    def __init__(self):
        self.reset()

    def reset(self):
        self.plr_hand = []
        self.plr_up = []
        self.plr_down = []
        self.opp_hand = []
        self.opp_up = []
        self.opp_down = []
        self.discard = []
        self.deck = []

        for num in range(2, 11):
            for i in range(4):
                if num in [2, 7, 10]:
                    self.deck.append(str(num) + "*")
                else:
                    self.deck.append(str(num))
        for face in ["J", "Q", "K", "A"]:
            for i in range(4):
                self.deck.append(face)
        random.shuffle(self.deck)

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
        card = self.deck[0]
        deal_to.append(card)
        self.deck.remove(card)

    def display(self):
        opp_hand_disp = []
        opp_down_disp = []
        plr_down_disp = []
        for i in range(len(self.opp_hand)):
            opp_hand_disp.append("X")
        for i in range(len(self.opp_down)):
            opp_down_disp.append("X")
        for i in range(len(self.plr_down)):
            plr_down_disp.append("X")
        print(opp_hand_disp)
        print(self.opp_up)
        print(opp_down_disp)
        print("\n")
        print(self.plr_up)
        print(plr_down_disp)
        print(self.plr_hand)
