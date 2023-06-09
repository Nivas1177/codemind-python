a,b = map(int,input().split())
l1 = []
l2 = []
l3 = []
if a>b:
    for i in range(1,a):
        if a%i == 0:
            l1.append(i)
        if b%i == 0:
            l2.append(i)
else:
    for i in range(1,b):
        if a%i == 0:
            l1.append(i)
        if b%i == 0:
            l2.append(i)
if len(l1)>len(l2):
    for i in l1:
        if i in l2:
            l3.append(i)
    print(max(l3))
else:
    for i in l2:
        if i in l1:
            l3.append(i)
    print(max(l3))
    
    