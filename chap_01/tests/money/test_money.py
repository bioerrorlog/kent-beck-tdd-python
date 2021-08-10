from src.money.dollar import Dollar

class MoneyTest:
    def test_multiplication():
        five = Dollar(5)
        five.times(2)
        assert five.amount == 10
