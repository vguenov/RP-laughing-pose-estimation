from Point import Point
class SkeletonEdge:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
        if "head" in p1.label or "head" in p2.label:
            self.color = "red"
        elif "Shoulder" in p1.label or "Shoulder" in p2.label or "Wrist" in p1.label or "Wrist" in p2.label:
            self.color = "blue"
        else:
            self.color = "green"

    def isNone(self):
        return self.p1 is None or self.p2 is None

