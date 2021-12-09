import random

CHOICES = 'rps'


def get_player_choice():
    """Get user input and validate it is one of the choices above"""
    player_choice = None
    while player_choice is None:
        print("Please enter your choice: ")
        player_choice = input('Choices: \n(R)ock \n(P)aper \n(S)cissors \n\nPick: ')
        if player_choice.lower() not in CHOICES:
            player_choice = None
    return player_choice.lower()


def get_computer_choice():
    """Have the computer pick one of the valid choices at random"""
    computer_choice = random.randint(0, 2)
    computer_choice = CHOICES[computer_choice]
    return computer_choice


def is_draw(player_choice, computer_choice):
    """Check if game was a draw"""
    if player_choice == computer_choice:
        return True


def print_winner(player_choice, computer_choice):
    """Check to see who won"""
    if player_choice == 'r' and computer_choice == 's':
        print('Player wins!')
    elif player_choice == 's' and computer_choice == 'p':
        print('Player wins!')
    elif player_choice == 'p' and computer_choice == 'r':
        print('Player wins!')
    else:
        print('Computer wins!')
        print('%s beats %s' % (computer_choice, player_choice))



"""play the game"""
s="y"
while s=='y':
    print("Hello user! Welcome to rock paper scissor game")
    print("The rules of the game are: ")
    print(""" Rock smashes scissors\n Scissors smashes paper \n Paper smashes rock\n""")
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    if is_draw(player_choice, computer_choice):
        print("It's a draw, both players picked %s: " % player_choice)
    else:
        print("Computer picked: %s" % computer_choice)
        print("Player picked: %s" % player_choice)
        print_winner(player_choice, computer_choice)
    print("Do you want to play another time?")
    print("If you want to play press y or n")
    s=input()

