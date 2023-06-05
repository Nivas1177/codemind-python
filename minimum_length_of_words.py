n = input()
s = n.split()
a = []
for i in s:
    a.append(len(i))
print(min(a))

