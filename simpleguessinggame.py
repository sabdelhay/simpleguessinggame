#!/usr/bin/env python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- 
# simpleguessinggame.py
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
        print("Wrong guess try again!")
        break
