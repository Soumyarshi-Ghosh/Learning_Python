import random
import time

player1 = input(" Please enter name of Player1 to play : ")
player2 = input(" Please enter name of Player2 to play : ")
p1_grand = 0
p2_grand = 0
dice = [0, 0, 0, 0]

for i in range(3):
    for i in range(4):
        dice[i] = random.randint(1, 6)

    p1 = dice[0] + dice[1]
    p1_grand += p1
    p2 = dice[2] + dice[3]
    p2_grand += p2
    print(f" {player1} You have rolled a {dice[0]} and a {dice[1]} giving you {p1}")
    time.sleep(2)
    print(f" {player2} You have rolled a {dice[2]} and a {dice[3]} giving you {p2}")
    time.sleep(2)
    if p1 > p2:
        print(f"{player1} wins this round !")
    elif p1 == p2:
        print(" It's a draw")
    else:
        print(f"{player2} wins this round !")
    time.sleep(2)

if p1_grand > p2_grand:
    print(f"{player1} wins with {p1_grand} points !")
elif p1_grand == p2_grand:
    print(" It's a draw")
else:
    print(f"{player2} wins with {p2_grand} points !")
