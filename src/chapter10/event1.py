import turtle

""" create window"""
turtle.setup(400,600)
wn = turtle.Screen()
wn.title("key movement")
wn.bgcolor("lightgreen")

"""  create turtle"""

tess = turtle.Turtle()

""" capture keys """

def keyup():
    tess.forward(50)

def keyright():
    tess.right(90)

def keyleft():
    tess.left(45)

def quit():
    wn.bye()

""" key function """

wn.onkey(keyup, "Up")
wn.onkey(keyright, "Right")
wn.onkey(keyleft, "Left")
wn.onkey(quit, "q")

""" exit prog"""

wn.listen()
wn.mainloop()