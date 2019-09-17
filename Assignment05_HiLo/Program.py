# Timothy Tarca 
# 9/17/19
# Assignment05_HiLo

import random


# Explains the how the game works	
print("Guessing Game\nHow it works:\nThe computer will generate a random whole number between 1 and 50.\nThe player will have 5 turns to guess the correct whole number.\nThe computer will the player if the entered number is too low or high.\nThis process will repeat until the player has either won or ran out of turns.\n")

# Method that runs the game
# Prompts uesr for input and compares it with computer's number
def HiLo(turnNum):
	if turnNum :
		
		# Tells the user which turn they are on
		if turnNum > 1:
			print("You have " + str(turnNum) + " turns left!")
		else:
			print("You're on your last turn! Guess Carefully!")
		turnNum = turnNum - 1
		
		# Determines is user's number matches the computer's
		userin = int(input("Guess a number: "))
		if userin == comNum:
			print("You Win!!")
		elif userin < comNum:
			print("Your number is too low!\n")
			HiLo(turnNum)
		else:
			print("Your number is too high!\n")
			HiLo(turnNum)
	else:
		print("You ran out of turns!\nGame Over")
		
# Creates a random number
comNum = random.randrange(1, 51)
# Starts the game
HiLo(5)
