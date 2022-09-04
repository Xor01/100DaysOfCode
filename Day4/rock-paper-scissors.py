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

moves = [rock,paper,scissors]

userChoice = int(input("Enter 0 for rock, 1 for paper, 2 for scissors: "))

computerChoice = random.randint(0,2)

if(userChoice == computerChoice):
    print("Tie.")
elif (userChoice == 0) & (computerChoice == 1):
    print("You lost")
    
elif (userChoice == 0) & (computerChoice == 2):
    print("You won")
    
elif (userChoice == 1) & (computerChoice == 0):
    print("You won")

elif (userChoice == 2) & (computerChoice == 0):
    print("You lost")
    
elif (userChoice == 1) & (computerChoice == 2):
    print("You lost")

elif (userChoice == 2) & (computerChoice == 1):
    print("You won")
    
print(f"Your choice: {moves[userChoice]}\n")
print(f"Computer choice: {moves[computerChoice]}")