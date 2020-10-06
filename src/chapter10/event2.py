import turtle

# create window

turtle.setup(400,600)
wn = turtle.Screen()
wn.title("key movement")
wn.bgcolor("lightgreen")

# Create turtle
tess = turtle.Turtle()
tess.color("blue")
tess.pensize(10)

# define mouse function

def mouse_event(x,y):
    wn.title("Clicked at coords {0}, {1}".format(x,y))
    tess.goto(x,y)




# exit

wn.onclick(mouse_event)
wn.mainloop()