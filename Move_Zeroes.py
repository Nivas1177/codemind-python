n = int(input())
lst = list(map(int,input().split()))
l1 = []
cnt = 0
for i in lst:
    if i == 0:
        cnt+=1
    else:
        l1.append(i)
        
for i in range(cnt):
    l1.append("0")
print(*l1)