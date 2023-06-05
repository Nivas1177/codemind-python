n = int(input())
lst = list(map(str,input().split()))
l1 = []
for i in lst:
    if "-" in i:
        l1.append(len(i)-1)
    else:
        l1.append(len(i))
k = min(l1)
print(l1.count(k))