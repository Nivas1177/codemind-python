n = input()
s = n.split()
l1 = []
l2 = []
for i in s:
    l1.append(min(i))
    l2.append(max(i))
a = []
b = []
for i in l1:
    a.append(ord(i))
for i in l2:
    b.append(ord(i))
print(sum(b) - sum(a))