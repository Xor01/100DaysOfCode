from game_data import data
from art import logo, vs
from os import system
import random
print(logo)

def get_random_info():
    return random.choices(data)

def compare(choice,a,b):
    
    if a[0]['follower_count'] > b[0]['follower_count']:
        return choice == 'A'
    else:
        return choice == 'B'

def prevent_equality(a,b):
    """Used to prevent b from equaling a"""
    b = get_random_info()
    while(a == b):
        b = get_random_info()
    return b

def game():
    score = 0
    
    a = get_random_info()
    
    b = get_random_info()
    b = prevent_equality(a,b)
    while True:
        
        print(f"Compare A: {a[0]['name']}, {a[0]['description']}, from: {a[0]['country']}")
        
        print(vs)
        
        print(f"Against B: {b[0]['name']}, {b[0]['description']}, from: {b[0]['country']}")
        
        choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        
        if (compare(choice,a,b)) :
            a = b
            b = prevent_equality(a,b)
            score+=1
            system("cls")
            print(logo)
            print(f"You're right! Current score: {score}.\n")
            
        else:
            system("cls")
            print(logo)
            print(f"Sorry that's the wrong answer, your score: {score}")
            return 

game()