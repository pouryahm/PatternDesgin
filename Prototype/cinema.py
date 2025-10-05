from sys import dont_write_bytecode


class Cinema:
    # This Class have NAME ADDRESS and ... in __init__

    pass


class Movie:
    # This Class have NAME DIRECTOR and ... in __init__
    pass


class Time:
    # This Class have Start_time End time  and ... in __init__
    pass


class Hall:
    def __init__(self, name, cinema, capacity):
        self.cinema = cinema
        self.capacity = capacity 
        self.name = name


class Seat:
    def __init__(self, number):
        self.number = number
        self.status = None


class Sans:
    def __init__(self, cinema, movie, time, hall, ):
        self.cinema = cinema
        self.movie = movie
        self.time = time
        self.hall = hall
        self.seats = list()
        self.prototype_seats()

    def prototype_seats(self):
        """Prototype all seats for selected hall"""
        for i in range(self.hall.capacity):
            self.seats.append(Seat(i))


if __name__ == "__main__":
    cinema = Cinema()
    movie = Movie()
    time = Time()
    hall = Hall("hall name", cinema, 50)

    sans = Sans(cinema, movie, time, hall)
    print(len(sans.seats))
    print(type(sans.seats[0]))