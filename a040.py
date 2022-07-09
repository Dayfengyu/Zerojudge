#水仙花數

list1 = {1,2,3,4,5,6,7,8,9,153,370,371,407,1634,
         8208,9474,54748,92727,93084,548834
        }
n , m = map(int,input().split())
output = 0

for i in range(m-n):
    for j in list1:
        if n + i == j:
            print(j , end=' ')
            output = 1

if output == 0 : print("none")