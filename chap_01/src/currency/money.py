from abc import ABC, abstractmethod


class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self._currency = currency

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @staticmethod
    def dollar(amount):
        return Dollar(amount, 'USD')

    @staticmethod
    def franc(amount):
        return Franc(amount, 'CHF')

    @property
    def currency(self):
        return self._currency

    def equals(self, object):
        return (
            self.amount == object.amount and
            isinstance(object, self.__class__)
        )

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)


class Dollar(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)


class Franc(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)
