c_list = []
count=[]
with open('rj.txt') as text:
	rj = text.read()
	print(rj)
for c in rj:
	if c not in c_list:
		c_list.append(c)
		count.append(0)
	char_pos = c_list.index(c)
	count[char_pos] += 1
for i in range (len(c_list)):
	print(f"{c_list[i]}: {count[i]}")