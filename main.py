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

map = [rock, paper, scissors]

computer_random_choice = random.randint(0,2)

comp_choice = map[computer_random_choice]

print("Welcome to Rock, Paper, Scissors!")
print("It's you vs the computer.")
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n")

if int(user_choice) > 2 or int(user_choice) < 0:
    print("That is not a choice, automatic GAME OVER.")
else:
    print(map[int(user_choice)])

    print("Computer chose:")
    print(comp_choice)

    if int(user_choice) == 0 and computer_random_choice == 2:
        print("You win!")
    elif computer_random_choice == 0 and int(user_choice) == 2:
        print("Computer wins.")
    elif int(user_choice) > computer_random_choice:
        print("You win!")
    elif int(user_choice) == computer_random_choice:
        print("It's a draw.")
    else:
        print("Computer Wins.")