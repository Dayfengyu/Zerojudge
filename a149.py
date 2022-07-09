#乘乘樂

while True:
    try:
        n = int(input())
        for i in range(0,n):
            num = [int(i) for i in list(input())]
            result = 1
            for j in num:
                result = result * j
            print(result)
        print()
    except:
        break