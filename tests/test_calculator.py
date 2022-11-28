import pytest
from app.Calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_add(self):
        assert self.calc.add(self, 4, 7) == 11

    def test_subtract(self):
        assert self.calc.sub(self, 10, 5) == 5

    def test_multiply(self):
        assert self.calc.mul(self, 3, 7) == 21

    def test_divide(self):
        assert self.calc.div(self, 10, 2) == 5


