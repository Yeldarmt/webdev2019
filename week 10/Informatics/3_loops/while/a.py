import math

a = int(input())

i = 1

while i<=a:
	b = int(math.sqrt(i))
	if b*b==i:
		print(i)
	i+=1