import turtle
import time
import random
import winsound


# Player
class Snake:
    def __init__(self):
        self.head = turtle.Turtle()
        self.head.shape("square")
        self.head.color("green")
        self.head.speed(0)
        self.head.penup()
        self.head.goto(0, 0)
        self.direction = 'stop'
        self.segments = [] #Snake's body

    def go_up(self):
        if self.direction != 'down':
            self.direction = "up"

    def go_down(self):
        if self.direction != 'up':
            self.direction = "down"

    def go_right(self):
        if self.direction != 'left':
            self.direction = "right"

    def go_left(self):
        if self.direction != 'right':
            self.direction = "left"

    def move(self):
        # Move body segments towards the one ahead
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i-1].xcor()
            y = self.segments[i-1].ycor()

            self.segments[i].goto(x, y)

        # First segment follows head
        if len(self.segments) > 0:
            x = self.head.xcor()
            y = self.head.ycor()
            self.segments[0].goto(x, y)

        # Movement
        if self.direction == 'up':
            self.head.sety(self.head.ycor() + 20)
        if self.direction == 'down':
            self.head.sety(self.head.ycor() - 20)
        if self.direction == 'right':
            self.head.setx(self.head.xcor() + 20)
        if self.direction == 'left':
            self.head.setx(self.head.xcor() - 20)

    def add_segment(self):
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("darkgreen")
        new_segment.penup()
        self.segments.append(new_segment)

    def reset(self):
        time.sleep(1)
        self.head.goto(0, 0)
        self.direction = "stop"

        # Hide old segments
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()

# Score
class Score:
    def __init__(self):
        self.score = 0
        self.highscore = 0
        self.writer = turtle.Turtle()
        self.writer.speed(0)
        self.writer.color("black")
        self.writer.penup()
        self.writer.hideturtle()
        self.writer.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.writer.clear()
        self.writer.write(f"Score: {self.score} \tHighscore: {self.highscore}", align="center", font=("courier", 24, "normal") )

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
        
        self.score = 0
        self.update_score()
    
    def increase_score(self):
        self.score += 10
        self.update_score()

# Food
class Food(turtle.Turtle):
    def __init__(self, color, shape):
        super().__init__() # Inicialize Base Turtle
        self.color(color)
        self.shape(shape)
        self.penup()
        self.speed(0)
        self.refresh()

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)

# 1st Variant Food - Normal
class NormalFood(Food):
    def __init__(self):
        super().__init__("orange", "square")
        self.points = 10
        self.speed_change = -0.005 # Acelerates
 
# 2nd Variant Food - Slow Power Up
class SlowFood(Food):
    def __init__(self):
        super().__init__("blue", "triangle")
        self.points = 5
        self.speed_change = 0.2 # Slows you

# 3rd Variant Food - Fast Power Up
class FastFood(Food):
    def __init__(self):
        super().__init__("red", "circle")
        self.points = 20
        self.speed_change = -0.015 # Acelerates you even more

class SnakeGame():
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(600, 600)
        self.screen.bgcolor("gray")
        self.screen.title("Snake")
        self.screen.tracer(0)

        self.snake = Snake()
        self.score_manager = Score()
        self.normal_food = NormalFood()
        self.extra_food = SlowFood()
        self.extra_food.hideturtle()

        self.delay = 0.1
        self.normal_streak = 0
        self.extra_active = False

        self.setup_controls()

    def setup_controls(self):
        self.screen.listen()
        self.screen.onkeypress(self.snake.go_up, "Up")
        self.screen.onkeypress(self.snake.go_down, "Down")
        self.screen.onkeypress(self.snake.go_right, "Right")
        self.screen.onkeypress(self.snake.go_left, "Left")

    def reset_match(self):
        play_game_over_sound()
        self.snake.reset()
        self.score_manager.reset_score()
        self.delay = 0.1
        self.normal_streak = 0
        self.extra_active = False
        self.extra_food.hideturtle()
        self.extra_food.goto(1000, 1000)

    def handle_collision(self):
        if abs(self.snake.head.xcor()) > 290 or abs(self.snake.head.ycor()) > 290: 
            self.reset_match()

        # Normal Food
        if self.snake.head.distance(self.normal_food) < 20:
            self.process_eat(self.normal_food)
            self.normal_food.refresh()
            self.manage_extra_spawn()

        # Extra Food
        if self.extra_active and self.snake.head.distance(self.extra_food) < 20:
            self.process_eat(self.extra_food)
            self.extra_active = False
            self.extra_food.hideturtle()
            self.extra_food.goto(1000, 1000)
        
        # Own Body Collision
        for segment in self.snake.segments:
            if segment.distance(self.snake.head) < 10:
                self.reset_match()
    
    def process_eat(self, food_obj):
        play_eat_sound()
        self.score_manager.score += food_obj.points
        self.score_manager.update_score()
        self.delay += food_obj.speed_change
        self.delay = max(0.01, min(self.delay, 0.2)) # Speed limits
        self.snake.add_segment()
    
    def manage_extra_spawn(self):
        if not self.extra_active:
            if random.random() < 0.3:
                self.extra_food = FastFood() if random.random() < 0.5 else SlowFood()
                self.extra_food.refresh()
                self.extra_food.showturtle()
                self.extra_active = True
                self.normal_streak = 0
        else:
            self.normal_streak += 1
            if self.normal_streak >= 3:
                self.extra_active = False
                self.extra_food.hideturtle()
                self.extra_food.goto(1000, 1000)

    def update(self):
        self.screen.update()
        self.handle_collision()
        self.snake.move()
        time.sleep(self.delay)
    

# Details
def play_eat_sound():
    winsound.Beep(1000, 50)

def play_game_over_sound():
    winsound.Beep(400, 500)

# -- Game's Exe --
the_snake = SnakeGame()

while True:
    the_snake.update()

turtle.done()