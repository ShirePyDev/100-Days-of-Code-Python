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
user_action = input("What do you choose? Rock, Paper, Scissors: \n")

possible_action = ["Rock", "Paper", "Scissors"]

computer_action = random.choice(possible_action)

user_action = user_action.capitalize()

if user_action not in possible_action:
        print("You choose an invalid choice. You loose!")
elif  user_action == computer_action:
        print("It's draw!!!")
elif (user_action == "Rock" and computer_action == "Scissors" ) or \
     (user_action == "Scissors" and computer_action == "Paper" ) or \
     (user_action == "Paper" and computer_action == "Rock" ):
        print(f"You win! ")
else:
    print("Computer Wins!!")