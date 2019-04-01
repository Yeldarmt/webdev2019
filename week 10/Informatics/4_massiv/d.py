n = int(input())

lis = input().split()

cnt = 0

for i in range(1,n):
	if int(lis[i])>int(lis[i-1]):
		cnt+=1

print(cnt)