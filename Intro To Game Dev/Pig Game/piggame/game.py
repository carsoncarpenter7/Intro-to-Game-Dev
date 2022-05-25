#! /usr/bin/env python3
# Carson Carpenter
# CPSC 386-02
# 2022-03-07
# carson.carpenter7@csu.fullerton.edu
# @carsoncarpenter7
#
# Lab 02-00
#
# This the game program contents
#


"""This module contains the contents of PigGame"""


import time
import sys
from .die import Die
from .player import Player, ComputerPlayer


class PigGame:
    """Game Contents"""

    def __init__(self):
        """__init__"""
        self._die = Die()
        # new_score = self._die
        self._number_of_players = int(input("How many Players? "))
        self._players = []
        for index in range(self._number_of_players):
            self._order = index
            new_name = input("What is your Name? ")
            self._players.append(Player(new_name))
        # print('Current Players Scores: {} '.format(self._players))

    @staticmethod
    def none():
        """Fixing pylint errors"""
        return

    def run(self):
        """Computer Ai and Score counting conditions"""
        cp_index = 0
        total_score = []
        player1_total = 0
        while True:
            roll_die = self._die.roll()
            cp_player = self._players[cp_index]
            print("Current player is {} {}".format(cp_index, cp_player))
            print("You rolled {}".format(roll_die))
            new_score = roll_die
            total_score.append(new_score)
            print(total_score)
            if self._number_of_players == 1:
                print("A Computer AI will play against you")
                print("Current player is {} {}".format(cp_index, cp_player))
                print("You rolled {}".format(roll_die))
                new_score = roll_die
                total_score.append(new_score)
                new_score = Player(new_score)
                for index in range(0, len(total_score[::2])):
                    player1_total = player1_total + total_score[index]
                    # print("Total Score: {}".format(player1_total))
                if player1_total >= 30:
                    print("Congradulations! {} you Won!".format(cp_player))
                    sys.exit(0)
            else:
                while True:
                    roll_die = self._die.roll()
                    cp_player = self._players[cp_index]
                    print("Player is {} {}".format(cp_index, cp_player))
                    print("You rolled {}".format(roll_die))
                    new_score = roll_die
                    total_score.append(new_score)
                    print("{} score is {}".format(cp_player, player1_total))
                    time.sleep(2)
                    cp_index = (cp_index + 1) % self._number_of_players
                    for index in range(0, len(total_score[::2])):
                        player1_total = player1_total + total_score[index]
                    if player1_total >= 30:
                        print("Congradulations! {} you Won!".format(cp_player))
                        sys.exit(0)
            if self._number_of_players > 5:
                print(ComputerPlayer)
