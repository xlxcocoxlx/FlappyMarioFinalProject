from time import sleep
import turtle
from turtle import *

class Hello:
    def helloScreen():
        hideturtle()
        Screen().bgcolor("cyan")
        speed(100)
        pensize(10)
        penup()
        left(90)
        forward(180)
        left(90)
        forward(280)
        left(90)
        pendown()
        forward(300)
        left(180)
        forward(150)
        right(90)
        forward(150)
        left(90)
        forward(150)
        left(180)
        forward(300)
        left(90)
        penup()
        forward(100)
        pendown()
        forward(200)
        backward(100)
        left(90)
        forward(300)
        left(90)
        forward(100)
        backward(200)
        penup()
        
        
Hello.helloScreen()
sleep(3)