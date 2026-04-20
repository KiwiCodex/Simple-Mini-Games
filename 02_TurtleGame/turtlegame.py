import turtle
import random


# Player's Racer
class Racer:
    def __init__(self, color: str, y_pos: int, goal_x: int):
        self.turtle = turtle.Turtle()
        self.turtle.shape("turtle")
        self.turtle.color(color, color)
        self.turtle.penup()
        self.turtle.goto(-250, y_pos)
        self.turtle.pendown()
        self.turtle.shapesize(2, 2, 2)
        self.turtle.pensize(3)
        
        # Stats
        self.color_name = color
        self.goal = goal_x

        # Turtle's "writer"
        self.writer = turtle.Turtle()
        self.writer.hideturtle()
        self.writer.penup()
        self.writer.goto(-250, y_pos + 30)

    def move(self, steps: int):
        distance = steps * 20
        self.turtle.forward(distance)

        # How much remains
        remaining = self.goal - self.turtle.xcor()
        if remaining < 0: remaining = 0

        # Update text's status
        self.writer.clear()

        if self.has_won():
            self.writer.goto(0, 0)
            self.writer.write(f"The {self.color_name.upper()} Won!", align="center", font=("Arial", 24, "bold"))

        else:
            self.writer.write(f"Dice {steps} | Missing: {remaining:.0f} units", font=("Arial", 10, "bold"))


    def has_won(self) -> bool:
        return self.turtle.xcor() >= self.goal


# Set the goal
def draw_goal(x: int, y: int):
    goal= turtle.Turtle()
    goal.hideturtle()
    goal.penup()
    goal.goto(x, y - 25)
    goal.pendown()
    goal.pensize(3)
    goal.circle(40)

# --GAME CONFIG--
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Turtle's Race")

GOAL_LINE = 200
draw_goal(GOAL_LINE, 200)
draw_goal(GOAL_LINE, -200)

# Instance for "racers"
player1 = Racer("green", 225, GOAL_LINE)
player2 = Racer("blue", -175, GOAL_LINE)

dice = [1, 2, 3, 4, 5, 6]

while True:
    # Player 1's Turn
    input(f"Turn: {player1.color_name.capitalize()}. Press Enter...")
    roll = random.choice(dice)
    player1.move(roll)

    if player1.has_won():
        print(f"The {player1.color_name.upper()} Won!")
        break
    
    # Player 2's Turn
    input(f"Turn: {player2.color_name.capitalize()}. Press Enter...")
    roll = random.choice(dice)
    player2.move(roll)

    if player2.has_won():
        print(f"The {player2.color_name.upper()} Won!")
        break


turtle.done()