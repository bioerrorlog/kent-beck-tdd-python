from src.money.dollar import Dollar


def test_multiplication():
    five = Dollar(5)
    assert five.times(2) == Dollar(10)
    assert five.times(3) == Dollar(15)

def test_equality():
    assert Dollar(5).equals(Dollar(5))
    assert not Dollar(5).equals(Dollar(6))
