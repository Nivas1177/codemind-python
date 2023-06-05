n = input()
s = n.split()
l1 = []
for i in s:
    l1.append(len(i))
print(sum(l1))