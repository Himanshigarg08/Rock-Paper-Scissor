import random

def play():
    user=input("What's ur choice? 'r' for rock, 'p' for paper and 's' for scissor.\n")
    Computer=random.choice(['r','p','s'])
    if user==Computer:
        return "It's a tie!!"
    if winner(user,Computer):
        return "You won!!"
    return "You Lost!"


def winner(player,computer):
    #r>s,s>p,p>r
    if (player=='r' and computer=='s') or (player=='s' and computer=='p') or (player=='p' and computer=='r'):
        return True


print(play())
