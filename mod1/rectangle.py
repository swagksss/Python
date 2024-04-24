from quadrilateral import Quadrilateral
import math

from quadrilateral import Quadrilateral

class Rectangle(Quadrilateral):
    def __init__(self, length, width, name="Rectangle"):
        super().__init__()
        self.figure_type = "Rectangle"
        self.name = name
        self.side_lengths = [length, width]
        self.vertices = [(0, 0), (length, 0), (length, width), (0, width)]
        self.calculate_perimeter()
        self.calculate_area()
        self.calculate_diagonals_lengths()
        self.calculate_angle_measures()
        self.check_properties()

    def calculate_perimeter(self):
        self.perimeter_value = 2 * (self.side_lengths[0] + self.side_lengths[1])

    def calculate_area(self):
        self.area_value = self.side_lengths[0] * self.side_lengths[1]

    def calculate_diagonals_lengths(self):
        self.diagonals_lengths = [math.sqrt(self.side_lengths[0] ** 2 + self.side_lengths[1] ** 2),
                                  math.sqrt(self.side_lengths[0] ** 2 + self.side_lengths[1] ** 2)]

    def calculate_angle_measures(self):
        self.angle_measures = [90, 90, 90, 90]

    def check_properties(self):
        if self.side_lengths[0] == self.side_lengths[1]:
            print("It's a square!")

    def get_subtypes(self):
        return [self.figure_type]
