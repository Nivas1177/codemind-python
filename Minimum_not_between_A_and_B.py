n = int(input())
lst = list(map(int,input().split()))
a,b = map(int,input().split())
l1 = []
l2 = []
for i in lst:
    if i>=a and i<=b:
        l1.append(i)
for j in lst:
    if j not in l1:
        l2.append(j)
if len(l2) == 0:
    print("-1")
else:
    print(min(l2))