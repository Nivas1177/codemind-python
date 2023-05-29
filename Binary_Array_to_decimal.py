def decimal(n):
    dec = 0
    power = 1
    while n>0:
        rem = n%10
        n = n//10
        dec += rem*power
        power = power*2
    return dec
n = int(input())
lst = list(map(str,input().split()))
x = ''.join(lst)
print(decimal(int(x)))