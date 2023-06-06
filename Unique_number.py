n = input()
lst = []
for i in n:
    lst.append(int(i))
if len(set(lst)) == len(n):
    print("Unique Number")
else:
    print("Not Unique Number")
