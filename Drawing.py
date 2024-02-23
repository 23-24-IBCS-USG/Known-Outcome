import turtle

def triangle(t,size):
    for i in range(3):
         t.forward(size)
         t.left(120)

def square(t,size):
    for i in range(4):
        t.forward(size)
        t.right(90)

def circle(t,size):
    for i in range(180):
        t.forward(size)
        t.right(2)

def pentagon(t,size):
    for i in range(5):
        t.forward(size)
        t.right(72)

def starcrossed(t,size):
    for i in range(5):
        t.forward(size)
        t.right(180-36)
        t.forward(size)
        t.right(72)

def star(t,size):
    for i in range(5):
        t.left(252-180)
        t.forward(size)
        t.right(180-36)
        t.forward(size)

def polygon(side, size):
    ang = 360 / side
    for i in range(side):
        turtle.forward(size)
        turtle.right(ang)

def main():
    win = turtle.Screen()
    t = turtle.Turtle()
    
    t.penup()
    t.goto(0,-200)
    t.pendown()
    square(t,100)
    
    t.penup()
    t.goto(100,200)
    t.pendown()
    triangle(t,100)

    t.penup()
    t.goto(200,100)
    t.pendown()
    circle(t,2)

    t.penup()
    t.goto(-200,0)
    t.pendown()
    pentagon(t,100)

    t.penup()
    t.goto(-100,100)
    t.pendown()
    starcrossed(t,100)

    t.penup()
    t.goto(-200,200)
    t.pendown()
    star(t,50)

    t.penup()
    t.goto(0,0)
    t.pendown()
    polygon(10,50)
if __name__ == "__main__":
    main()
