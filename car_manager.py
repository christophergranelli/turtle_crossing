from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_choice = random.randint(1,6)
        if random_choice == 1:
            car = Turtle('square')
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            randy = random.randint(-250, 250)
            car.goto(300, randy)
            self.all_cars.append(car)

    def move_cars(self):
        for i in self.all_cars:
            i.backward(self.car_speed)

    def increment_speed(self):
        self.car_speed += MOVE_INCREMENT






