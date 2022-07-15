import random


def play():
    print('Enter your choice')
    user = input('Rock(r), Paper(p) or Scissor(s)\n')
    computer = random.choice(['r', 'p', 's'])
    print('Computer:', computer)
    if user == computer:
        return "It's a tie"

    if is_win(user, computer):
        return 'Yay! you won.'

    return 'Oh! you lost'


def is_win(player, opponent):
    # r>s, s>p, p>r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


if __name__ == '__main__':
    print(play())
