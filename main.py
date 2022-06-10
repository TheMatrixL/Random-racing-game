from turtle import Turtle, Screen
import random

FONT = ("Arial", 30, "normal")

class Finish_line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pensize(5)
        self.penup()
        self.goto(300, -800)
        self.pendown()
        self.goto(300, 800)
        self.penup()

class Result(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-50, -50)

    def you_lose(self):
        self.pencolor("red")
        self.write(f"You lose!\n{win_team.capitalize()}\nWin the race!", align="center", font=FONT)

    def you_win(self):
        self.pencolor("green")
        self.write(f"You win!\n{win_team.capitalize()}\nWin the race!", align="center", font=FONT)


is_race_on = False
screen = Screen()
screen.setup(width=1000, height=800)
screen.bgcolor("#F1EEE9")
screen.title("Random racing game!")
screen.onclick("click me")

teams = ["ferrari", "mercedes", "redbull", "mclaren", "alpine", "astonmartin", "alphatauri", "alfaromeo", "haas", "williams"]
team1 = {1: "ferrari", 2: "mercedes", 3: "redbull", 4: "mclaren", 5: "alpine", 6: "astonmartin", 7: "alphatauri", 8: "alfaromeo", 9: "haas", 10: "williams"}


user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which team will win the race? Choose a team below:\n"
            "Ferrari\nMercedes\nRedbull\nMclaren\nAlpine\nAstonmartin\nAlphatauri\nAlfaromeo\nHaas\nWilliams").lower()


y_position = -350
all_teams = {}

for team in teams:
    y_position += 60
    screen.register_shape(f"img/{team}.gif", shape=None)
    t = Turtle(f"img/{team}.gif")
    t.penup()
    t.goto(x=-430, y=y_position)
    all_teams[team] = t

if user_bet:
    is_race_on = True
    Finish_line()

while is_race_on:
    for team, t in all_teams.items():
        if t.xcor() > 250:
            is_race_on = False
            win_team = team
            if win_team == user_bet:
                Result().you_win()
            else:
                Result().you_lose()
        t.fd(random.randint(0, 20))


screen.exitonclick()
