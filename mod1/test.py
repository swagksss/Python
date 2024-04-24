import unittest
from quadrilateral import Quadrilateral
from rectangle import Rectangle
from square import Square
from parallelogram import Parallelogram
from rhombus import Rhombus
from trapezoid import Trapezoid
from rectangular_trapezoid import RectangularTrapezoid
from equilateral_trapezoid import EquilateralTrapezoid

class TestQuadrilateralMethods(unittest.TestCase):
    def test_sort_by_area(self):
        rect1 = Rectangle(3, 4, name="Rectangle 1")
        rect2 = Rectangle(5, 6, name="Rectangle 2")
        square = Square(5, name="Square")
        parallelogram = Parallelogram(4, 5, 6, name="Parallelogram")
        rhombus = Rhombus(5, 6, name="Rhombus")
        trapezoid = Trapezoid(3, 4, 5, 6, 7, name="Trapezoid")
        rectangular_trapezoid = RectangularTrapezoid(3, 4, 5, 6, name="Rectangular Trapezoid")
        equilateral_trapezoid = EquilateralTrapezoid(5, 6, 7, name="Equilateral Trapezoid")

        shapes = [rect1, rect2, square, parallelogram, rhombus, trapezoid, rectangular_trapezoid, equilateral_trapezoid]
        sorted_shapes = sorted(shapes, key=lambda x: x.get_area())

        areas = [(shape.get_area(), shape.name) for shape in sorted_shapes]
        print("Sorted by area:")
        for area, name in areas:
            print(f"{name}: {area}")

    def test_sort_by_perimeter(self):
        rect1 = Rectangle(3, 4, name="Rectangle 1")
        rect2 = Rectangle(5, 6, name="Rectangle 2")
        square = Square(5, name="Square")
        parallelogram = Parallelogram(4, 5, 6, name="Parallelogram")
        rhombus = Rhombus(5, 6, name="Rhombus")
        trapezoid = Trapezoid(3, 4, 5, 6, 7, name="Trapezoid")
        rectangular_trapezoid = RectangularTrapezoid(3, 4, 5, 6, name="Rectangular Trapezoid")
        equilateral_trapezoid = EquilateralTrapezoid(5, 6, 7, name="Equilateral Trapezoid")

        shapes = [rect1, rect2, square, parallelogram, rhombus, trapezoid, rectangular_trapezoid, equilateral_trapezoid]
        sorted_shapes = sorted(shapes, key=lambda x: x.get_perimeter())

        perimeters = [(shape.get_perimeter(), shape.name) for shape in sorted_shapes]
        print("Sorted by perimeter:")
        for perimeter, name in perimeters:
            print(f"{name}: {perimeter}")


if __name__ == '__main__':
    unittest.main()


