#二進制
while 1:
    try:
        print("{:b}".format(int(input())))
    except EOFError:
        break

