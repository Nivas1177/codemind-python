def palindrome(n):
    if str(n)[::-1] == str(n):
        return True
    else:
        return False
n = int(input())
l1 = []
l2 = []
l3 = []
for i in range(1,n*10000):
    if palindrome(i) == True:
        l1.append(i)
for j in l1:
    if j<n:
        l2.append(j)
    if j>n:
        l3.append(j)
a = l2[-1]
b = l3[0]
if (n-a)>(b-n):
    print(b)
elif (n-a) == (b-n):
    print(a,b)
else:
    print(a)

    
