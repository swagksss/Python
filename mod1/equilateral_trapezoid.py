from trapezoid import Trapezoid

class EquilateralTrapezoid(Trapezoid):
    def __init__(self, base, height, side,name="EquilateralTrapezoid"):
        super().__init__(base, base, height, side, side)
        self.figure_type = "Equilateral Trapezoid"
        self.check_properties()
        self.name = name

    def check_properties(self):
        if self.side_lengths[0] == self.side_lengths[1]:
            print("It's an equilateral trapezoid!")

    def get_subtypes(self):
        return [self.figure_type]

