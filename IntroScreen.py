# import turtle
from time import sleep
import turtle
from turtle import *

class instructionText():
    def instructions():
        title("Instructions")
        clear()
        home()
        Screen().bgcolor("cyan")
        color("red")
        penup()
        style = ("Arial", 40, "italic")
        write("Press Up Arrow or", font = style, align = "center")
        right(90)
        forward(50)
        left(90)
        write("Space to Start!", font = style, align = "center")
instructionText.instructions()
sleep(2)