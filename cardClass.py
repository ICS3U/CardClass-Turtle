import turtle


class Card:
    SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
    RANKS = ('narf', 'Ace', '2', '3', '4', '5', '6', '7',
             '8', '9', '10', 'Jack', 'Queen', 'King')

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def draw(self):
        if self.rank == '9':
            t.setheading(0)
            t.penup()
            t.setpos(-210, 170)
            t.pendown()
            t.write("9", align="center", font=("Arial", 40, "normal"))
            t.penup()
            t.setpos(210, -230)
            t.pendown()
            t.right(180)
            t.write("6", align="center", font=("Arial", 40, "normal"))

        if self.rank == '10':
            t.setheading(0)
            t.penup()
            t.setpos(-210, 170)
            t.pendown()
            t.write("I0", align="center", font=("Arial", 40, "normal"))
            t.penup()
            t.setpos(210, -230)
            t.pendown()
            t.right(180)
            t.write("0Ɩ", align="center", font=("Arial", 40, "normal"))

        if self.rank == 'Jack':
            t.setheading(0)
            t.penup()
            t.setpos(-210, 170)
            t.pendown()
            t.write("J", align="center", font=("Arial", 40, "normal"))
            t.penup()
            t.setpos(210, -230)
            t.pendown()
            t.right(180)
            t.write("ſ", align="center", font=("Arial", 40, "normal")
        
         if self.rank == 'Clubs'
            t.left(90)
            t.forward(100)
            t.dot(150, "black")
            t.right(180)
            t.forward(100)
            t.right(90)
            t.back(50)
            t.dot(150, "black")
            t.forward(100)
            t.dot(150, "black")
            t.back(50)
            t.left(70)
            t.begin_fill()
            t.width(20)
            t.forward(150)
            t.left(110)
            t.forward(100)
            t.left(110)
            t.forward(100)
            t.end_fill()

# Program variables
screen_width = 500
screen_height = 500

# Sets up screen
screen = turtle.Screen()  # Creates screen object
screen.setup(screen_width, screen_height)  # Sets screen size
screen.colormode(255)  # Allows RGB values to be used as colours
screen.bgcolor([255, 255, 255])

# Sets up turtle
t = turtle.Turtle()  # Creates turtle object
t.pensize(2)
t.pencolor([0, 0, 0])
t.speed(0)

screen.exitonclick()  # Keeps screen open until mouse is clicked
