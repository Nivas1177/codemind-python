def prime(i):
    cnt = 0
    for j in range(1,i+1):
        if i%j == 0:
            cnt+=1
    if cnt == 2:
        return True
    else:
        return False
n = int(input())
lst = list(map(int,input().split()))
l1 = []
for i in lst:
    x = prime(i)
    if prime(i) == True:
        l1.append(i)
x = sum(l1)/len(l1)
print('{:.2f}'.format(x))