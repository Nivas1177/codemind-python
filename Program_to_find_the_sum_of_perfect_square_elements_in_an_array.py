n = int(input())
lst = list(map(int,input().split()))
l1 = []
l2 = []
for i in range(0,max(lst)):
    l1.append(i*i)
for j in lst:
    if j in l1:
        l2.append(j)
print(sum(l2))