#!/usr/bin/env python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- 
#
# simpleguessinggame.py
# Copyright (C) 2017 sherif <sabdelhay@gmx.com>
# 
# SimpleGuessingGame is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# SimpleGuessingGame is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

from random import randrange

# Ask the user to enter an integer number
# Validate it is an integer number
# make a loop to check the entered number is matching or not

randNum = int(randrange(11))
guessed_number = 0

while True:
    try:
        guessed_number = int(input("Enter a number between 1 and 10: "))
    except ValueError:
        print("Please enter a valid int number")
    except:
        print("Unknown error")

    # print a message says "you won" or "try again"
    if((guessed_number > 0) and (guessed_number == randNum)):
        print("You won!")
        break
    else:
        print("Wrong guess or try again!")
        break