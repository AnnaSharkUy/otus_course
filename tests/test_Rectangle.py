import pytest

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


def test_rectangle_name():
    rectangle = Rectangle(1, 2)
    assert rectangle.name == "Rectangle"


def test_rectangle_invalid_arguments():
    with pytest.raises(ValueError):
        Rectangle(0, 3)


def test_rectangle_area():
    rectangle = Rectangle(1, 2)
    assert rectangle.area == 2


def test_rectangle_add_area():
    rectangle = Rectangle(1, 2)
    square = Square(1)
    expected_result = rectangle.area + square.area
    assert rectangle.add_area(square) == expected_result
    triangle = Triangle(2, 3, 4)
    expected_result = triangle.area + rectangle.area
    assert rectangle.add_area(triangle) == expected_result
    circle = Circle(1)
    expected_result = rectangle.area + circle.area
    assert rectangle.add_area(circle) == expected_result


def test_rectangle_add_area_argument_notafigure():
    with pytest.raises(ValueError):
        Rectangle(1, 2).add_area("not a figure")


def test_rectangle_add_area_argument_none():
    with pytest.raises(ValueError):
        Rectangle(1, 2).add_area(None)
