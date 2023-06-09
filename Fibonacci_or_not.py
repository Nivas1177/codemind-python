n = int(input())
a = 0
b = 1
l1 = [0,1]
for i in range(1,n-1):
    c = a+b
    a = b
    b = c
    l1.append(c)
print(n in l1)