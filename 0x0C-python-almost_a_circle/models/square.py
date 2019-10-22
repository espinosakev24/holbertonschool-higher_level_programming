#!/usr/bin/python3
""" Module of rectangle """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """contructor of the class
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ method __str__
        """
        return '[{}] ({}) {}/{} - {}'.format(
                self.__class__.__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ setting size
        """
        return self.width

    @size.setter
    def size(self, value):
        """ method size
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise TypeError('width must be > 0')
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ task 12 --> update, kwargs
        """
        len_ags = len(args)
        for d in range(0, len_ags):
            if d > len_ags:
                break
            if len_ags == 1:
                self.id = args[0]
            elif len_ags == 2:
                self.id = args[0]
                self.width = args[1]
            elif len_ags == 3:
                self.id = args[0]
                self.width = args[1]
                self.x = args[2]
            elif len_ags == 4:
                self.id = args[0]
                self.width = args[1]
                self.x = args[2]
                self.y = args[3]
        if not args:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.width = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """ task 14 --> dictionary representation of a square
        """
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
