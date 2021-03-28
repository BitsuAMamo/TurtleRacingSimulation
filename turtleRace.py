import turtle
import time
import random

WIDTH, HEIGHT = 700, 500
COLORS = ['gray', 'cyan', 'green', 'red', 'yellow',
          'pink', 'brown', 'blue', 'purple', 'white']


def get_turtle_amount():
    """
    Funtion to get number of racers
    param: None
    return: integer of the number of racers
    """
    turtle_number = 0
    while True:
        turtle_number = input("Enter the number of turtles you want(2 - 10): ")
        if turtle_number.isdigit():
            turtle_number = int(turtle_number)
        else:
            print('You entered a non numberic input. Please input again!')
            continue
        if 2 <= turtle_number <= 10:
            return turtle_number
        else:
            print('Your input is out of range (2 - 10). Please try again!')


def init_screen():
    """
    Turtle Screen initializer
    param: None
    return: None
    """
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor('black')
    screen.title('Turtle Racer')


def create_turtles(colors):
    """
    Function that create the turtle objects
    param: colors -> an array that holds the different colors
    return: turtles -> an array of turtle objects
    """
    turtles = []
    init_pos = HEIGHT//(len(colors) + 1)
    for i, color in enumerate(colors):
        t = turtle.Turtle()
        t.color(color)
        t.shape('turtle')
        t.penup()
        # t.setpos(-HEIGHT//2 + (i+1)*init_pos, -WIDTH//2 + 20)
        t.setpos(-WIDTH//2 + 20, HEIGHT//2 - (i+1)*init_pos)
        t.pendown()
        turtles.append(t)

    return(turtles)


def race_turtles(colors):
    """
    Function that controls the racing
    param: colors -> an array that holds the different colors
    return: colors[i] -> the color of the winner
    """
    turtles = create_turtles(colors)
    while True:
        for t in turtles:
            distance = random.randrange(1, 20)
            t.forward(distance)
            x, y = t.pos()
            if x >= WIDTH//2 - 10:
                return colors[turtles.index(t)]


def welcome_msg():
    print('Welcome to turtle race simulator.\nHave fun!!!')


def winner_msg(winner):
    print(f'Congratulations the winner is: {winner.upper()}')


def main():
    welcome_msg()
    random.shuffle(COLORS)
    turtle_num = get_turtle_amount()
    colors = COLORS[:turtle_num]
    print(colors)
    init_screen()
    winner = race_turtles(colors)
    winner_msg(winner)
    time.sleep(3)


main()
