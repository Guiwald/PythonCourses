import os


max_attempt = 6
nb_loss = 0
os.system('clear')
name = input("please tell me your name\n")
while True:
	number = None
	guess = None
	counter = 1
	min_num = 0
	max_num = 100
	os.system('clear')
	print(f"Hi {name}.\nYou will need to solve this game in less than {max_attempt} attempts!\n")
	print(f"nb of win: 0 | nb of loss: {nb_loss}")
	for count in range(max_attempt):
		raw_guess = (input(f"Please choose a number between {min_num} and {max_num} (attempt number {counter})\n"))

		if raw_guess.isdigit():
			guess = int(raw_guess)
			if guess<= max_num and guess >= min_num:
				
				if max_num - guess < guess - min_num:
					number = min_num + ((guess - min_num)/2)
					max_num = guess - 1
					print("LOWER!")
					#print(number)
				else:
					number = guess + ((max_num - guess)/2)
					print("HIGHER!")
					min_num = guess + 1
					#print(number)
			else:
				key_pressed = input(f"Do you understand that {guess} is not between {min_num} and {max_num}? ")
				if key_pressed:
					input("That was a rhetorical question... \U0001F926")
				else:
					input("DO")
					key_pressed = input("YOU?")
		elif raw_guess:
			input(f"Wait... Is {raw_guess} a number!")
			input("I mean, the instructions are clear, aren't they?")
		else:
			input("OK you just lost 1 attempt by not typing anything... Well done...")
		counter += 1
	number = int(number)
	#print(f"min number: {min_num}\nmax number: {max_num}\nnumber: {number}")
	if max_num == min_num:
		if number != max_num:
			number += 1
	#if number == max_num:
	#	number -= 1	
	input(f"You're a lOSER, {name}! The correct number was {number}")
	replay = input("Do you want to play again ? :) (y/n)")
	nb_loss += 1
	if replay != "y":
		input(f"Wow... You lost {nb_loss} time!!!")
		break

