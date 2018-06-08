'''
ScreenSaver:
    canvers
    
Ball:
    颜色、大小、方向、多少、运动方向
    球能动
'''
import random
import tkinter

class RandomBall():
    def __init__(self,canvas,scrnwidth,scrnheight):
        #球出现的初始位置随机
        self.xpos = random.randint(10,int(scrnwidth)-20)
        self.ypos = random.randint(10,int(scrnheight)-10)
        #定义球运动的速度
        #模拟运动
        self.xvelocity = random.randint(4,20)
        self.yvelocity = random.randint(4,20)
        #屏幕的大小
        self.scrnwidth = scrnwidth
        #定义球的大小
        self.radius = random.randint(20,120)
        #定义球的颜色
        c = lambda: random.randint(0,255)
        self.color = '#%02x%02x%02x'%(c(),c(),c())


    def creat_ball(self):
        #tkinter只有画椭圆的工具
        x1 = self.xpos - self.radius
        y1 = self.ypos + self.radius
        x2 = self.xpos + self.radius
        y2 = self.ypos - self.radius
        self.item = self.canvas.create_oval(x1,y1,x2,y2,fill=self.color,outline=self.color)
    def move_ball(self):
        self.xpos += self.xvelocity
        self.ypos += self.yvelocity
        #判断是否撞墙
        if self.xpos + self.radius >= self.scrnwidth:
            self.xvelocity *= -1
        #elif
        #elif
        #else:



        self.canvas.move(self.item,self.xvelocity,self.yvelocity)



class ScreenSaver():
    balls = list()

    def __init__(self):
        self.num_balls = random.randint(6,20)
        self.root = tkinter.Tk()
        #取消边框
        self.root.overriderdirect(1)
        self.root.bind('<Motion>',self.myquit)

        w,h = self.root.winfo_screenwidth(),self.winfo_screenheitht()
        self.canvas = tkinter.Canvas(self.root,width=2,heitht=h)
        self.canvas.pack()

        for i in range(self.num_balls):
            ball = RandomBall(self.canvas,scrnwidth=w,scrnheitht=h)
            ball.creat_ball()
            self.balls.append(ball)

        self.run_screen_saver()
        self.root.mainloop()

    def run_screen_saver(self):
        for ball in self.balls:
            ball.move_ball()
            self.canvas.after(200,self.run_screen_saver)

    def myquit(self,e):
        self.root.destroy()

if __name__ == '__main__':
    ss = ScreenSaver()
    ss.start()
