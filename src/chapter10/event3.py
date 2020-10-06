import turtle

# create window
turtle.setup(400,600)
wn = turtle.Screen()
wn.title("key movement")
wn.bgcolor("lightgreen")

# Create turtle
tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)

alex = turtle.Turtle()
alex.color("red")
alex.pensize(6)
alex.forward(100)

# define mouse function

def tess_event(x,y):
    wn.title("tess coords {0}, {1}".format(x,y))
    tess.left(45)
    tess.forward(50)

def alex_event(x,y):
    wn.title("alex coords {0}, {1}".format(x, y))
    alex.right(40)
    alex.forward(50)

# exit

tess.onclick(tess_event)
alex.onclick(alex_event)
wn.mainloop()