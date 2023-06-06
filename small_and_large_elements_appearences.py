n = input()
s = n.split()
l1 = []
l2 = []
for i in s:
    l1.append(min(i))
a = min(l1)
for j in s:
    l2.append(max(j))
b = max(l2)
print(a,n.count(a),b, n.count(b))
