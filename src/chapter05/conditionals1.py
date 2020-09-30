import turtle

def draw_graph(t,height):
    #define the graph pattern
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(" " + str(height))
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.forward(10)

wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.title('Graph')

tess = turtle.Turtle()
tess.pensize(5)
tess.color('blue','red')

xs = [100, 10, 250, 240, 50, 260, 200]

for a in xs:
    draw_graph(tess,a)

wn.mainloop()