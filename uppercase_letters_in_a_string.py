def upper(i):
    cnt = 0
    for j in i:
        if j in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            cnt+=1
    return cnt


n = input()
s = n.split()
l1 = []
for i in n:
    x = upper(i)
    l1.append(x)
print(sum(l1))
        

    
