from abc import ABC, abstractmethod


class Money(ABC):
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @staticmethod
    def dollar(amount):
        return Dollar(amount)

    @staticmethod
    def franc(amount):
        return Franc(amount)

    def equals(self, object):
        return (
            self.amount == object.amount and
            isinstance(object, self.__class__)
        )

    @abstractmethod
    def times(self):
        pass


class Dollar(Money):
    def __init__(self, amount):
        super().__init__(amount)

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)


class Franc(Money):
    def __init__(self, amount):
        super().__init__(amount)

    def times(self, multiplier):
        return Franc(self.amount * multiplier)
