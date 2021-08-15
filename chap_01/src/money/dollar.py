

class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

    def equals(self, object):
        return self.amount == object.amount 

class Franc:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def times(self, multiplier):
        return Franc(self.amount * multiplier)

    def equals(self, object):
        return self.amount == object.amount 