n = int(input())
lst = list(map(int,input().split()))
l1 = []
for i in lst:
    if lst.count(i) == 1:
        l1.append(i)
if len(l1) == 0:
    print("-1")
else:
    print(max(l1))