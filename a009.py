#解碼器
code = input()
k = -7
char = []
for i in code:
    char.append(chr(ord(i)+k))

print("".join(char))
