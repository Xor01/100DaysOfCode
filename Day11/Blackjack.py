# Blackjack Game
import random
from os import system
from art import logo


def get_card():
    """ Returns a random card from a card list """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def getScore(cards):
    """ Returns the sum of a card list """
    if (sum(cards) == 21) and (len(cards) == 2):
        return 0

    if sum(cards) > 21 and (11 in cards):
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, dealer_score):
    if user_score == dealer_score:
        return "It's a draw, you have the same score"

    elif user_score == 0:
        return "You won, you have a blackjack"

    elif dealer_score == 0:
        return "You lost, the dealer has a blackjack"

    elif user_score > 21:
        return "You lost, your score is higher than 21"

    elif dealer_score > 21:
        return "You won, the dealer's score is higher than 21 "

    elif user_score > dealer_score:
        return "You won, congrats"

    else:
        return "You lost, sorry"


def blackjack():
    is_game_over = False
    user_hand = []
    dealer_hand = []

    for _ in range(2):
        user_hand.append(get_card())
        dealer_hand.append(get_card())

    while not is_game_over:

        user_score = getScore(user_hand)
        dealer_score = getScore(dealer_hand)

        print(f"    Your hand: {user_hand} your score: {user_score}")
        print(f"Dealer's hand: {dealer_hand[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            draw = input("Enter 'd' to draw a card or 'p' to pass: ")
            if draw.lower() == 'd':
                user_hand.append(get_card())
            else:
                is_game_over = True
                while dealer_score < 17 and dealer_score != 0:
                    dealer_hand.append(get_card())
                    dealer_score = getScore(dealer_hand)

    print("-------------------------------------------------")
    print(f"Your final hand: {user_hand} your final score: {user_score}")
    print(f"Dealer's final hand: {dealer_hand} final dealer score: {dealer_score}")
    print(compare(user_score, dealer_score))


while input("Enter 'y' to play or 'n' to exit ").lower() == 'y':
    system("cls")
    print(logo)
    blackjack()
