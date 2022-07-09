#數字翻轉
q = list(input())
q.reverse()

try:
    while q[0] == '0': del q[0]
except:
    q = ['0']

for i in q:
    print(i, end='')