from components import choices

def winorlose(status):
    print("you" + status)

    choice = input("*That was fun! Want to play again? Press y/n?*")

    global playerslives
    global CPUlives
    global player

    if choice == "n":
    	print("=====bye=bye!=====")
    	exit()
    elif choice == "y":
    	CPUlives = 5
    	playerslives = 5
    	player = False