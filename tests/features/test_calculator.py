from src.features.calculator import add, substract

class TestCalculator:
    
    def test_addition(self):
        assert 4 == add(2,2)
    
    def test_subtraction(self):
        assert 2 == substract(4,2)