#! /usr/bin/env python3
# Carson Carpenter
# CPSC 386-02
# 2022-03-29
# carson.carpenter7@csu.fullerton.edu
# @carsoncarpenter7
#
# Lab 03-00
#
# This the game program contents
#


"""This module contains the contents of PigGame"""


from time import sleep
from blackjackgame import cards
from .cards import Deck
from .player import Player


class BlackJackGame:
    """BlackJack Game class"""

    def __init__(self):
        self._deck = cards.Deck()
        # self._deck = cards.Deck(1, 10)
        # players and read in any data files
        self._number_of_players = int(input("How many Players? [1-4]"))
        if self._number_of_players > 4:
            print("Error: 4 Players Max.")
            self._number_of_players = int(input("How many Players? [1-4]"))
        self._players = []
        self._totalbalance = []
        # dealer
        self._dealer = []
        self._score = 10000
        self._game_is_not_over = True

    @staticmethod
    def none():
        """Fixing pylint errors"""
        return

    def run(self):
        """Run the game program"""
        for index in range(self._number_of_players):
            order = index
            score = self._score
            name = input("What is your Name? ")
            self._players.append(Player(name, order, score))
        print("Current Players: {} ".format(self._players))
        while self._game_is_not_over:
            print("===== Top of the game loop =====")
            # Player Plays Dealer
            player1_score = []
            player2_score = []
            player3_score = []
            player4_score = []
            # Track Wagers for all Players before dealing
            run_once = 0
            if run_once == 0:
                for key in self._players:
                    score = self._score
                    if self._players[0] == key:
                        # print("TEST: {}" .format(self._players[0]))
                        print("Please Place your bets:")
                        print("Player: {} ".format(key))
                        player_wager = int(input("Enter wager amount:"))
                        if player_wager < 1:
                            print("Wager must be at least $1.")
                        elif player_wager > score:
                            # Restore Wager
                            score = score + player_wager
                            print(
                                "Insufficient Funds. \
                                You balance is {}".format(
                                    score
                                )
                            )
                        else:
                            score = score - player_wager
                            player1_score.append(score)
                            self._totalbalance.append(Player(key, order, score))
                            print("New Balance: {}\n".format(score))
                        # print("AFTER: {} ".format(self._totalbalance))
                        # print("Balance: {}".format(player1_score))

                    elif self._players[1] == key:
                        # print("TEST: {}" .format(self._players[0]))
                        print("Please Place your bets:")
                        print("Player: {} ".format(key))
                        player_wager = int(input("Enter wager amount:"))
                        if player_wager < 1:
                            print("Wager must be at least $1.")
                        elif player_wager > score:
                            # Restore Wager
                            score = score + player_wager
                            print(
                                "Insufficient Funds. \
                                You balance is {}".format(
                                    score
                                )
                            )
                        else:
                            score = score - player_wager
                            # player2_score.append(self._players[1])
                            player2_score.append(score)
                            self._totalbalance.append(Player(key, order, score))
                            print("New Balance: {} \n".format(score))
                        # print("AFTER: {} ".format(self._totalbalance))
                        # print("Balance: {}".format(player2_score))
                        run_once = 1

                    elif self._players[2] == key:
                        # print("TEST: {}" .format(self._players[0]))
                        print("Please Place your bets:")
                        print("Player: {} ".format(key))
                        player_wager = int(input("Enter wager amount:"))
                        if player_wager < 1:
                            print("Wager must be at least $1.")
                        elif player_wager > score:
                            # Restore Wager
                            score = score + player_wager
                            print(
                                "Insufficient Funds. \
                                You balance is {}".format(
                                    score
                                )
                            )
                        else:
                            score = score - player_wager
                            # Player.score = score - player_wager
                            # player3_score.append(self._players[2])
                            player3_score.append(score)
                            self._totalbalance.append(Player(key, order, score))
                            print("New Balance: {}\n".format(score))
                            run_once = 1
                        # print("AFTER: {} ".format(self._totalbalance))
                        # print("Balance: {}".format(player3_score))

                    elif self._players[3] == key:
                        # print("TEST: {}" .format(self._players[0]))
                        print("Please Place your bets:")
                        print("Player: {} ".format(key))
                        player_wager = int(input("Enter wager amount:"))
                        if player_wager < 1:
                            print("Wager must be at least $1.")
                        elif player_wager > score:
                            # Restore Wager
                            score = score + player_wager
                            print(
                                "Insufficient Funds. \
                                You balance is {}".format(
                                    score
                                )
                            )
                        else:
                            score = score - player_wager
                            # Player.score = score - player_wager
                            # player4_score.append(self._players[3])
                            player4_score.append(score)
                            self._totalbalance.append(Player(key, order, score))
                            print("New Balance: {}\n".format(score))
                            run_once = 1
                        # print("AFTER: {} ".format(self._totalbalance))
                        # print("Balance: {}".format(player4_score))
                print("Current Players Balance: {} ".format(self._totalbalance))

            # Create, Shuffle, and Merge 8 decks of Cards
            # Access cards
            print("\nShuffling Cards... \n")
            for deck_of_cards in range(7):
                deck_of_cards = Deck()
                deck_of_cards2 = Deck()
                deck_of_cards3 = Deck()
                deck_of_cards4 = Deck()
                deck_of_cards5 = Deck()
                deck_of_cards6 = Deck()
                deck_of_cards7 = Deck()
                deck_of_cards8 = Deck()
                Deck.merge(deck_of_cards, deck_of_cards2)
                Deck.merge(deck_of_cards, deck_of_cards3)
                Deck.merge(deck_of_cards, deck_of_cards4)
                Deck.merge(deck_of_cards, deck_of_cards5)
                Deck.merge(deck_of_cards, deck_of_cards6)
                Deck.merge(deck_of_cards, deck_of_cards7)
                Deck.merge(deck_of_cards, deck_of_cards8)
            # print(deck_of_cards)
            deck_of_cards.shuffle(10)
            deck_of_cards.cut()
            # print(type(deck_of_cards))
            # print("\n \n")
            print("Cards Shuffled! \n")

            # Deal Cards
            # Keep Track of All hands Dealt
            new_hand = []
            dealer_hand = []
            for key in self._totalbalance:
                # Holds Each individual Players Cards
                player_hand = [[] for player in range(self._number_of_players)]
                if self._number_of_players == 1:
                    print("Game Start:\n\tMano a mano (◣_◢)\n\t\t\t - Dealer\n")
                    print("Player: {}".format(key))
                    for _ in range(2):
                        for hand in player_hand:
                            hand.append(deck_of_cards.deal())
                        for _ in range(1):
                            dealer_hand.append(deck_of_cards.deal())
                    print("Dealing Cards: {} \n".format(hand))
                    new_hand.append(hand)
                else:
                    print("Player: {}".format(key))
                    for _ in range(2):
                        for hand in player_hand:
                            hand.append(deck_of_cards.deal())
                    for _ in range(1):
                        dealer_hand.append(deck_of_cards.deal())
                    print("Dealing Cards: {} \n".format(hand))
                    new_hand.append(hand)
            # Split Cards
            # Access Cards
            # print("\n Card 1 \n {} \n".format(new_hand[0][0]))
            # print("\n Card 2 \n {} \n".format(new_hand[0][1]))
            # print("\n Card 3 \n {} \n".format(new_hand[0][0][0][0]))
            # print("\n Card 4 \n {} \n".format(new_hand[0][1][0][0]))
            # print("\n Card 5 \n {} \n".format(new_hand[2][0]))
            # print("\n Card 6 \n {} \n".format(new_hand[2][1]))
            # print("\n Card 7 \n {} \n".format(new_hand[3][0]))
            # print("\n Card 8 \n {} \n".format(new_hand[3][1]))
            card1_value = new_hand[0][0]
            card2_value = new_hand[0][1]
            if card1_value == card2_value:
                print("\n Card 1 \n {} \n".format(card1_value))
                print("\n Card 2 \n {} \n".format(card2_value))
                split = input("Would you like to split your cards? [Y / N]")
                # if split != "Y" or split != "y" or split != "N" or split != "n":
                #     print("Invalid Input: Enter Y for Yes or N for No.\n")
                #     split = input("Would you like to split your cards? [Y / N] ")
                #     if split == "Y" or split == "y":
                #         split = True
                #         print("\nSuccess!")
                #         # print(split)
                #         if split is True:
                #             print("Splitting Cards: ")
                #             for _ in range(1):
                #                 hand.append(deck_of_cards.deal())
                #             print(
                #                 "Dealing Cards: {} \n {} \n".format(new_hand[0], hand)
                #             )

            # print("\nAll Player Cards: \n {} \n".format(new_hand))
            print("Dealers Show Card: {} \n".format(dealer_hand[0][0]))
            # print("Dealers Cards: {} \n".format(dealer_hand))

            # print("\n Player Card1 value \n {} \n".format(card1_value))
            # print("\n Player Card2 value \n {} \n".format(card2_value))

            dealer_cardvalue = []
            dealer_cardvalue.append(dealer_hand[0][0][0])
            # print("\n Dealer Card value \n {} \n".format(dealer_cardvalue))
            # print("\n Type: \n {} \n".format(type(dealer_cardvalue)))

            # Offer Insurance if Dealer shows 10 or Ace
            # IF statements are not properly checking item in list
            for index in dealer_cardvalue:
                # print(type(index))
                # print(index)
                if (
                    index == "Ace"
                    or index == "Jack"
                    or index == "Queen"
                    or index == "King"
                    or index == "10"
                ):

                    insurance = input("Would you like insurance? [Y / N]")
                    if (
                        insurance != "Y"
                        or insurance != "y"
                        or insurance != "N"
                        or insurance != "n"
                    ):
                        print("Invalid Input: Enter Y for Yes or N for No.\n")
                        insurance = input("Would you like insurance? [Y / N] ")
                        # print("\nSuccess!")
                        # print(insurance)
                    if insurance == "Y" or insurance == "y":
                        insurance_wager = int(input("Enter Insurance Wager:"))
                        score = score - insurance_wager
                        print(
                            "Wager: {} \nCurrent Balance: {} ".format(
                                insurance_wager, score
                            )
                        )
                        print("\nSuccess!")
                    else:
                        print("No insurance.")
                else:
                    print("Goodluck!")
            sleep(1)
