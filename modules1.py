import random
for i in range(4):
	coin = random.randint(0,1)

	if coin == 0:
		print("Heads")
	else:
		print("Tails")