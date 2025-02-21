import random
import time

moves = ["rock", "paper", "scissors", "lizard", "spock"]
wins = {"rock":["scissors", "lizard"], "paper": ["rock","spock"], 
        "scissors": ["paper", "lizard"], "lizard": ["spock", "paper"], 
        "spock": ["rock", "scissors"]}

cpu = random.choice(moves)
while True:
    player = input("rock paper scissors lizard spock\nchoose from the above\n>")
    if player in moves:
        break
    else:
        print("please choose from the available choices")
        time.sleep(2)

for x in wins:
    if cpu == x:
        if player in wins[x]:
            print("rock -- rock")
            time.sleep(0.5)
            print("paper -- paper")
            time.sleep(0.5)
            print(f"cpu:{cpu} -- player:{player}")
            time.sleep(0.5)
            print(f"{cpu} beats {player}\ncpu wins!!!")
            break
    elif player == x:
        if cpu in wins[x]:
            print("rock -- rock")
            time.sleep(0.5)
            print("paper -- paper")
            time.sleep(0.5)
            print(f"cpu:{cpu} -- player:{player}")
            time.sleep(0.5)
            print(f"{player} beats {cpu}\nplayer wins!!")
            break
    elif player == cpu:
        print("rock -- rock")
        time.sleep(0.5)
        print("paper -- paper")
        time.sleep(0.5)
        print(f"cpu:{cpu} -- player:{player}")
        time.sleep(0.5)
        print("DRAW!")
        break
    else:
        continue

