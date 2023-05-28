n = int(input())
lst = list(map(int,input().split()))
l1 = []
l2 = []

for i in range(n//2):
    if lst[i]<lst[(n//2)]:
        l1.append(lst[i])
print(sum(l1))
for j in lst:
    if j not in l1:
        l2.append(j)
print(sum(l2))
