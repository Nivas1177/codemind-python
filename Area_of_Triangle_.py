import math
l,b,h = map(int,input().split())
s = (l+b+h)/2
area = math.sqrt(s*(s-l)*(s-b)*(s-h))
print('{:.2f}'.format(area))