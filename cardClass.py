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
   
    def clubs(self):
        import turtle
        turtle.setup(500, 700)
        t = turtle.Pen()
        if self.suit == True:
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


if __name__ == '__main__':
    import doctest
    doctest.testmod()
