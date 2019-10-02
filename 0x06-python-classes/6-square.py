#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        if (not isinstance(position, tuple) or len(position) != 2 or not
                isinstance(position[0], int) or not
                isinstance(position[1], int) or
                position[0] < 0 or position[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__size = size
        self.__position = position

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or not
                isinstance(value[0], int) or not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for d in range(self.__position[1]):
            print()
        for a in range(self.__size):
            for c in range(self.__position[0]):
                print(' ', end="")
            for b in range(self.__size):
                print('{}'.format('#'), end="")
            print()
