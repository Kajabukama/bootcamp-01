# super class Shape which in herits an object
# the class is not implemented

class Shape(object):
    def paint(self, canvas): 
    	pass


# class canvas which in herits an object
# the class is not implemented
class Canvas(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [[' '] * width for i in range(height)]

    # setter method which sets row and column
    def setpixel(self, row, col):
        self.data[row][col] = '*'

    # getter method that will get the values of row and column
    def getpixel(self, row, col):
        return self.data[row][col]

    def display(self):
        print "\n".join(["".join(row) for row in self.data])

# the subclass Rectangle which inherits from the Shape Superclass
# inheritance concept

class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    # a method to draw a horizontal line
    def hline(self, x, y, w):
        self.x = x
        self.y = y
        self.w = w

    # another method that will draw a vertical line
    def vline(self, x, y, h):
        self.x = x
        self.y = y
        self.h = h

    # this method calls the other three methods 
    # and draws the respective shapes on a camnvas

    def paint(self, canvas):
        hline(self.x, self.y, self.w)
        hline(self.x, self.y + self.h, self.w)
        vline(self.x, self.y, self.h)
        vline(self.x + self.w, self.y, self.h)