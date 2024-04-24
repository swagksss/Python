from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side_length,name="Square"):
        super().__init__(side_length, side_length)
        self.figure_type = "Square"
        self.check_properties()
        self.name = name

    def check_properties(self):
        if self.side_lengths[0] == self.side_lengths[1]:
            print("It's a square!")

    def get_subtypes(self):
        return [self.figure_type]
