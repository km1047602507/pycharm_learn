'''
构成：
    贪吃蛇Snake
    食物Food
    世界World


'''
import random
class Food():
    def __init__(self,queue):
        self.queue = queue
        self.new_food()
    def new_food(self):
        x = random.randrange(50,480,10)
        y = random.randrange(50,480,10)
        self.position = x,y
        self.queue.put({"food":self.position})
class Snake(threading.Thread):
    def __init__(self,world,queue):
        threading.Thread.__inint__(self)
        self.world = world
        self.queue
        self.points_earned = 0
        self.food = Food(self.queue)
        self.snake_points = [{(495,55),(485,55),(465,55),(455,55)]
        self.start()
    def run(self):
        if self.world.id_game_over:
            self._delete()
        while not self.world.is_game_over:
            self.queue.put({"move":self.snake_points})
            time.sleep(0.5)
            self.move()

    '''
    1.能动
    2.每次动，计算蛇头的位置
    3.检测游戏是否结束
    '''
    def move(self):
        new_snake_point = self.cal_new_pos()
        if self.food.position == new_snake_point:
            self.points_earned += 1
            self.queue.put({"points_earned":self.points_earned})
            self.food.new_food()
        else:
            self.snake_points.pop(0)
            self.check_game_over(new_snake_point)
            self.snake_points.qppend(new_snake_point)
    def cal_new_position(self):
        last_x,last_y = self.snake_points[-1]
        if self.direction == "Up":
            new_snake_point = last _x,last_y - 10
        elif self.direction == "Down":

        return new_snake_point
    def key_press(self,e):
        self.direction = e.keysym2
    def check_game_over(self,snake_point):
        x,y = snake_point[0],snake_point[1]
        if not -5 < x < 505 or not -5 < y < 315 or snake_point in self.snake_points:
            self.queue.put({'game_over':True})
class World(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.queue
        self.is_game_over = False

        self.canvas = Canvas(self,width=500,heght=300,bg='red')
        self.pack()

        self.snake = self.canvas.create_line((0,0))





