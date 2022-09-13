import random
from art import logo
print(logo)
# TODO 1: get 1 random number to be guessed :DONE

# TODO 2: ask the user to choose a game level 'easy' 5 or 'hard'10 :DONE

# TODO 3: check user's answer if it correct or high or low :DONE

# TODO 4: repet TODO 3 until all atempts over :DONE

# TODO 5: print final result :DONE

# TODO 6: add logo and greeting statmenet :DONE

def get_random_number():
    """ Returns a random number between 1 ~ 100 """
    return random.randint(1,100)

def check_value(user_guess,flag):
    """Returns 0 if user guess is uqual to flag, -1 if it's less than flag, 1 if it's grater than flag """
    if user_guess == flag:
        return 0
    elif user_guess > flag:
        return 1
    else:
        return -1

def guess():
    
    flag = get_random_number()
    user_guess = 0
    print("Welcom to 'Guess Me' game")
    print("Guess a number between 1 ~ 100")
    game_level = input("What Difficlulty level to play with 'easy' or' hard': ")
 
    if (game_level != "easy") and (game_level != "hard"):
        print ("Wrong choice!")
        return
    
    elif game_level == "easy":
        attempts = 10
    
    else:
        attempts = 5
    
    ctr = 0
    check_me = check_value(user_guess,flag)

    while (ctr < attempts ) and (check_me != 0):
        
        print(f"\nYou have {attempts - ctr} attempts left")
        
        user_guess = int(input("Enter your guess: "))
        ctr+=1
        check_me = check_value(user_guess,flag)
        
        if check_me == 0:
            print(f"\nYou won! with {ctr} attempts")
        
        elif check_me == 1:
            print("    \n[Too high]")
        
        else:
            print("    \n[Too low]")
            
        
    if check_me != 0:
        print("\nSorry You lost")
    print(f"[{flag}] is the correct answer")

guess()
