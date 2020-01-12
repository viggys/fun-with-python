from turtle import Screen
from turtle import Turtle

TITLE = "PyPong"
BACKGROUND_COLOUR = "black"
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Window Object
wndw = Screen()
wndw.title(TITLE)
wndw.bgcolor(BACKGROUND_COLOUR)
wndw.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
wndw.tracer(0)

# Left Paddle Object
paddle_left = Turtle()
paddle_left.speed(0)
paddle_left.color("white")
paddle_left.shape("square")
paddle_left.shapesize(stretch_wid=5, stretch_len=1)
paddle_left.penup()
paddle_left.goto(-385, 0)

# Right Paddle Object
paddle_right = Turtle()
paddle_right.speed(0)
paddle_right.color("white")
paddle_right.shape("square")
paddle_right.shapesize(stretch_wid=5, stretch_len=1)
paddle_right.penup()
paddle_right.goto(375, 0)

# Pong Object
pong = Turtle()
pong.speed(0)
pong.color("white")
pong.shape("square")
pong.penup()
pong.goto(0, 0)
pong.DX = 1
pong.DY = 1
pong.SEMI_WIDTH = 10
pong.SEMI_HEIGHT = 10


def left_paddle_up():
    """Function to move the left paddle up

    :return: void
    """
    pos_y = paddle_left.ycor()
    pos_y += 20
    paddle_left.sety(pos_y)


def left_paddle_down():
    """Function to move the left paddle down

    :return: void
    """
    pos_y = paddle_left.ycor()
    pos_y -= 20
    paddle_left.sety(pos_y)


def right_paddle_up():
    """Function to move the right paddle up

    :return: void
    """
    pos_y = paddle_right.ycor()
    pos_y += 20
    paddle_right.sety(pos_y)


def right_paddle_down():
    """Function to move the right paddle down

    :return: void
    """
    pos_y = paddle_right.ycor()
    pos_y -= 20
    paddle_right.sety(pos_y)


# listen keyboard instructions
wndw.listen()
wndw.onkeypress(fun=left_paddle_up, key="w")
wndw.onkeypress(fun=left_paddle_down, key="s")
wndw.onkeypress(fun=right_paddle_up, key="Up")
wndw.onkeypress(fun=right_paddle_down, key="Down")


def reset_pong():
    """Reset position of pong to center (0, 0)

    :return: void
    """
    pong.goto(0, 0)


def bounce_vertically():
    """Checks for the vertical position of pong
    and bounces it, if at top or bottom boundary

    :return: void
    """
    # print("Checking pong vertical position")
    pos_y = pong.ycor()
    if (pos_y + pong.SEMI_HEIGHT) >= (WINDOW_HEIGHT / 2) or (pos_y - pong.SEMI_HEIGHT) <= (- WINDOW_HEIGHT / 2):
        print("Bouncing at Vertical Position: " + str(pos_y))
        pong.DY *= -1


def reset_horizontally():
    """Checks for the horizontal position of pong
    and resets the position to start, if the pong crosses left or right boundary

    :return: void
    """
    # print("Checking pong horizontal position")
    pos_x = pong.xcor()
    if (pos_x + pong.SEMI_WIDTH) >= (WINDOW_WIDTH / 2) or (pos_x - pong.SEMI_WIDTH) <= (- WINDOW_WIDTH / 2):
        print("Resetting from Horizontal Position: " + str(pos_x))
        pong.DX *= -1
        reset_pong()

# game run logic
def start_pong():
    """Starts the pong game

    :return: void
    """
    wndw.update()
    pong.setx(pong.xcor() + pong.DX)
    pong.sety(pong.ycor() + pong.DY)


while True:
    start_pong()
    bounce_vertically()
    reset_horizontally()

