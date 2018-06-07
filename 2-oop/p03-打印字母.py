#打印字母A
def a():
    for i in range(1,6):
        for k in range(5-i):
            print(' ',end='')
        for j in range(1,i+1):
            if i == 1 or i == 4 or j == 1 or i == j:

                print("*" ,end=' ')
            else:
                print(" ",end=' ')
        print()
#打印字母B
def b():
    for i in range(1,5):
        for j in range(1,4):
            if i == 1 or i == 4:
                if j != 3:
                    print('*',end=' ')
                else:
                    print(' ', end=' ')
            elif j ==1 or j ==3:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
    for i in range(2,5):
        for j in range(1,4):
            if i == 1 or i == 4:
                if j != 3:
                    print('*',end=' ')
                else:
                    print(' ', end=' ')
            elif j ==1 or j ==3:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
#打印字母C
def c():
    for i in range(1,5):
        for j in range(1,4):
            if i == 1 or i == 4:
                if j != 1:
                    print('*',end=' ')
                else:
                    print(' ',end=' ')
            elif j ==1 or j ==3:
                if j == 1:
                    print('*',end=' ')
                else:
                    print(' ',end=' ')
            else:
                print(' ',end=' ')
        print()
#打印字母D
def d():
    for i in range(1,5):
        for j in range(1,4):
            if i == 1 or i == 4:
                if j != 3:
                    print('*',end=' ')
                else:
                    print(' ', end=' ')
            elif j ==1 or j ==3:
                   print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
#打印字母E
def e():
    for i in range(1,8):
        for j in range(1,4):
            if i ==1 or i ==4 or i == 7 or j == 1:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
#打印字母F
def f():
    for i in range(1,8):
        for j in range(1,4):
            if i ==1 or i ==4 or j == 1:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
#打印字母G
def g():
    for i in range(1,5):
        for j in range(1,5):
            if i == 1 or i == 4:
                if j != 1:
                    print('*',end=' ')
                else:
                    print(' ',end=' ')
            elif i == 2:
                if j == 1:
                    print('*',end=' ')
                else:
                    print(' ', end=' ')
            else:
                if j != 2:
                    print('*',end=' ')
                else:
                    print(' ',end=' ')
        print()
#打印字母H
def h():
    for i in range(1,8):
        for j in range(1,6):
            if i == 4 or j == 1 or j == 5:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()



