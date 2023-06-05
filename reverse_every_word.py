n = input()
s = n.split()
l1 = []
for i in s:
    l1.append(i[::-1])
print(*l1)