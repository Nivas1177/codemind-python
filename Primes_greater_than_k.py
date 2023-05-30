def is_prime(x):
    cnt = 0
    for i in range(1,x+1):
        if x%i == 0:
            cnt+=1
    if cnt == 2:
        return True
    else:
        return False
n = int(input())
lst = list(map(int,input().split()))
a = int(input())
l1 = []
cnt = 0
for i in lst:
    if i>=a:
        l1.append(i)
for i in l1:
    y = is_prime(i)
    if is_prime(i) == True:
        cnt+=1
print(cnt)
    