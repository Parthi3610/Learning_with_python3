import turtle

def draw_square(t, sz, an):
    '''function to draw square'''
    for i in range(4):
        t.forward(sz)
        t.right(an)


wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.title('turtle square')

alex = turtle.Turtle()
draw_square(alex,50, 90)

wn.mainloop()