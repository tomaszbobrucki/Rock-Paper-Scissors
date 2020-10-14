# Write your code here
import random

options = ["scissors", "rock", "paper"]
opt_chosen = []

winning_cases = {
    'water': ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
    'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
    'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
}

"""
def who_wins(us, comp):
    if (us == options[0] and comp == options[2]
            or us == options[1] and comp == options[0]
            or us == options[2] and comp == options[1]):
        return us
    else:
        return comp


def who_wins(us, comp, opt2):
    if (us and comp) in options:
        if (us == options[0] and comp == options[2]
                or us == options[1] and comp == options[0]
                or us == options[2] and comp == options[1]):
            return us
        else:
            return comp
    num = opt2.index(us)
    opt3 = opt2[:num] + opt2[num + 1:]
    divide = len(opt3) // 2
    winners = opt3[:divide]
    losers = opt3[divide:]
    # print(losers)
    # print(winners)
    if comp in losers:
        return us
    else:
        return comp
"""


def who_wins(us, comp):
    if comp in winning_cases[us]:
        return us
    else:
        return comp


def game(user1, computer1, score):
    effect = who_wins(user1, computer1)
    if user1 == computer1:
        print(f"There is a draw ({user1})")
        score += 50
        return score
    elif effect == user1:
        print(f"Well done. The computer chose {computer1} and failed")
        score += 100
        return score
    elif effect == computer1:
        print(f"Sorry, but the computer chose {computer1}")
        return score


name = input("Enter your name: ")
file = open("rating.txt", "r")
print("Hello, " + name)
opt_user = input()
if not opt_user:
    opt_chosen = options[:]
else:
    opt_chosen = opt_user.split(",")

print("Okay, let's start")

rating = 0
all_data = [line.rstrip().split() for line in file]
for x in range(len(all_data)):
    if name == all_data[x][0]:
        rating = all_data[x][1]

while True:
    number = 0
    user = input()
    computer = random.choice(opt_chosen)
    if user == "!rating":
        print("Your rating: {}".format(rating))
    elif user == "!exit":
        print("Bye!")
        break
    elif user in opt_chosen:
        out = game(user, computer, number)
        rating = int(rating) + out
    else:
        print("Invalid input")

file.close()
