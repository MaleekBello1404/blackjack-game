import random
from replit import clear
from art import logo


def deal_card():
    """function chooses a random number from the list and returns the value"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(list_of_cards):
    """function checks the for some condition in the list with the variable that's defined in it"""
    if 11 in list_of_cards and len(list_of_cards) == 2:
        return 0
    if 11 in list_of_cards and sum(list_of_cards) > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)

    return sum(list_of_cards)

def compare(user_score, computer_score):
    """Function checks for the player with the highest score"""
    if user_score == computer_score:
        return "You and computer have the same score, It's a draw"
    elif computer_score == 0:
        return "Computer score a blackjack, You Lose"
    elif user_score == 0:
        return "You scored a blackjack, You Won"
    elif user_score > 21:
        return "You went over, You Lose"
    elif computer_score > 21:
        return "Computer went over, you Win"
    elif user_score > computer_score:
        return "You won"
    else: 
        return "You lose"
        
def restart():
    """Function that'll execute when the player wants to play the game"""
    print(logo)
    user_cards = []
    computer_cards = []
    end_game = False
        
    
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    
    while end_game == False:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"Your numbers {user_cards} and total of {user_score}")
        print(f"Computer number is {computer_cards[0]} ")
        
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            end_game = True
        else:
            another_card = input("Type 'Yes' to draw another card or 'No' to pass: ").lower()
            if another_card == "yes":
                user_cards.append(deal_card())
            else:
               end_game = True
    
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f"Your Final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's Final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Will you like to play a game of blackjack? Type 'Yes' or 'No': ").lower() == "yes":
    clear()
    restart()    

    

    
