# In this game user and computer has to guess each other's number
import random


# Part1: user will guess the number picked up by computer
def user_guess(end_range):
    random_number = random.randint(1, end_range)    # Computer will generate a random number
    guess = 0
    while guess != random_number:  # User will keep inputting the no. util it matches with computer generated no.
        guess = int(input('Enter a number:'))
        if guess < random_number:
            print('Incorrect, too low!')
        if guess > random_number:
            print('Incorrect, too high!')
    print(f'Yay! you have guessed the number {random_number} correctly!')


# Part2: computer will guess the correct number from user
def computer_guess(end_range):
    low, high = 1, end_range
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f'Is the {guess} correct? No, too high(H), too Low(L). Yes correct(C) : ').lower()
        if feedback == 'l':
            low = guess + 1
        elif feedback == 'h':
            high = guess - 1
    print(f'Yay! computer has guessed the number {guess} correctly!')


if __name__ == '__main__':
    print('User is guessing!')
    user_guess(10)
    print()
    print('Now computer will guess your number, think about a number!')
    computer_guess(20)

