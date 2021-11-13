from random import randint
from components import winlose, choices

# add function
def winner():
	# compare the two
	if choices.CPU == choices.player:
		# tie - nothing else to compare, exit
		print("Whoops! A tie! Try again!")

	elif choices.player == "rock":
		if choices.CPU == "paper":
			print("===you lose!===")
			choices.playerslives = choices.playerslives -1
		else:
			print("***you win!***")
			choices.CPUlives = choices.CPUlives - 1

	elif choices.player == "paper":
		if choices.CPU == "scissors":
			print("===you lose!===")
			choices.playerslives = choices.playerslives -1
		else:
			print("***you win!***")
			choices.CPUlives = choices.CPUlives - 1

	elif choices.player == "scissors":
		if choices.CPU == "rock":
			print("===you lose!===")
			choices.playerslives = choices.playerlives -1
		else:
			print("***you win!***")
			choices.CPUlives = choices.CPUlives - 1