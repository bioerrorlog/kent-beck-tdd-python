from abc import ABC, abstractmethod


class Money(ABC):
    def __init__(self, amount):
        self.amount = amount
        self._currency = None

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @staticmethod
    def dollar(amount):
        return Dollar(amount, 'USD')

    @staticmethod
    def franc(amount):
        return Franc(amount, 'CHF')

    def currency(self):
        return self._currency

    def equals(self, object):
        return (
            self.amount == object.amount and
            isinstance(object, self.__class__)
        )

    @abstractmethod
    def times(self):
        pass


class Dollar(Money):
    def __init__(self, amount, currency):
        super().__init__(amount)
        self._currency = currency

    def times(self, multiplier):
        return Money.dollar(self.amount * multiplier)


class Franc(Money):
    def __init__(self, amount, currency):
        super().__init__(amount)
        self._currency = currency

    def times(self, multiplier):
        return Money.franc(self.amount * multiplier)
