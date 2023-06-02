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
cnt = 0
for i in range(1,n+1):
    if n%i == 0:
        l1.append(i)
for j in l1:
    if prime(j) == False:
        cnt+=1
print(cnt)