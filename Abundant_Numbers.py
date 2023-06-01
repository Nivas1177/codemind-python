n = int(input())
l1 = []
for i in range(1,n):
    if n%i == 0:
        l1.append(i)
if sum(l1)>n:
    print('True')
else:
    print("False")