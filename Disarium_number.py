n = input()
s = [*n]
l1 = []
l2 = []
for i in range(1,len(n)+1):
    l1.append(i)
for i in range(len(n)):
    l2.append(int(s[i])**l1[i])
print(sum(l2) == int(n))
