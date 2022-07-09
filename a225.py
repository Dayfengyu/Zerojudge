#排列
#key=lambda 元素: 元素[字段索引] 
while True:
    try:
        n=int(input())
        num = [int(i) for i in input().split()]
        num.sort(reverse=True)
        num.sort(key=lambda s:s%10)
        print(*num)
    except:
        break
