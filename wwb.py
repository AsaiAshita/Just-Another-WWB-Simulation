#!/usr/bin/env python

import random #for generating random numbers to simulate the dice's roll
import sys #for managing command line arguments

__author__ = "AsaiAshita"
__copyright__ = "Copyright 2025, AsaiAshita"
__credits__ = ['AsaiAshita']
__license__ = "GNU GPL 2.0"
__version__ = "1.0"


def WBB():
    """
    The function simulates the functioning of WBB: it initializes a turn count and the position of the player, then, until the poition is not 101 (so the Finish square)
    it randomly generates a value between 1 and 6, simulating the throw of a dice: if the result is not 5, nothing happens; if it is, then the player moves one position
    and then another number is randomly generated between 1 and 6. If the result is 5, the player remains in the new position, else it is brought back to position 0.
    Every time a new position is reached, a string gets printed saying the index of the new position and the number of turns necessary to reach it.
    The function returns only if the player succeeds in arriving at position 101, thus winning the game.
    """
    turn = 1 #counts the number of turns (and it will be the reason why, at a certain point, either the program will crash or there will be an integer overflow)
    position = 0 #goes from 0 to 101, where 0 is Start, 101 is Finish, for a total of 102 possible positions (follows the Boardgamegeek description of the game)
    dice = 0 #result of the dice
    furthest_position = 0 #furthest position reached on the board
    while position != 101:
        dice = random.randint(1,6) #generate random integere between 1 and 6 (NB: due to the nature of PRG, it does not perfectly simulate a real throw, as it is impossible to simulate true randomness)
        if dice == 5: #if the result of the dice is equal to 5, move forward one position and roll the dice again: if it is not 5, return to the Start position. Else, remain on the new position
            position = position + 1
            dice = random.randint(1,6)
            if dice != 5:
                if position != 0:
                    position = 0
            else:
                if position > furthest_position: #prints how many turns were needed to reach the new best position and updates furthest_position
                    print("Player reached position ", position, " in ", turn, " turns!")
                    furthest_position = position
        turn = turn + 1 #increase turn counter
    print("Congratulations! You have won WBB in a total of " + turn + " turns!") #if someone succeeds in printing this, it probably has exhausted every single ounce of luck it had in its entire life
    return

def WBB_2():
    """
    A variation of WBB that simulates the game described in the WBB function, but with two players. At every turn, both players execute the same actions of WBB, but, if both of them find
    themselves in the same position and that position is not 0 (aka the Start position), the position of both players is reset to 0.
    Whenever a player reaches an unexplored position, its index gets printed, along with the index of the player that reached it and the number of turns it took (this means that, the first time player 1
    visits position 1, it prints its index, the position and the number of turns necessary to do so: when player 2 visits position 1 for the first time, it will also print
    the same as above).
    The function returns whenever one of the two players reaches position 101.
    """
    turn = 1 #counts the number of turns (and it will be the reason why, at a certain point, either the program will crash or there will be an integer overflow)
    position = 0 #goes from 0 to 101, where 0 is Start, 101 is Finish (follows the Boardgamegeek description of the game), represents player 1. If it is the same as position_p2, then both players get sent back to the start
    position_p2 = 0 #goes from 0 to 101, where 0 is Start, 101 is Finish (follows the Boardgamegeek description of the game), represents player 2. Same as above
    dice = 0 #result of the dice
    furthest_position = 0 #furthest position reached on the board by player 1
    furthest_position_p2 = 0 #furthest position reached on the board by player 2
    while position != 101 or position_p2 != 101:
        for i in range(1,3): #we simulate the player 1 turn and then the player 2 turn (if i==1, it is player 1's turn, if i==2, it is player 2's turn)
            dice = random.randint(1,6) #generate random integere between 1 and 6 (NB: due to the nature of PRG, it does not perfectly simulate a real throw, as it is impossible to simulate true randomness)
            if dice == 5: #if the result of the dice is equal to 5, move forward one position and roll the dice again: if it is not 5, return to the Start position. Else, remain on the new position
                if i==1:
                    position = position + 1
                else:
                    position_p2 = position_p2 + 1
                dice = random.randint(1,6)
                if dice != 5:
                    if i==1:
                        if position != 0:
                            position = 0
                    else:
                        if position_p2 != 0:
                            position_p2 = 0
                else:
                    if position != 0 and position_p2 != 0 and position == position_p2: #if both players end up on the same space and it is not the start, they both get sent back to the start
                        position = 0
                        position_p2 = 0
                    else:
                        if i==1:
                            if position > furthest_position: #prints how many turns were needed to reach the new best position and updates furthest_position
                                print("Player ", i, " reached position ", position, " in ", turn, " turns!")
                                furthest_position = position
                        else:
                            if position_p2 > furthest_position_p2: #prints how many turns were needed to reach the new best position and updates furthest_position
                                print("Player ", i, " reached position ", position_p2, " in ", turn, " turns!")
                                furthest_position_p2 = position_p2
        turn = turn + 1 #increase turn counter
    #check who won the game and print the message accordingly
    winner = 0
    if (position == 101):
        winner = 1
    else:
        winner = 2
    print("Congratulations! Player ", winner, " has won WBB in a total of " + turn + " turns!") #if someone succeeds in printing this, it probably has exhausted every single ounce of luck it had in its entire life
    return

