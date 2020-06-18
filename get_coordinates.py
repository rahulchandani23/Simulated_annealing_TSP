import numpy



class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def get_distance(a,b):
        return numpy.sqrt(numpy.abs(a.x-b.x)+numpy.abs(a.y-b.y))
    @staticmethod
    def get_total_distance(coords):
        dist = 0
        for first, second in zip(coords[:-1],coords[1:]):
            dist+= Coordinate.get_distance(first,second)
        dist += Coordinate.get_distance(coords[0],coords[-1])
        return  dist

def coordinates(n):
    coords = []
    for i in range(n):
        coords.append(Coordinate(numpy.random.uniform(0, 100), numpy.random.uniform(0, 100)))

    return coords