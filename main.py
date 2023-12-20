import time
from turtle import Screen,Turtle
from car_manager import CarManager
from scoreboard import Scoreboard

tim = Turtle()
tim.shape("turtle")
tim.setheading(90)
tim.penup()
tim.goto(0,-240)
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)



def move_forwards():
    tim.forward(20)


screen.listen()
screen.onkey(move_forwards, "Up")

car_manager=CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    if tim.ycor()>250:
       tim.goto(0, -240)
       car_manager.level_up()
       scoreboard.increase_score()

    screen.update()
    screen.listen()
    screen.onkey(move_forwards, "Up")

    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(tim) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()