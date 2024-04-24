from quadrilateral import Quadrilateral

class Trapezoid(Quadrilateral):
    def __init__(self, base1, base2, height, side1, side2,name="Trapezoid"):
        super().__init__()
        self.figure_type = "Trapezoid"
        self.side_lengths = [base1, base2, side1, side2]
        self.height = height
        self.vertices = [(0, 0), (base1, 0), (base2 + side2, height), (side1, height)]
        self.calculate_perimeter()
        self.calculate_area()
        self.calculate_diagonals_lengths()
        self.calculate_angle_measures()
        self.name = name

    def calculate_perimeter(self):
        self.perimeter_value = sum(self.side_lengths)

    def calculate_area(self):
        self.area_value = (self.side_lengths[0] + self.side_lengths[1]) * self.height / 2

    def calculate_diagonals_lengths(self):
        self.diagonals_lengths = [None, None]

    def calculate_angle_measures(self):
        self.angle_measures = [None, None, None, None]
