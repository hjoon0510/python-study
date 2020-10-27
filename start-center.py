a = int(input('숫자를 입력하세요: '))
for i in range(a):
    for j in range(a - 1):
        if j < i:
            print(' ', end='')
        else:
            print('*', end='')
    for f in range(a - i):

        print("*",end="")

    print()

