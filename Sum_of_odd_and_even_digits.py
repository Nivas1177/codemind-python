n = int(input())
lst = list(map(int,input().split()))
l1 = []
l2 = []
for i in range(n):
    if i%2 == 0:
        l1.append(lst[i])
    else:
        l2.append(lst[i])
if sum(l1)-sum(l2) == 0:
    print("YES")
else: 
    print("NO")
    