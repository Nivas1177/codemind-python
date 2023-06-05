n = input()
cnt = 0
for i in n:
    if i in "AEIOUaeiou":
        cnt+=1
print(cnt)