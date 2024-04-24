from parallelogram import Parallelogram

class Rhombus(Parallelogram):
    def __init__(self, side, height,name="Rhombus"):
        super().__init__(side, height, side)
        self.figure_type = "Rhombus"
        self.check_properties()
        self.name = name

    def check_properties(self):
        if self.side_lengths[0] == self.side_lengths[1]:
            print("It's a rhombus!")

    def get_subtypes(self):
        return [self.figure_type]
