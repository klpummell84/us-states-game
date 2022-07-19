from turtle import Turtle
import pandas as pd

FONT = ("Arial", 8, "bold")

class Master:
    def __init__(self):
        self.__score = 0
        self.__total_states = 50
        self.__states = pd.read_csv("50_states.csv")
        self.should_quit = False

    @property
    def states(self):
        return self.__states

    @property
    def score(self):
        return self.__score

    @property
    def num_states(self):
        return self.__total_states

    def increment_score(self):
        self.__score += 1

    @property
    def show_score(self):
        return f"{self.score}/{self.__total_states}"

    def check_guess(self, guess: str):
        for i in self.states.state:
            if i == guess:
                self.create_state_name(i, float(self.states[self.states.state == i].x),
                                         float(self.states[self.states.state == i].y))
                self.increment_score()

    @staticmethod
    def create_state_name(name: str, x: float, y: float, font: tuple[str, int, str] = FONT):
        StateName(name, x, y, font)


class StateName(Turtle):
    def __init__(self, state_name: str,  x_pos: float, y_pos: float, font: tuple[str, int, str]):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x_pos, y_pos)
        self.write(state_name, font=font)
