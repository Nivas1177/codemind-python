n = input()
vow = ["a","e","i","o","u"]
vowels = ["A","E","I","O","U"]
l1 = []
l2 = []
for i in n:
    if i in vow:
        l1.append(i)
    elif i in vowels:
        l2.append(i)
if len(set(l1)) == 5 or len(set(l2)) == 5:
    print("True")
else:
    print("False")