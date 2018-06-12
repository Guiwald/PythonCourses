print("...rock...\n...paper...\n...scissors...\n")
player1choice = input("Player 1, enter your choice\n")
player2choice = input("Player 2, enter your choice\n")

if player1choice == player2choice:
	print("That's a tie!")

elif player1choice == "rock":
	
	if player2choice == "paper":
		print("Player 2 wins!")
	else: 
		print("Player 1 wins!")

elif player1choice == "paper":
	
	if player2choice == "scissors":
		print("Player 2 wins!")
	else: 
		print("Player 1 wins!")

else:
	
	if player2choice == "rock":
		print("Player 2 wins!")
	else: 
		print("Player 1 wins!")