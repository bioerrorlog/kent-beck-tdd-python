class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @staticmethod
    def dollar(amount):
        return Dollar(amount)

    def equals(self, object):
        return (
            self.amount == object.amount and
            isinstance(object, self.__class__)
        )

class Dollar(Money):
    def __init__(self, amount):
        super().__init__(amount)

    def times(self, multiplier):
        return Money(self.amount * multiplier)

class Franc(Money):
    def __init__(self, amount):
        super().__init__(amount)

    def times(self, multiplier):
        return Money(self.amount * multiplier)