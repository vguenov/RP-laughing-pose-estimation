import string

import numpy as np
from webencodings import labels


class Point:
    def __init__(self, x, y, point_index, label):
        self.point_index = point_index
        self.x = x
        self.y = y
        self.label = label

    def isNone(self):
        return self.x is None or self.y is None

    @staticmethod
    def populate(xs : list, labelList : list):
        assert (len(xs) % 2 == 0)

        points = []
        for i in range (len(xs)//2):
            points.append(Point(xs[2*i], xs[2*i+1], i, labelList[i]))

        return points

