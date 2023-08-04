import random

player1 = input(" Please enter name of Player1 to play : ")

player2 = input(" Please enter name of Player2 to play : ")

p1d1 = random.randint(1, 6)
p1d2 = random.randint(1, 6)
p2d1 = random.randint(1, 6)
p2d2 = random.randint(1, 6)

p1 = p1d1 + p1d2
p2 = p2d1 + p2d2
print(f" {player1} You have rolled a {p1d1} and a {p1d2}")
print(f" {player2} You have rolled a {p2d1} and a {p2d2}")

if p1 > p2:
    print(f"{player1} wins")
elif p1 == p2:
    print(" It's a draw")
else:
    print(f"{player2} wins")