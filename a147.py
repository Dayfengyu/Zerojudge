#print it all

while True:
    try:
        i = int(input())
        for i in range(1,i):
            if i % 7 != 0:
                print(i,end=' ')
        print()
    except:
            break