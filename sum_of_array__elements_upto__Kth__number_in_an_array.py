n = int(input())
lst = list(map(int,input().split()))
a = int(input())
l1 = []
for i in lst:
    if i<=a:
        l1.append(i)
print(sum(l1))
