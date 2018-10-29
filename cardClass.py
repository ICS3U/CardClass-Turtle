import turtle

pen = turtle.Pen()
turtle.Screen().setup(400, 600)
turtle.Screen().bgcolor('white')


class Card:
    SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
    RANKS = ('narf', 'Ace', '2', '3', '4', '5', '6', '7',
             '8', '9', '10', 'Jack', 'Queen', 'King')

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """
          >>> print(Card(2, 11))
          Queen of Hearts
        """
        return '{0} of {1}'.format(Card.RANKS[self.rank],
                                   Card.SUITS[self.suit])
    def draw_image(self):
        pen.up()
        pen.setpos(-150, 250)
        pen.down()
        pen.write(self.rank, font=("Arial", 20, "normal"))

        pen.up()
        pen.setpos(150, -250)
        pen.left(30)
        pen.down()
        pen.write(self.rank, font=("Arial", 20, "normal"))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
