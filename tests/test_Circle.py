import pytest

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


def test_circle_invalid_arguments():
    with pytest.raises(ValueError):
        Circle(0)


def test_circle_add_area():
    circle = Circle(1)
    square = Square(1)
    expected_result = circle.area + square.area
    assert circle.add_area(square) == expected_result
    rectangle = Rectangle(1, 2)
    expected_result = circle.area + rectangle.area
    assert circle.add_area(rectangle) == expected_result
    triangle = Triangle(2, 3, 4)
    expected_result = triangle.area + circle.area
    assert circle.add_area(triangle) == expected_result


def test_circle_add_area_argument_notafigure():
    with pytest.raises(ValueError):
        Circle(1).add_area("not a figure")
