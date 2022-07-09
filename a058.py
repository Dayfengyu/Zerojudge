#mod3

while True:
    try:
        n=int(input())
        arr=[0,0,0]
        for i in range(n):
            a=int(input())
            if a % 3 == 0:
                arr[0] += 1
            if a % 3 == 1 :
                arr[1] += 1
            if a % 3 == 2 :
                arr[2] += 1
        for i in arr:
            print(i,end=' ')
    except:
        break