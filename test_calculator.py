import calculator


class TestCalculator:

    def test_add(self):
        assert 4 == calculator.add(2, 2)

    def test_subtract(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiply(self):
        assert 4 == calculator.multiply(2, 2)

    def test_divide(self):
        assert 2 == calculator.divide(4, 2)
