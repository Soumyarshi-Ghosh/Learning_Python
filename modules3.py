import random
import time
player1 = input(" Please enter name of Player1 to play : ")
player2 = input(" Please enter name of Player2 to play : ")
p1_grand = 0
p2_grand = 0

for i in range(3):
    p1d1 = random.randint(1, 6)
    p1d2 = random.randint(1, 6)
    p2d1 = random.randint(1, 6)
    p2d2 = random.randint(1, 6)

    p1 = p1d1 + p1d2
    p1_grand += p1
    p2 = p2d1 + p2d2
    p2_grand += p2
    print(f" {player1} You have rolled a {p1d1} and a {p1d2} giving you {p1}")
    time.sleep(2)
    print(f" {player2} You have rolled a {p2d1} and a {p2d2} giving you {p2}")
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
