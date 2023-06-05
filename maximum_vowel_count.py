def vowels(i):
    cnt = 0
    for j in i:
        if j in "aeiou":
            cnt+=1
    return cnt

n = input()
s = n.split()
l1 = []
for i in s:
    x = vowels(i)
    l1.append(x)
print(max(l1))