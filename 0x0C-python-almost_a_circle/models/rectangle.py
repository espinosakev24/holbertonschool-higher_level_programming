#!/usr/bin/python3
"""Module of first rectangle"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """setting widht"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    """setting height"""
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    """ task 4 --> rectangle area """
    def area(self):
        return self.__height * self.__width

    """ task 5 --> display function """
    def display(self):
        for a in range(0, self.__height):
            for b in range(0, self.__width):
                print('#', end="")
            print()

    """ task 6 --> __str__ function """
    def __str__(self):
        return '[{}] ({:d}) {:d}/{:d} - {:d}/{:d}'\
            .format(self.__class__.__name__,
                    self.id, self.__x, self.__y, self.__width, self.__height)

    """setting x"""
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    """setting y"""
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value
