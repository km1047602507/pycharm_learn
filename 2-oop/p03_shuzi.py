import random
def GameNum():
    while 1:
        num = int(input("请输入一个三位数，输入-1结束:"))

        rand_num = random.randrange(1,4)

        print("您输入的数字是：{}  系统随机数字是：{}".format(num,rand_num))

        if num == -1:
            break

        source = 0
        if num > rand_num:
            print("您输入的数字比随机数字大！")
        elif num == rand_num:
            source += 100
            print("您输入的数字和随机数字相同！")
        else:
            print("您输入的数字比系统随机数字小！")

