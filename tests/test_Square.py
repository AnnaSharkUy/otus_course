import pytest

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


def test_square_name():
    assert Square(1).name == "Square"


def test_square_invalid_arguments():
    with pytest.raises(ValueError):
        Square(0)


def test_square_area():
    assert Square(4).area == 16


def test_square_add_area():
    square = Square(1)
    triangle = Triangle(2, 3, 4)
    expected_result = square.area + triangle.area
    assert square.add_area(triangle) == expected_result
    rectangle = Rectangle(1, 2)
    expected_result = square.area + rectangle.area
    assert square.add_area(rectangle) == expected_result
    circle = Circle(1)
    expected_result = square.area + circle.area
    assert square.add_area(circle) == expected_result


def test_square_add_area_argument_notafigure():
    with pytest.raises(ValueError):
        Square(1).add_area("not a figure")


def test_square_add_area_argument_none():
    with pytest.raises(ValueError):
        Square(1).add_area(None)
