def power(c,d):
	cnt = 1.0
	for i in range(d):
		cnt*=c
	return cnt
m = input().split()
a = float(m[0])
b = int(m[1])
print(power(a,b))