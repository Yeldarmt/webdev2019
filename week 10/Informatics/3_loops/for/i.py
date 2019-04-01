import math

a = int(input())
k=0
for i in range(1,int(math.sqrt(a))):
	if a%i==0:
		k+=1
if a%int(math.sqrt(a))==0:
	print(2*k+1)
else: 
	print(2*k)