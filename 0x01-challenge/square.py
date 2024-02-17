#!/usr/bin/python3

class Square():
    
    side = 0

    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area(self):
        """ Area of the square """
        return self.side * self.side

    def perimeter(self):
        """ Perimeter of the square """
        return 4 * self.side
     

    def __str__(self):
        return "Side length: {}".format(self.side)

if __name__ == "__main__":

    s = Square(side=12)
    print(s)
    print("Area:", s.area())
    print("Perimeter:", s.perimeter())
