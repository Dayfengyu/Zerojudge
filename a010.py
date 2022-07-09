#因數分解
n=int(input(""))
result={}
while True:
    for i in range(2,n+1):
        if n % i == 0:
            if i in result:
                result[i]= result[i]+1
            else:
                result[i]=1
            n = n // i
            break
    if n == 1:
        break

output=''
for i in result:
    if result[i] != 1:
       output = f'{output}{i}^{result[i]} * '
    else:
        output = f'{output}{i} * '  
output=output[:-2]
print(output)