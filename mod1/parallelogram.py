from quadrilateral import Quadrilateral

class Parallelogram(Quadrilateral):
    def __init__(self, base, height, side,name="Parallelogram"):
        super().__init__()
        self.figure_type = "Parallelogram"
        self.side_lengths = [base, side]
        self.height = height
        self.vertices = [(0, 0), (base, 0), (base + side, height), (side, height)]
        self.calculate_perimeter()
        self.calculate_area()
        self.calculate_diagonals_lengths()
        self.calculate_angle_measures()
        self.name = name

    def calculate_perimeter(self):
        self.perimeter_value = sum(self.side_lengths) * 2

    def calculate_area(self):
        self.area_value = self.side_lengths[0] * self.height

    def calculate_diagonals_lengths(self):
        self.diagonals_lengths = [None, None]

    def calculate_angle_measures(self):
        self.angle_measures = [None, None, None, None]
