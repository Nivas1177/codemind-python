n = int(input())
lst = list(map(int,input().split()))
a = int(input())
x = max(lst)
l1 = []
for i in lst:
    if i+a < x:
        l1.append("False")
    else:
        l1.append("True")
print(*l1)