#look at adding a file for leaderboard
#can add an option to re-play the game 
#change final else statement to a break clause

import random,time

suits = ['\u2665','\u2666','\u2660','\u2663']
# [ hearts, diamonds, spades, clubs]
numbers = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
deck = []

def shuffle_deck():
    card_value = 0
    for number in numbers:
        card_value +=1
        for suit in suits:
            deck.append([f'{number} of {suit}',card_value])
            random.shuffle(deck)
    return deck

def display_leaderboard():
    leaderboard_file = open('leaderboard.txt','r')
    top_players = leaderboard_file.read().splitlines()
    for player in top_players:
        player_info = player.split(',')
        name = player_info[0]
        score = int(player_info[1])
        print(f'Player name: {name} got {score} points')
    leaderboard_file.close()

def add_score_to_leaderboard(score):
    short_pause()
    name = input('Thank you for playing, please type your name so you can be added to the leaderboard: ')
    with open('leaderboard.txt', 'a') as a_writer:
        a_writer.write(f'\n {name}, {score}')

def user_input():
    guess = input('Will the next card be higher or lower?')
    return guess

def correct_guess(score,next_card):
    print(f'The next card is {next_card[0]}')   
    short_pause()
    message = print(f'Correct, your score is now {score}!')
    return message

def incorrect_guess(score,next_card):
    print(f'The next card is {next_card[0]}')
    short_pause()
    print(f'Sorry, that was incorrect! Your final score is {score}')
    add_score_to_leaderboard(score)
    display_leaderboard()

def same_value_card(next_card):
    short_pause()
    print(f'The card was {next_card[0]}, Snap!')

def short_pause():
  time.sleep(0.5)

def exit(score):
    print(f'Thank you for playing, your final score was {score}')

def game_loop():
    print('\u2663 \u2660 \u2666 \u2665  Welcome to this higher or lower card game \u2665 \u2666 \u2660 \u2663 \nThe aim of the game is to guess whether the next card drawn will be higher or lower than the previous one. \nSee how many you can consecutively guess correctly! \nYou may exit the game at any time, by typing the word exit. \nEnjoy and good luck!')
    current_card = deck.pop(0)
    score = 0
    while True:
        short_pause()
        print(f'The current card is {current_card[0]}')
        next_card = deck.pop(0)
        short_pause()

        guess = user_input()
        short_pause()

        if guess.lower() == 'higher' and current_card[1] < next_card[1] or guess.lower() == 'lower' and current_card[1] > next_card[1]:
            current_card=next_card
            score+=1
            correct_guess(score,next_card)

        elif (guess.lower() == 'higher' or guess.lower() == 'lower') and current_card[1] == next_card[1]:
            same_value_card(next_card)

        elif guess.lower() == 'higher' and current_card[1] > next_card[1] or guess.lower() == 'lower' and current_card[1] < next_card[1]:
            incorrect_guess(score,next_card)
            break

        elif guess.lower() == 'exit':
            exit(score)
            break

        else:
            print('Invalid input: Please type whether you think the next card will be higher or lower:')


shuffle_deck()
game_loop()

