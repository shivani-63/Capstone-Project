"""Runs a higher or lower card game
Allows the user to input a guess as to whether the next card 
will be higher or lower than the previous. Tallies a score for each turn played"""
import random
import time

SUITS = ['\u2665','\u2666','\u2660','\u2663']
# [ hearts, diamonds, spades, clubs]
NUMBERS = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
DECK = []

def shuffle_deck():
    """Forms and shuffles a deck of cards"""
    card_value = 0
    for number in NUMBERS:
        card_value +=1
        for suit in SUITS:
            DECK.append([f'{number} of {suit}',card_value])
            random.shuffle(DECK)
    return DECK


def user_input():
    """Allows the used to input their guess"""
    guess = input('Will the next card be higher or lower?')
    return guess


def correct_guess(score,next_card):
    """Prints the next card, and updates the score if the users guess is correct"""
    print(f'The next card is {next_card[0]}')
    short_pause()
    print(f'Correct, your score is now {score}!')
    return score


def incorrect_guess(score,next_card):
    """Prints the next card to evaluate the user guess,
    if incorrect, prints the final score"""
    print(f'The next card is {next_card[0]}')
    short_pause()
    print(f'Sorry, that was incorrect! Your final score is {score}')
    return score


def same_value_card(next_card):
    """Deals with if the card is the same - simply snaps and 
    continues with the next card, no point updates/deductions"""
    short_pause()
    print(f'The card was {next_card[0]}, Snap!')


def short_pause():
    """allows a break between printed statements"""
    time.sleep(0.5)


def game_loop():
    """The bulk of the game loop, 
    evaluates the cards and the user input against one of the listed outcomes"""
    print('\u2663 \u2660 \u2666 \u2665  Welcome to this higher or lower card game \
\u2665 \u2666 \u2660 \u2663\
\nThe aim of the game is to guess whether the next card drawn will be higher\
or lower than the previous one\nSee how many you can consecutively guess correctly!\
\nYou may exit the game at any time, by typing the word exit.\nEnjoy and good luck!')

    current_card = DECK.pop(0)
    score = 0
    while True:
        short_pause()
        print(f'The current card is {current_card[0]}')
        next_card = DECK.pop(0)
        short_pause()

        guess = user_input()
        short_pause()

        if guess.lower() == 'higher' and current_card[1] < next_card[1] \
            or guess.lower() == 'lower' and current_card[1] > next_card[1]:
            current_card=next_card
            score+=1
            correct_guess(score,next_card)

        elif (guess.lower() == 'higher' \
              or guess.lower() == 'lower') and current_card[1] == next_card[1]:
            same_value_card(next_card)

        elif guess.lower() == 'higher' and current_card[1] > next_card[1] \
            or guess.lower() == 'lower' and current_card[1] < next_card[1]:
            incorrect_guess(score,next_card)
            break

        elif guess.lower() == 'exit':
            print(f'Thank you for playing, your final score was {score}')
            break

        else:
            print('Invalid input: Please type either "higher" or "lower":')

shuffle_deck()
game_loop()
