n = int(input())
lst = list(map(int,input().split()))
l1 = [lst[i] for i in range(n) if i%2 == 0]
l2 = [lst[i] for i in range(n) if i%2 != 0]
for i in range(len(l1)):
    p=l2[i]
    while p:
        print(l1[i],end=" ")
        p-=1

