n = input()
s = n.split()
cnt = 0
for i in s:
    if i[0] in "aeiouAEIOU" and i[-1] not in "aeiouAEIOU":
        cnt+=1
print(cnt)