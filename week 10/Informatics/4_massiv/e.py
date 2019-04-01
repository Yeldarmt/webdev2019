n = int(input())

lis = input().split()
cnt = 0
for i in range(1,n):
	if (int(lis[i-1])>=0 and int(lis[i])>=0) or (int(lis[i-1])<0 and int(lis[i])<0):
		cnt+=1
#print(cnt)
if cnt==0:
	print("NO")
else:
	print("YES")
