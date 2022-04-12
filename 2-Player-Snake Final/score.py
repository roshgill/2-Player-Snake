from turtle import Turtle
"Create the Score class, its color, shape and position"
"Everytime a snake eats the food, the score will delete and reset with the updated numbers"
"Once the game ends, the game will stop and the winner shall be announced"
class Score():
    def __init__(self):
        self.score1 = Turtle()
        self.score_1 = 0
        self.score1.color("grey")
        self.score1.penup()
        self.score1.goto(-200, 270)
        self.update_scoreboard()
        self.score1.hideturtle()
        
        self.score2 = Turtle()
        self.score_2 = 0
        self.score2.color("tan")
        self.score2.penup()
        self.score2.goto(200, 270)
        self.update_scoreboard2()
        self.score2.hideturtle()

    def update_scoreboard(self):
        self.score1.write(f"Player 1: {self.score_1}", align="center",
        font=("Arial", 24, "normal"))
        
    def update_scoreboard2(self):
        self.score2.write(f"Player 2: {self.score_2}", align="center",
        font=("Arial", 24, "normal"))
    
    def game_over(self, snake_num):
        self.game_over = Turtle()
        if snake_num == 1:
            color = "grey"
        else:
            color = "tan"
        self.game_over.color(color)
        self.game_over.goto(0, 200)
        self.game_over.write(f"CALL ME DADDY", align="center",
        font=("Arial", 30, "normal"))
    
    def increase_score(self, snake_num):
        if snake_num == 1:
            self.score_1 += 1
            self.score1.clear()
            self.update_scoreboard()
        else:
            self.score_2 += 1
            self.score2.clear()
            self.update_scoreboard2()