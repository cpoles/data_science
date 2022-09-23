"""Solution to Ellen's Alien Game exercise."""


def new_aliens_collection(list):
    return [Alien(x, y) for x, y in list]


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    # class attribute
    total_aliens_created = 0

    def __init__(self, x, y):
        self.__x_coordinate = x
        self.__y_coordinate = y
        self.__health = 3
        Alien.total_aliens_created += 1

    # properties
    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, level):
        self.__health = level

    @property
    def x_coordinate(self):
        return self.__x_coordinate

    @x_coordinate.setter
    def x_coordinate(self, x):
        self.__x_coordinate = x

    @property
    def y_coordinate(self):
        return self.__y_coordinate

    @y_coordinate.setter
    def y_coordinate(self, y):
        self.__y_coordinate = y

    # methods
    def hit(self):
        if self.health > 0:
            self.health -= 1

    def is_alive(self):
        return True if self.health > 0 else False

    def teleport(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y

    def collision_detection(self, object):
        pass
