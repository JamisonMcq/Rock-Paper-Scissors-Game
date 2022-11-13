# Rock paper scissors game
import random

print('Welcome to Rock, Paper, Scissors game! We play best of 3.')
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

pictures = [rock, paper, scissors]
user_score = 0
computer_score = 0

while user_score < 2 and computer_score < 2:

	user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: '))

	if 0 <= user_choice < 3:
		print(f'You chose: {pictures[user_choice]}')

	computer_choice = random.randint(0,2)
	print(f'Computer chose: {pictures[computer_choice]}')
	if user_choice >= 3 or user_choice < 0:
		print('Invalid Number, You Lose!')
		computer_score +=1

	elif user_choice == 0 and computer_choice == 2:
		print('You Win!')
		user_score += 1

	elif computer_choice > user_choice:
		print('You Lose!')
		computer_score += 1

	elif computer_choice == user_choice:
		print('Draw')

	elif computer_choice == 0 and user_choice == 2:
		print('You Lose!')
		computer_score += 1

	elif computer_choice < user_choice:
		print('You Win!')
		user_score += 1

	print(f'\n--Score--\nYou: {user_score}\nComputer:{computer_score}\n--------\n')

if user_score > computer_score:
	print('You won the match!')

else:
	print('You lost the match!')