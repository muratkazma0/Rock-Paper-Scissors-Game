import random

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

game_images = [rock, paper, scissors]

user_choice = int(input('Which one do you choose? Rock = 0 | Paper = 1 | Scissors = 2\n '))
print('\nYour choice:')
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print('Computer chose:')
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print('You entered an invalid number. You lose!')
    
elif user_choice == 0 and computer_choice == 2:
    print('Congratulations! You win!')
    
elif computer_choice == 0 and user_choice == 2:
    print('Sorry. You lose!')

elif computer_choice > user_choice:
    print('Sorry. You lose!')
    
elif user_choice > computer_choice:
    print('Congratulations! You win!')
    
elif computer_choice == user_choice:
    print('It\'s a tie!')
