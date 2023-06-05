def lower(i):
    cnt = 0
    for j in i:
        if j in "abcdefghijklmnopqrstuvwxyz":
            cnt+=1
    return cnt
n = input()
s = n.split()
l1 = []
for i in s:
    x = lower(i)
    l1.append(x)
print(sum(l1))    