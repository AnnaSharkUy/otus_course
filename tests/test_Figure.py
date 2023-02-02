import pytest
from src.Figure import Figure
from src.Square import Square


def test_figure_area():
    with pytest.raises(RuntimeError):
        Figure("invalid").area


def test_figure_add_area():
    with pytest.raises(RuntimeError):
        Figure("invalid").add_area(Square(1))


def test_circle_add_area_argument_not_figure():
    with pytest.raises(ValueError):
        Figure("invalid").add_area("not a figure")


def test_circle_add_area_argument_none():
    with pytest.raises(ValueError):
        Figure("invalid").add_area(None)
