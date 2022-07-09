#回家作業
x = int(input())

for i in range(x):
    a, b, c, d = map(int, input().split())

    if b-a == c-b:
        print(a, b, c, d, int(d+(b-a)))
    else:
        print(a, b, c, d, int(d*(b/a)))
