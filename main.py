from turtle import Turtle, Screen
from random import choice, randint
from tkinter import messagebox


class Race:
    cars = []

    def __init__(self):
        self.winning_color = None
        for _ in range(len(RacingTurtle.available_colors)):
            self.cars.append(RacingTurtle())
            self.cars[_].print_turtle()

    def start(self):
        is_race_finished = False
        while not is_race_finished:
            for car in self.cars:
                car.move()
                if car.is_turtle_winning():
                    is_race_finished = True
                    self.winning_color = car.get_color()
        print(f"The winner is {self.winning_color}!")

    def get_winner(self):
        return self.winning_color


class RacingTurtle:
    available_colors = ["red", "green", "blue", "yellow", "orange"]
    INITIAL_X = -300
    INITIAL_Y = -100
    DEFAULT_STEP = 30

    def __init__(self):
        self.turtle = Turtle()
        self.turtle.up()
        self.set_color()
        self.set_x()
        self.set_y()

    def set_x(self):
        self.turtle.setx(self.INITIAL_X)

    def set_y(self):
        y = self.INITIAL_Y + len(self.available_colors) * 50
        self.turtle.sety(y)

    def set_color(self):
        self.turtle.color(self.pick_and_remove_color())

    def pick_and_remove_color(self):
        color = choice(self.available_colors)
        self.available_colors.remove(color)
        return color

    def print_turtle(self):
        print(f"Color {self.turtle.color()}")

    def move(self):
        self.turtle.forward(self.random_step())

    def random_step(self):
        return randint(1, self.DEFAULT_STEP)

    def is_turtle_winning(self):
        print(f"X = {self.turtle.xcor()}")
        return self.turtle.xcor() >= abs(self.INITIAL_X)

    def get_color(self):
        return self.turtle.pencolor()


class Quiz:
    def __init__(self):
        self.user_choice = screen.textinput("Put your bet!", "Are you ready to bet?")
        self.winner = ""

    def print_the_winner(self):
        self.winner = race.get_winner()
        print(f"Answer {self.user_choice}, winner {self.winner}")
        message = f"Your choice was {self.user_choice}, the winner is {self.winner}.\n"
        if self.user_choice == self.winner:
            messagebox.showinfo("Who won?", f"{message}You won!")
        else:
            messagebox.showinfo("Who won?", f"{message}You lost!")


def game():
    global screen, race
    screen = Screen()
    quiz = Quiz()
    race = Race()
    race.start()
    quiz.print_the_winner()
    screen.exitonclick()


if __name__ == '__main__':
    game()
