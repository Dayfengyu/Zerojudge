#you cannot pass?!

while True:
    try:
        n1 = [int(i) for i in input().split(' ')]
        n = n1[1:]
        avg = sum(n)/n1[0]
        if avg > 59:
            print("no")
        else:
            print("yes")
    except:
        break