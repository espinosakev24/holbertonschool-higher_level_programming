#!/usr/bin/python3
"""Module of first rectangle
"""


from models.base import Base


class Rectangle(Base):
    """ Class Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Contructor
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """setting widht"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting height"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """ Height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter of height
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    def area(self):
        """ task 4 --> rectangle area """
        return self.__height * self.__width

    def display(self):
        """ task 5 --> display function """
        for c in range(0, self.__y):
            print()
        for a in range(0, self.__height):
            print(self.__x * " ", end="")
            for b in range(0, self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """ task 6 --> __str__ function """
        return '[{}] ({:d}) {:d}/{:d} - {:d}/{:d}'\
            .format(self.__class__.__name__,
                    self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ task --> 9 update #1 """
        len_ags = len(args)
        for d in range(0, len_ags):
            if d > len_ags:
                break
            if len_ags == 1:
                self.id = args[0]
            elif len_ags == 2:
                self.id = args[0]
                self.__width = args[1]
            elif len_ags == 3:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
            elif len_ags == 4:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
            elif len_ags == 5:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
        if not args:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.__width = value
                if key == 'height':
                    self.__height = value
                if key == 'x':
                    self.__x = value
                if key == 'y':
                    self.__y = value

    def to_dictionary(self):
        """ task --> 13 dictionary definition of rectangle """
        return ({"x": self.__x, "y": self.__y, "id": self.id,
                "height": self.__height, "width": self.__width})

    @property
    def x(self):
        """setting x"""
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter of x """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """setting y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setting y"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value
