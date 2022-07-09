#明明愛數數

while True:
    try:
        n , m = map(int,input().split())
        a = 0
        b = 0
        while True:
           a += 1
           b += n
           n += 1
           if b > m:
               break 
        print(a)
    except EOFError:
        break