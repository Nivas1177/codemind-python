n = int(input())
lst = list(map(int,input().split()))
a, b = map(int,input().split())
l1 = []
for i in lst:
    if i>=a and i<=b:
        l1.append(i)
if len(l1) == 0:
    print("-1")
else:
    print(*l1)