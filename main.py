from random import randint
from components import winlose, choices, results

# set up the game loop
while choices.player is False:
	choices.player = input("Please choose either Rock, Paper, or Scissors: ")
	choices.CPU = choices.weapon[randint(0, 2)]

	if choices.player == "exit":
		exit()
	else:
		# choosing a weapon
		print("you chose..." + choices.player)
		print("the CPU chose..." + choices.CPU)

		results.winner()

		print("player lives :" + str(choices.playerslives))
		print("CPU lives: " + str(choices.CPUlives))
		
		choices.player = False
