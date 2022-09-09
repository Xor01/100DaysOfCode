from os import system

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

def get_winner_info(list):
    winner_name = ""
    winner_bid = 0
    for i  in range(len(list) ):
        if list[i][1] > winner_bid:
            winner_name = list[i][0]
            winner_bid = list[i][1]
    print(f"\"{winner_name}\" has won with a bid of ${winner_bid}") 

program_continue = "yes"

user_info = []

print("Welcom to the secret auction program")
while program_continue == "yes":

    name = input("What is your name: ")
    bid = int(input("What is your bid:$"))
    user = [name,bid]
    user_info.append(user) 
    chocice = input("Are there any other bidders ? 'yes or 'no': ")
    
    if chocice.lower() == "yes":
        system("cls")
    else:
        get_winner_info(user_info)
        program_continue = "no"