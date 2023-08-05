import random
c_list =[]
with open('rj.txt') as text:
	rj = text.read()
	print(rj)
for letter in range(rj):
	c_list.append(letter)
print(c_list)