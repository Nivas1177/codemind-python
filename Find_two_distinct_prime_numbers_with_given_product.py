def prime(n):
    cnt = 0
    for i in range(1,n+1):
        if n%i == 0:
            cnt+=1
    if cnt == 2:
        return True
    else:
        return False
            

n = int(input())
l1 = []
l2 = []
for i in range(1,n+1):
    if prime(i) == True:
        l1.append(i)
for i in l1:
    for j in l1[::-1]:
        if i*j == n:
            l2.append(i)
if len(l2) == 0:
    print("-1")
else:
    print(*l2)
    