#矩陣翻轉
while True:
    try:
        a,b=map(int,input().split())
        array=[]
        for i in range(a):
            array.append(input().split())
        for i in range(b):
            for j in range(a):
                print((array[j][i]),end=' ')
            print(' ')
    except EOFError:
        break