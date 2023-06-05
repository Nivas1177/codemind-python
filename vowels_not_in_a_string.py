n = input()
vowels = ["a","e","i","o","u"]
l1 = []
l2 = []
lwr = n.lower()
for i in lwr:
    if i in "aeiou":
        l1.append(i)
for i in vowels:
    if i not in l1:
        l2.append(i)
if len(l2) == 0:
    print("0")
else:
    print(*l2)