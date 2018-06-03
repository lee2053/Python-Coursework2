#Jangwon Lee
#Individual HW #1

#----------------------------------------------------------------------------
#1.Write an algorithm for a Rock Paper Scissors game.

#Play rock, paper, scissors game.
#ask a user what he or she wants to enter either rock, paper, or scissors.
#make the computer choice either rock, paper, or scissors randomly.
#if the user enters rock and the computer chooses rock randomly, then they tied.
#if the user enters rock and the computer chooses paper randomly, then the computer won and the user lost.
#if the user enters rock and the computer chooses scissors randomly, then the user won and the computer lost.

#if the user enters paper and the computer chooses rock randomly, then the user won and the computer lost.
#if the user enters paper and the computer chooses paper randomly, then they tied.
#if the user enters paper and the computer chooses scissors randomly,then the user lost and the computer won.

#if the user enters scissors and the computer chooses rock randomly, then the user lost and the computer won.
#if the user enters scissors and the computer chooses paper randomly, then the user won and the computer lost.
#if the user enters scissors and the computer chooses scissors randomly,then they tied.

#if the user wants to stop this game, enters STOP. Then, the gave is over.

#---------------------------------------------------------------------------------------
#2.Write a program that takes a string as input.
#AbC123 would be printed out as 321CbA.

#create a function called reverse

def reverse():
    #take a string as an input from the user.
    string = input("Please enter the word: ")
    #make a variable named string to be printed out in reverse.
    string_reverse = string[::-1]
    return print(string_reverse)
#----------------------------------------------------------------------------------------
#3.Write a function that takes a one letter abbreviation for a day of the week and returns the full day.

#Create abbreviation dictionary.
abbreviation = {"M":"Monday", "T":"Tuesday", "W":"Wednesday", "R": "Thursday", "F":"Friday", "S":"Saturday","U":"Sunday"}


#create function called fullweek that takes a character.
def fullweek(char):
    #if the character user enters is in the abbreiviation dictionary,
    if char in abbreviation:
        #return the full day
        return abbreviation[char]
    #if the character user enters is not in the dictionary,
    else:
        #return couldn't find it.
        return "Could not find it."

#-------------------------------------------------------------------------------------
#4. Write a code to implement the Rock Paper Scissors game.

import random

#make a list of options for computer.
options = ["Rock", "Paper", "Scissors"]

while True:
    #make computer to choose either rock, paper, or scissors randomly
    computer = random.choice(options)
##    print(computer) check what computer chose.

    #make user enters his choice.
    player = input("Rock, Paper, Scissors? or STOP? ")
    #if player's choice and computer's choice are the same,
    if player == computer:
        #print Tie
        print("Tie!")
    #when player enters rock
    elif player == "Rock":
        if computer =="Paper":
            print("You lost")
        else:
            print("You win")
    #when player enters Scissors
    elif player == "Scissors":
        if computer == "Rock":
            print("You lost")
        else:
            print("You win")
    #when player enters paper
    elif player == "Paper":
        if computer =="Rock":
            print("You win")
        else:
            print("You lost")
    #when player enters STOP, loop is over.
    elif player == "STOP":
        break
    









