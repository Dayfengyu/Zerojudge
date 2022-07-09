#最大公因數
x , y = map(int,input().split())

import math

if x > y: x,y = y,x

ans = math.gcd(x,y)

print(ans)