#Sagit's 計分程式
while True:
    try:
        n=int(input())
        if n>=0 and n<=100:
            if n <= 10 :
                print(n*6)
            elif n<=20:
                print(60+(n-10)*2)
            elif n<=40:
                print(80+(n-20))
            else:
                print(100)
    except:
        break