

class Dollar:

    def __init__(self, amount: int) -> None:
        self.amount = amount

    def times(self, multiplier: int) -> None:
        return Dollar(self.amount * multiplier)

    def equals(self, object) -> bool:
        return self.amount == object.amount 