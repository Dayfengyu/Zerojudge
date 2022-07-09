#完全平方和
n = int(input())
for i in range(n):
    sum = 0
    result = []
    a = int(input())
    b = int(input())
    for j in range(a,b+1):
        if (j**0.5) * 100 % 100 == 0:
            sum += j
    print("Case {}: {}".format(i+1,sum))
