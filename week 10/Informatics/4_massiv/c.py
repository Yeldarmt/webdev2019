n = int(input())
lis = input().split()
cnt = 0
for i in range(n):
	if int(lis[i])>0:
		cnt+=1
print(cnt)