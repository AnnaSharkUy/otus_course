import pytest

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


def test_triangle_name():
    assert Triangle(2, 3, 4).name == "Triangle"


def test_triangle_invalid_arguments():
    with pytest.raises(ValueError):
        Triangle(2, 3, 5)


def test_triangle_area():
    triangle = Triangle(5, 3, 4)
    assert triangle.area == 6


def test_triangle_add_area():
    triangle = Triangle(2, 3, 4)
    square = Square(1)
    expected_result = triangle.area + square.area
    assert triangle.add_area(square) == expected_result
    rectangle = Rectangle(1, 2)
    expected_result = triangle.area + rectangle.area
    assert triangle.add_area(rectangle) == expected_result
    circle = Circle(1)
    expected_result = triangle.area + circle.area
    assert triangle.add_area(circle) == expected_result


def test_triangle_add_area_argument_notafigure():
    with pytest.raises(ValueError):
        Triangle(2, 3, 4).add_area("not a figure")


def test_triangle_add_area_argument_none():
    with pytest.raises(ValueError):
        Triangle(2, 3, 4).add_area(None)
