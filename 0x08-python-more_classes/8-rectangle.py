#!/usr/bin/python3
class Rectangle:

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not(isinstance(value, int)):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not(isinstance(value, int)):
            raise TypeError('height must be an integer')
        if value < 0:
            raise TypeError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        rect = ""
        for a in range(self.__height):
            if a == self.__height - 1:
                rect += str(self.print_symbol) * self.__width
            else:
                rect += str(self.print_symbol) * self.__width + '\n'
        return rect

    def __repr__(self):
        return "Rectangle({}, {})".format(eval(str(self.__width)),
                                          eval(str(self.__height)))

    def __del__(self):
        print('{}'.format('Bye rectangle...'))
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() == rect_2.area():
            return rect_1.area()
        else:
            return rect_2.area()
