def prime(i):
    cnt = 0
    for j in range(1,i+1):
        if i%j == 0:
            cnt+=1
    if cnt ==2:
        return True
    else:
        return False


n = int(input())
lst = list(map(int,input().split()))
a = int(input())
l1 = []
cnt = 0
for i in lst:
    if i<=a:
        l1.append(i)
for j in l1:
    x = prime(j)
    if prime(j) == True:
        cnt+=1
print(cnt)
