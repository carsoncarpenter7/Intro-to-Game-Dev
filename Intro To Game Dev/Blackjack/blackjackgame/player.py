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
import pickle
import random

# import stat
from blackjackgame import cards


class Player:
    """Example Player class for a game."""

    def __init__(self, name, order, score=10000):
        """Init a player with a name and a score."""
        self._name = name
        self._score = score
        self._order = order
        self._id = random.randint(1, 100)

    @property
    def name(self):
        """Return the player's name"""
        return self._name

    @property
    def order(self):
        """Return the player's order"""
        return self._order

    @property
    def score(self):
        """Return the player's score."""
        return self._score

    @score.setter
    def score(self, points):
        """Add points to the player's score."""
        self._score += points

    def __str__(self):
        """Convert the Player to a printable string."""
        return f"{self._name}"

    def __repr__(self):
        """Python representation."""
        return f"Player(name: {self._name}, score = {self._score})"

    @staticmethod
    def to_file(pickle_file, players):
        """Write the list players to the file pickle_file."""
        with open(pickle_file, "wb") as file_handle:
            pickle.dump(players, file_handle, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def from_file(pickle_file):
        """Read the contents of pickle_file,
        decode it, and return it as players."""
        with open(pickle_file, "rb") as file_handle:
            players = pickle.load(file_handle)
        return players


class Dealer:
    """Dealer Class"""

    def __init__(self, n_decks=1):
        self._deck = cards.Deck()
        for _ in range(n_decks - 1):
            self._deck.merge(cards.Deck())

    @staticmethod
    def none():
        """Fixing pylint errors"""
        return

    @staticmethod
    def none1():
        """Fixing pylint errors"""
        return

    # @staticmethod
    # def deal_to(self, player):
    #     """ Deal to player"""
    #     return player

    # @staticmethod
    # def check_shoe(self):
    #     """Check to see if the dealer has reached the cut\
    #         card, if so re-prepare the shoe."""
    #     return


# Pickle Example for score saving
# def main():
#     """Main function; entry point."""
#     names = [
#         'Groucho',
#         'Harpo',
#         'Chico',
#         'Zeppo',
#         'Buster',
#         'Charlie',
#         'Stan',
#         'Oliver',
#     ]
# player_list = [
#     Player(random.choice(names),
#            random.randint(0, 25)) for _ in range(10)
# ]
#     print('This is what is going into the pickle file:')
#     print('\n'.join(map(str, player_list)))
#     to_file('players.pckl', player_list)
#     # Set to None to prove we are getting the data from the file.
#     player_list = None
#     player_list = from_file('players.pckl')
#     print('This is what we got back out of the pickle file:')
#     print('\n'.join(map(str, player_list)))


# if __name__ == '__main__':
#     main()
