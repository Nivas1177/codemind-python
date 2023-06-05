n = input()
cnt = 0
for i in n:
    if i in "~`!@#$%^&*()_+{}:?><\|/.,":
        cnt+=1
print(cnt)