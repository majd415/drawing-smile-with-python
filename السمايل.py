import turtle
def maya(c,r,z):
     g=0
     while(g<180):
           c.forward(r)
           c.left(z)
           c.color("blue")
           g=g+1
a=turtle.Screen()
b=turtle.Turtle()
b.speed(0)

maya(b,4,2)
b.penup()
b.left(90)
b.forward(60)
b.pendown()

b.right(45)
b.forward(20)
b.backward(20)
b.left(90)
b.forward(20)
b.right(45)

b.penup()
b.forward(30)

b.pendown()

b.right(90)
b.forward(30)
b.left(120)
b.forward(30)
b.left(120)
b.forward(30)
b.penup()
b.right(120)
b.forward(60)
b.pendown()
maya(b,2,5)
b.penup()
b.left(55)
b.forward(140)
b.pendown()
maya(b,2,5)


a.mainloop()