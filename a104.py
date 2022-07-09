#排序
while True:
    try:
        n=int(input())
        arr=[int(i) for i in input().split()]
        arr.sort()
        for i in range(n):
            print("{}".format(arr[i]),end=' ')
        print()
    except EOFError:
        break