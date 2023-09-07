import turtle
import random

score = 0
time = 15
game_status = True

screen = turtle.Screen()
screen.bgcolor("light blue")
window_height = screen.window_height() / 2


turtle.tracer(0)

score_text = turtle.Turtle()
catch_turtle = turtle.Turtle()
time_text = turtle.Turtle()

def set_timer():
    global time
    global game_status

    if time != 0:
        turtle.tracer(0)
        time_text.hideturtle()
        time_text.penup()
        time_text.setpos(0,window_height * 0.70)
        time_text.clear()
        time_text.write("Time : {}".format(time), move=False, align="center", font=("Cooper Black", 25, "italic"))
        time = time - 1
        screen.ontimer(set_timer,1000)
        turtle.tracer(1)
    else:
        time_text.clear()
        time_text.write("Game Over !", move=False, align="center", font=("Cooper Black", 25, "italic"))
        game_status = False


def set_score_text():

    score_text.hideturtle()
    score_text.penup()
    score_text.setpos(0, window_height * 0.85)
    score_text.write("Score : {}".format(score), move=False, align="center", font=("Cooper Black", 25, "italic"))

def set_turtle():

    catch_turtle.shape("turtle")
    catch_turtle.shapesize(2)
    catch_turtle.color("green")
    catch_turtle.onclick(increase_score)

def set_random_pos():

    if game_status:
        turtle.tracer(0)
        screen.ontimer(set_random_pos, 500)
        catch_turtle.penup()
        catch_turtle.hideturtle()
        x = random.randint(-250,250)
        y = random.randint(-200,170)
        catch_turtle.goto(x,y)
        catch_turtle.showturtle()
        turtle.tracer(1)
    else:
        catch_turtle.hideturtle()

def increase_score(x,y):

    global score
    score = score + 1
    score_text.clear()
    set_score_text()


def start_game():

    set_score_text()
    set_timer()
    set_turtle()
    set_random_pos()


start_game()

turtle.tracer(1)

turtle.mainloop()

