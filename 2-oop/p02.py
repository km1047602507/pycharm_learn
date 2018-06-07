import math
print(math.ceil(5.001))

print(math.floor(5.001))

import keyword
print(round(5.45))
#sqrt是开平方
print(math.sqrt(4))
#pow是开平方
print(math.pow(4,3))
#幂运算
print(5**2)
print(abs(-3.6))
print(math.fsum([1.2,3,4,5]))
print(sum([1,2,3,4]))

print(math.modf(4.5))
help(math.modf)

rst = math.copysign(2,-5)
print(rst)
help(math)
print(math.pi)
print(math.e)
import random
for i in range(10):
    print(random.random() * 10)
    print(random.randint(1,9))
help(random.randrange)
print("-" * 50)
#import tkinter
#tkinter._test()
for j in range(10):
    print(random.choice([12,23,34,45,56]))
list1 = [12,23,34,45,56]
random.shuffle(list1)
print(list1)
print("-" * 50)
for k in range(10):
    print(random.uniform(1,8))
print("-" * 50)



#案例


import random
import math

class GameNum():
    def line(self):
        str_num = ''
        for i in range(4):
            j = random.randrange(97,123)
            str_s = chr(j)
            str_num = str_num + str_s
        #print(str_num)
        for m in range(8):
            n = random.randrange(0,10)
            str_num = str_num +str(n)
        #print(str_num)
        return str_num


    def num_game(self,total,source):
        source = 0
        total = 0
        while 1:
            num = int(input("请输入一个三位数："))
            if num == -1:
                break
            random_num = random.randrange(100,1000)
            print("num = {0},random_num = {1}".format(num,random_num))
            if 100<=num<=999:
                total += 1
                print("输入%d次"%total)
                if num > random_num:
                    print("百位数字是：{}  十位数字是：{}  个位数字是：{}".format(num//100,num//10%10,num%10))
                    print("你输入的数字比程序随机数大！")
                elif num == random_num:
                    source += 1
                    print("恭喜您中奖了！您的分数为".source)
                    print("你中奖的概率是多少",source/total)
                else:
                    for k in range(10):
                        str_line = GameNum.line(0)
                        with open('str_num.txt','a') as f:
                            f.write(str_line + '\n')

            else:
                print("您输入的数字有误，请重新输入！")

#程序入口（也叫调试入口）
if __name__ == '__main__':
    source = 0
    total = 0
    GameNum.num_game(0,source,total)


