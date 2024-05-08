import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(fun=player.move_up, key='Up')

car_mgr = CarManager()

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.display_scoreboard()
    car_mgr.create_car()
    car_mgr.move_cars()
    for i in car_mgr.all_cars:
        if (abs(player.xcor() - i.xcor()) < 30) and (abs(player.ycor() - i.ycor()) < 10):
            game_is_on = False
            scoreboard.display_game_over()
    if player.finished_level():
        player.go_to_next_level()
        car_mgr.increment_speed()
        scoreboard.increment_scoreboard()

screen.exitonclick()