#一元二次
a, b, c = map(int, input().split())
d = (b*b)-(4*a*c)

if d > 0:
    x1 = (-b+(d**0.5))/(2*a)
    x2 = (-b-(d**0.5))/(2*a)
    print("Two different roots x1=%d , x2=%d" % (x1, x2))
elif d == 0:
    x1 = -b/(2*a)
    print("Two same roots x=%d" % x1)
else:
    print("No real root")
