import art
import random


card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

def drawing_card(card_needed):
    cards = []
    for _ in range(card_needed):
        cards.append(random.choice(card))
    print(cards)
    return cards

while True:
    choice = input("So, Do you want to play a game of Blackjack?(y/n) ").lower()

    if choice == 'y':
        player_card = drawing_card(2)
        dealer_card = drawing_card(1)

        player_choice = input("Do you want to 'HIT' or 'HOLD? (hit/hold) ").lower()

        if player_choice == 'hit':
            pass
        elif player_choice == 'hold':
            pass
    elif choice == 'n':
        print(art.text2art("Goodbye"))
        break
    else:
        print("INVALID choice!!!")
        continue


