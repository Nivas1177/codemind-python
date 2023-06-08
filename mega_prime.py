def prime(n):
    cnt = 0
    for i in range(1,n+1):
        if n%i == 0:
            cnt+=1
    if cnt == 2:
        return True
    else:
        return False

n = input()
cnt = 0
if prime(int(n)) == True:
    for i in n:
        if prime(int(i)) == True:
            cnt+=1
    if cnt == len(n):
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")
