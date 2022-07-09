#推算身分證
table = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':34,
            'J':18,'K':19,'L':20,'M':21,'N':22,'O':35,'P':23,'Q':24,'R':25,
            'S':26,'T':27,'U':28,'V':29,'W':32,'X':30,'Y':31,'Z':33}
while True:
    try:
        num = list((input()))
        sum = 0
        for i in range(8):
            sum += int(num[i])*(8-i)
        for i in table:
            a = list(str(table[i]))
            if int(num[8]) == 0:
                if (sum + int(a[0]) + int(a[1])*9)%10 == 0:
                    print(i,end='')
            else:
                if 10 - ((sum + int(a[0]) + int(a[1])*9)%10) == int(num[8]):
                    print(i,end='')
        print()
    except:
        break