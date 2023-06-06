n = input()
s = n.split()
for i in s:
    print(ord(max(i))-ord(min(i)),end = ' ')