def minn(a,b,c,d):
	if a<=b and a<=c and a<=d:
		return a
	elif b<=a and b<=c and b<=d:
		return b
	elif c<=b and c<=a and c<=d:
		return c
	else:
		return d
lis = input().split()
print(minn(int(lis[0]),int(lis[1]),int(lis[2]),int(lis[3])))