def main():
    #just a series of checks on the presence and number of command line arguments and a textual interface to make the user choose what simulation to execute
    arg_number = len(sys.argv) #number of command line arguments (needs to be at least 1 because... well... how do you execute the script otherwise?)
    if arg_number > 2: #more arguments than the ones this script is willing to accept
        print("Usage: wbb.py [n/f]\n"
        "where n can be absent, but, if present, needs to be either 1 or 2\n"
        "and f can only be equal to -h")
        exit(1)
    if arg_number == 1: #no additional command line argument has been given, thus we need to make the user choose what simulation to execute
        print("Hello and welcome to Just Another WBB Simulation!\n"
        "The following script offers two possible simulations: a single player one and a two player one.\n"
        "If you wish to simulate the first scenario, please input 1; otherwise, please input 2.")
        choice = input()
        if len(choice) > 1: #number needs to be 1 or 2, no reason why choice should be longer than 1. Could be condensed with the next check, but it was decided to keep them separated
            print("Wrong input, please try again")
            exit(2)
        elif choice not in {"1", "2"}: #again, number needs to be 1 or 2
            print ("Wrong input, please try again")
            exit(3)
        else:
            if choice == "1": #if the choice was 1, we execute the sigle player version...
                WBB()
                return 0
            else: #...else we execute the two player version
                WBB_2()
                return 0
    if arg_number == 2: #this means that a command line value was given, we need to check what it is
        if sys.argv[1] == "1": #if it was 1, we know we need to simulate the single player version
            WBB()
            return 0
        elif sys.argv[1] == "2": #if it was 2, we know we need to imulate the two player version
            WBB_2()
            return 0
        elif sys.argv[1] == "-h": #if it was -h, it means the user wants to bring up the instructions for the usage of the script
            print("Usage: wbb.py [n/f]\n"
            "n: {1,2, none}\n"
            "If n = 1, the simulation for the single player version will be launched.\n"
            "If n = 2, the simulation for the two player version will be launched.\n"
            "If n is absent, you will be asked what simulation would you like to execute.\n"
            "\n"
            "f: {-h}\n"
            "If f = -h, you will be brought to the help page, with instrunctions regarding how to execute this script")
            exit(0)
        else: #if the user input something else, we don't accept it, bring up a succint version of the -h page and we exit
            print("Usage: wbb.py [n/f]\n"
            "where n can be absent, but, if present, needs to be either 1 or 2\n"
            "and f can only be equal to -h")
            exit(1)
    return 0 #should never be seen (in theory)

main()
