#Choosing random number from list
def deal_card():
    return random.choice(cards)
#calculating score if score>21 and 11 in the deck then replacing 11 with 1
def calculate_score(l):
    score=sum(l)
    if len(l) == 2 and score == 21:
        return 0
    elif (11 in l) and score > 21:
        l[l.index(11)] = 1
        return sum(l)
    else:
        return score
# Comparing player score and dealer score
def compare_score(player_score,dealer_score):
    if player_score == dealer_score:
        print(f"Its Draw user score is :{player_score}, dealer score :{dealer_score}")
        return False
    elif dealer_score == 21:
        print(f"Computer Got BlackJack ,User loses")
        return False
    elif player_score == 21:
        print(f"User Got BlackJack ,User Wins")
        return False
    elif player_score > 21:
        print(f"user : {user_score} got bust  ,computer wins {dealer_score}")
        return False
    elif dealer_score > 21:
        print(f"computer {dealer_score} got bust ,user : {user_score} wins")
        return False
    else:
        if player_score > dealer_score:
            print(f"Your score {player_score},Player wins ")
            return False
        else:
            print(f"Your score {player_score}, Computer :{dealer_score} wins ")
            return False
# Driver Code
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
p=input("Do you want to play BlackJack Yes type 'y' Or No type 'n': ").lower()
if p == 'y':
    play = True
else:
    play = False
    print("Good Bye")

while play:    
    user_cards=[]
    computer_cards=[]
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    print(f"User Deck {user_cards},score:{sum(user_cards)}")
    print(f"Dealer Deck {computer_cards[0]}")
    user_cal = calculate_score(user_cards)
    comp_cal = calculate_score(computer_cards)
    if user_cal == 0:
        print("Player Got BlackJack,Player Wins")
        break
    elif comp_cal == 0:
        print("Computer Got BlackJack,Player Wins")
        break
    elif user_cal > 21:
        print(f"Game Over,{user_cal} Bust")
        break
    else:
        draw_card=input(f"Your Score is {user_cal},Do you want to draw a card 'y' or 'n' :")
        if draw_card =="y":
            user_cards.append(deal_card())
            
    while sum(computer_cards)<17:
        computer_cards.append(deal_card())
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)
    play=compare_score(user_score,computer_score)
