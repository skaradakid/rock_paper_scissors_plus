import random
import time

moves = ["rock", "paper", "scissors", "lizard", "spock"]
wins = {"rock":["scissors", "lizard"], "paper": ["rock","spock"], 
        "scissor": ["paper", "lizard"], "lizard": ["spock", "paper"], 
        "spock": ["rock", "scissors"]}

cpu = random.choice(moves)
player = input("rock paper scissors lizard spock\nchoose from the above\n>")

for x in wins:
    if cpu == x:
        if player in wins[x]:
            print("rock -- rock")
            time.sleep(1)
            print("paper -- paper")
            time.sleep(1)
            print("scissor -- scissor")
            time.sleep(1)
            print(f"cpu:{cpu}\n player:{player}")
            time.sleep(1)
            print(f"{cpu} beats {player}\n well done cpu!!")
            break
    elif player == x:
        if cpu in wins[x]:
            print("rock -- rock")
            time.sleep(1)
            print("paper -- paper")
            time.sleep(1)
            print("scissor -- scissor")
            time.sleep(1)
            print(f"cpu:{cpu}\n player:{player}")
            time.sleep(1)
            print(f"{player} beats {cpu}\n well done player!!")
            break
    else:
        print("rock -- rock")
        time.sleep(1)
        print("paper -- paper")
        time.sleep(1)
        print("scissor -- scissor")
        time.sleep(1)
        print(f"cpu:{cpu}\n player:{player}")
        time.sleep(1)

