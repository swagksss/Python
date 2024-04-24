from trapezoid import Trapezoid

class RectangularTrapezoid(Trapezoid):
    def __init__(self, base1, base2, height, side,name="RectangularTrapezoid"):
        super().__init__(base1, base2, height, side, side)
        self.figure_type = "Rectangular Trapezoid"
        self.check_properties()
        self.name = name

    def check_properties(self):
        if self.angle_measures[1] == 90 or self.angle_measures[2] == 90:
            print("It's a rectangular trapezoid!")

    def get_subtypes(self):
        return [self.figure_type]
