from src.money.dollar import Dollar, Franc, Money


class TestMoney:
    def test_multiplication(self):
        five = Money.dollar(5)
        assert five.times(2) == Dollar(10)
        assert five.times(3) == Dollar(15)

    def test_equality(self):
        assert Dollar(5).equals(Dollar(5))
        assert not Dollar(5).equals(Dollar(6))
        assert Franc(5).equals(Franc(5))
        assert not Franc(5).equals(Franc(6))
        assert not Franc(5).equals(Dollar(5))

    def test_franc_multiplication(self):
        five = Franc(5)
        assert five.times(2) == Franc(10)
        assert five.times(3) == Franc(15)
