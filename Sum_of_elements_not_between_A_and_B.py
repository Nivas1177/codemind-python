n = int(input())
l = list(map(int,input().split()))
a, b = map(int,input().split())
l1 = []
for i in range(n):
    if l[i]<a or l[i]>b:
        l1.append(l[i])
    
print(sum(l1))