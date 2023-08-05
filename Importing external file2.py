import random
with open('rj.txt') as text:
	rj = text.read()
	print(rj)
print("The text variable is: ", type(text))
print("The contents variable is: ", type(rj))

start = random.randint(5,50)
end = random.randint(100,200)
print(rj[start:end])
