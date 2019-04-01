n = int(input())

m = input().split()

cnt = 0

for i in range(1,n-1):
	if int(m[i])>int(m[i-1]) and int(m[i])>int(m[i+1]):
		cnt+=1
print(cnt)