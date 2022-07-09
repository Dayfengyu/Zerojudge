#提款機密碼
import math
x=list(input())
for i in range(6):
    print(int(math.fabs(ord(x[i])-ord(x[i+1]))),end='')
