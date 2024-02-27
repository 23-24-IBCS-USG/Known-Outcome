import turtle

def hair(t,size):
    for i in range(180):
        t.forward(size)
        t.right(2)


def hair2(t,size):
    for i in range(4):
        t.forward(size)
        t.right(90)

def face(t,size):
    for i in range(180):
        t.forward(size)
        t.right(2)

def ears(t,size):
    for i in range(180):
        t.forward(size)
        t.right(2)

def bang(t,size):
    for i in range(4):
        t.forward(size)
        t.right(90)

def neck(t,size):
    for i in range(4):
        t.forward(size)
        t.right(90)

def blush(t,size):
    for i in range(180):
        t.forward(size)
        t.right(2)

def eyes(t,size):
    for i in range(180):
        t.forward(size)
        t.right(2)

def nose(t,size):
    for i in range(3):
         t.forward(size)
         t.left(120)

def mouth(t,size):
    for i in range(180):
        t.forward(size)
        t.right(2)


def main():
    win = turtle.Screen()
    t = turtle.Turtle()

    t.goto(0,210)
    t.color("brown")
    t.pendown()
    t.begin_fill()
    hair(t,8)
    t.end_fill()
    t.penup()

    t.goto(-250,-110)
    t.color("white")
    t.pendown()
    t.begin_fill()
    bang(t,500)
    t.end_fill()
    t.penup()

    t.goto(0,200)
    t.color("cornsilk")
    t.pendown()
    t.begin_fill()
    face(t,5)
    t.end_fill()
    t.penup()

    t.goto(100,100)
    t.color("cornsilk")
    t.pendown()
    t.begin_fill()
    ears(t,2)
    t.end_fill()
    t.penup()

    t.goto(-100,100)
    t.color("cornsilk")
    t.pendown()
    t.begin_fill()
    ears(t,2)
    t.end_fill()
    t.penup()

    t.goto(-40,0)
    t.color("cornsilk")
    t.pendown()
    t.begin_fill()
    neck(t,100)
    t.end_fill()
    t.penup()

    t.goto(-70,30)
    t.color("pink")
    t.pendown()
    t.begin_fill()
    blush(t,1)
    t.end_fill()
    t.penup()

    t.goto(70,30)
    t.color("pink")
    t.pendown()
    t.begin_fill()
    blush(t,1)
    t.end_fill()
    t.penup()

    t.goto(50,50)
    t.color("black")
    t.pendown()
    t.begin_fill()
    eyes(t,0.5)
    t.end_fill()
    t.penup()

    t.goto(-50,50)
    t.color("black")
    t.pendown()
    t.begin_fill()
    eyes(t,0.5)
    t.end_fill()
    t.penup()

    t.goto(-10,0)
    t.color("brown")
    t.pendown()
    t.begin_fill()
    nose(t,20)
    t.end_fill()
    t.penup()

    t.goto(0,-3)
    t.color("red")
    t.pendown()
    t.begin_fill()
    mouth(t,1)
    t.end_fill()
    t.penup()

    t.goto(0,0)
    t.color("cornsilk")
    t.pendown()
    t.begin_fill()
    mouth(t,1)
    t.end_fill()
    t.penup()

if __name__ == "__main__":
    main()
