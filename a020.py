#身分證
local = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16,"H":17,
         "I":34,"J":18,"K":19,"L":20,"M":21,"N":22,"O":35,"P":23,
         "Q":24,"R":25,"S":26,"T":27,"U":28,"V":29,"W":32,"X":30,
         "Y":31,"Z":33}

ID = input()
sum1 = 0

if len(ID)!=10:
    print("fake")

sum = (local[ID[0]]//10) + (local[ID[0]]%10)*9

for i in range(8):
    sum += int(ID[i+1])*(8-i)

sum += int(ID[9])

if sum % 10 == 0 :
    print("real")
else:
    print("fake")