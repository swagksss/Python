from abc import ABC, abstractmethod
import math

class Quadrilateral(ABC):
    def __init__(self, *args):
        self.figure_type = "Quadrilateral"
        self.unique_id = None
        self.vertices = None
        self.side_lengths = None
        self.perimeter_value = None
        self.area_value = None
        self.diagonals_lengths = None
        self.angle_measures = None


    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_diagonals_lengths(self):
        pass

    @abstractmethod
    def calculate_angle_measures(self):
        pass

    def check_properties(self):

        pass

    def get_vertex_coordinates(self):
        return self.vertices

    def get_side_lengths(self):
        return self.side_lengths

    def get_perimeter(self):
        return self.perimeter_value

    def get_area(self):
        return self.area_value

    def get_diagonals_lengths(self):
        return self.diagonals_lengths

    def get_angle_measures(self):
        return self.angle_measures

    def get_figure_type(self):
        return self.figure_type

    def get_subtypes(self):
        return [self.figure_type]

    def get_supertypes(self):
        return ["Quadrilateral"]

    def check_membership(self, subtype):
        return subtype in self.get_subtypes()

    def compare_area(self, other_figure):
        return self.area_value - other_figure.get_area()

    def compare_perimeter(self, other_figure):
        return self.perimeter_value - other_figure.get_perimeter()

    def compare_area_perimeter(self, other_figure):
        if self.area_value == other_figure.get_area():
            return self.perimeter_value - other_figure.get_perimeter()
        return self.area_value - other_figure.get_area()

    def check_intersection(self, other_figure):

        pass