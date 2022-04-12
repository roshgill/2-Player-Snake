"""2 Player Snake involves both snakes racing for food. The snake to reach 21 wins.
Also, if either snake touches the wall or itself, it loses."""

"Import the the Screen class from the turtle module, the created snake food and score classes"
"Also import the time class"
from turtle import Screen
from snake import Snakes
from food import Food
from score import Score
import time

"Create snake dictionaries that will hold the color of the snake and its starting postion"
"This information will be used when we create our snakes"
snake1_dict = {
    'color':"grey",
    'starting_position': [(0, 0), (-20, 0), (-40, 0)]
}

snake2_dict = {
    'color':"tan",
    'starting_position': [(0, -40), (-20, -40), (-40, -40)]
}

"Initialize the screen and all specified features"
main_screen = Screen()
main_screen.setup(width=700, height=595)
main_screen.bgcolor("black")
main_screen.title("Snake")
main_screen.tracer(0)

"Initialize snakes, food_dots, and score objects from respective classes"
snake1 = Snakes(snake1_dict)
snake2 = Snakes(snake2_dict)
food_dots = Food()
score = Score()

# "Screen.listen monitors if certain keys are pressed"
# "Furthermore, specific functions will be called to move the snakes a certain way"
main_screen.listen()
main_screen.onkey(snake1.up, "w")
main_screen.onkey(snake1.down, "s")
main_screen.onkey(snake1.left, "a")
main_screen.onkey(snake1.right, "d")

main_screen.onkey(snake2.up, "i")
main_screen.onkey(snake2.down, "k")
main_screen.onkey(snake2.left, "j")
main_screen.onkey(snake2.right, "l")

# "Infinite loop is used to keep game running continuously"
game_is_on = True
# """1. Update the screen every time through the loop
# 2. Move the snakes, check for collision with food and the wall
# 3. Also check for collisions with ones own tail
# 4. Depending on the circumstance, specfic code will run in regards
# to updating the score, and if the game should end"""
while game_is_on:
    main_screen.update()
    time.sleep(0.1)

    snake1.move()
    snake2.move()
    
    #Detect collision with food
    if snake1.head.distance(food_dots) < 15:
        food_dots.refresh()
        snake1.extend()
        score.increase_score(1)
        if score.score_1 == 21:
            game_is_on = False
            score.game_over(1)
            
    elif snake2.head.distance(food_dots) < 15:
        food_dots.refresh()
        snake2.extend()
        score.increase_score(2)
        if score.score_2 == 21:
            game_is_on = False
            score.game_over(2)
    
    #Detect collision with tail
    for segment in snake1.segments[1:]:
        if snake1.head.distance(segment) < 10:
            game_is_on = False
            score.game_over(2)
    
    for segment in snake2.segments[1:]:
        if snake2.head.distance(segment) < 10:
            game_is_on = False
            score.game_over(1)
    
    #Detect collision with wall
    if snake1.head.xcor() > 355 or snake1.head.xcor() < -355 or snake1.head.ycor() > 300 or snake1.head.ycor() < -300:
        game_is_on = False
        score.game_over(2)
    elif snake2.head.xcor() > 355 or snake2.head.xcor() < -355 or snake2.head.ycor() > 300 or snake2.head.ycor() < -300:
        game_is_on = False
        score.game_over(1)
        
main_screen.exitonclick()