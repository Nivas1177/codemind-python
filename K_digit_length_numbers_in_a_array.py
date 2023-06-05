n, m = map(int,input().split())
lst = list(map(int,input().split()))
l1 = []
l2 = []
cnt = 0
for i in lst:
    l1.append(abs(i))
for j in l1:
    l2.append(str(j))
for k in l2:
    if len(k) == m:
        cnt+=1
print(cnt)
    