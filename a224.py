#回文
while True:
    try:
        n = list(input().lower())
        s = set(n)
        a = 0
        table = 'abcdefghijklmnopqrstuvwxyz'
        for i in s:
            if i in table:
                c = n.count(i)
                if c % 2 != 0:
                    a += 1
        if a <= 1:
            print("yes !")
        else:
            print("no...")
    except:
        break