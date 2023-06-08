def sdf(n):
    k = str(n)
    cnt = 0
    for i in k:
        if n%int(i) == 0:
            cnt+=1
    if cnt == len(k):
        return True
    else:
        return False


n = int(input())
m = int(input())
l1 = []
l2 = []
for i in range(n,m+1):
    if str(i)[-1] != '0':
        l1.append(i)
for i in l1:
    if sdf(i) == True:
        l2.append(i)
print(*l2,end = ' ')