class Bottles:
    def song(self):
        return self.verses(99, 0)

    def verses(self, upper, lower):
        return '\n'.join(self.verse(n) for n in range(upper, lower - 1, -1))

    def verse(self, number):
        bottle_number = BottleNumber.from_number(number)

        return (
            f'{str(bottle_number).capitalize()} of beer on the wall, '
            f'{bottle_number} of beer.\n'
            f'{bottle_number.action}, '
            f'{bottle_number.successor} of beer on the wall.\n'
        )

class BottleNumber:
    def __init__(self, number, action=None, container='bottles', pronoun='one', quantity=None):
        self.number = number
        self.pronoun = pronoun
        self.action = action or f'Take {self.pronoun} down and pass it around'
        self.container = container
        self.quantity = quantity or str(self.number)

    # This can't be in __init__, because it causes a recursion error.
    # Since @property runs after init, this will resolve correctly.
    @property
    def successor(self):
        return BottleNumber.from_number(self.number - 1)

    @classmethod
    def from_number(cls, number):
        # With this strategy, the class reconfigures itself by overriding
        # specific attributes, and returning a custom instance.
        # But the factory has to hold all this logic around customization.
        match number:
            case -1:
                return cls(99)
            case 0:
                return cls(number, action='Go to the store and buy some more', quantity='no more')
            case 1:
                return cls(number, container='bottle', pronoun='it')
            case 6:
                return cls(number, container='six-pack', quantity='1')
            case 12:
                return cls(number, container='case', quantity='1')
            case _:
                return cls(number)

    def __str__(self):
        return f'{self.quantity} {self.container}'
