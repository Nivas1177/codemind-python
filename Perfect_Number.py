n = int(input())
lst = []
for i in range(1,n):
    if n%i == 0:
        lst.append(i)
if sum(lst) == n:
    print("True")
else:
    print("False")