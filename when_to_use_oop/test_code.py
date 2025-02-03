import math
from typing import List


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p2: "Point"):
        return math.sqrt((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2)


class Polygon:
    def __init__(self, points: List[tuple] = None):
        points = points if points else []
        self.vertices = []
        for point in points:
            if isinstance(point, tuple):
                point = Point(*point)  # Spread operation
            self.vertices.append(point)

    def add_point(self, point: Point):
        self.vertrices.append(point)

    def perimeter(self):
        perimeter = 0
        points: List[Point] = self.vertices + [self.vertices[0]]
        for i in range(len(self.vertrices)):
            perimeter += points[i].distance(points[i + 1])
        return perimeter


class Color:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name

    def _set_name(self, name):
        if not name:
            raise Exception("Invalid Name")
        self._name = name

    def _get_name(self):
        return self._name

    name = property(_get_name, _set_name)


class Foo:
    _foo = None

    @property
    def foo(self):
        return self._foo

    @foo.setter
    def foo(self, value):
        self._foo = value + " From Foo"


class Silly:
    _silly = None

    @property
    def silly(self):
        """This is a silly property"""
        print("You are getting silly")
        return self._silly

    @silly.setter
    def silly(self, value):
        print(f"Value of silly changed to {value}")
        self._silly = value

    @silly.deleter
    def silly(self):
        print("Killed Silly!!!")
        del self._silly


from urllib.request import urlopen


class WebPage:
    def __init__(self, url):
        self.url = url
        self._content = None

    @property
    def content(self):
        if not self._content:
            print("Retrieving new page")
            self._content = urlopen(self.url).read()
        return self._content


class AverageList(list):
    @property
    def average(self):
        return sum(self) / len(self)


import time

webpage = WebPage("https://tgs.alumniconnect.xyz")
now = time.time()
content1 = webpage.content
print(time.time() - now)
now = time.time()
content2 = webpage.content
print(time.time() - now)
print(content1 == content2)
