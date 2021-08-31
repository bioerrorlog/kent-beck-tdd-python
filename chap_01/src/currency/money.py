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

    @abstractmethod
    def currency(self):
        pass


class Dollar(Money):
    def __init__(self, amount):
        super().__init__(amount)
        self._currency = 'USD'

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

    def currency(self):
        return self._currency


class Franc(Money):
    def __init__(self, amount):
        super().__init__(amount)
        self._currency = 'CHF'

    def times(self, multiplier):
        return Franc(self.amount * multiplier)

    def currency(self):
        return self._currency
