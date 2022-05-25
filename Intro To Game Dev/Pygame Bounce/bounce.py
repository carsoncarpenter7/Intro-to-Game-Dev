#! /usr/bin/env python3
# Carson Carpenter
# CPSC 386-02
# 2022-04-24
# carson.carpenter7@csu.fullerton.edu
# @carsoncarpenter7
#
# Lab 05-00
#
# This my Pygame game program with of bouncing balls
#
# python3 -m venv env
# source env/bin/activate
# pip install -r requirements.txt
#
# black bounce.py 
# pylint bounc.py
#
"""
Imports the Bounce demo and executes the main function.
"""

import sys
from game import game

if __name__ == "__main__":
    NUM_BALLS = 5
    if len(sys.argv) > 1:
        NUM_BALLS = int(sys.argv[1])
    if NUM_BALLS >= 50:
        NUM_BALLS = 49
    if NUM_BALLS < 3:
        NUM_BALLS = 3
    VIDEO_GAME = game.BounceDemo(NUM_BALLS)
    VIDEO_GAME.build_scene_graph()
    VIDEO_GAME.run()
