def prime(n):
    cnt = 0
    for i in range(1,n+1):
        if n%i == 0:
            cnt +=1
    if cnt == 2:
        return True
    else:
        return False
n = int(input())
lst = list(map(int,input().split()))
l1 = []
l2 = []
l3 = []
l4 = []
if "1" in lst:
    lst.pop(1)
product = 1
c = 1
for i in lst:
    if prime(i) == True:
        l1.append(i)
    elif prime(i) == False:
        l2.append(i)
for j in l1:
    product *= j
l3.append(product)
for k in l2:
    c *= k
l4.append(c)
print(abs(sum(l3)-sum(l4)))



