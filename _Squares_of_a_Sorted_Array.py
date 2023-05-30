n = int(input())
lst = list(map(int,input().split()))
l1 = []
for i in lst:
    l1.append(abs(i*i))
print(*sorted(l1))