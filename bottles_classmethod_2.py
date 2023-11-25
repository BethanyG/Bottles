"""This avoids having child constructors.

    It trades that for more verbosity with methods
    and with decorating.  However, this also prevents
    attribute mutation, due to the lack of property setters,
    and retains the same interface for attribute access.
"""

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
    _registry = { }

    def __init__(self, number):
        self.number = number

    @property
    def pronoun(self):
        return 'one'

    @property
    def container(self):
        return 'bottles'

    @property
    def action(self):
        return f'Take {self.pronoun} down and pass it around'

    @property
    def quantity(self):
        return str(self.number)

    @property
    def successor(self):
        return BottleNumber.from_number(self.number - 1)

    @classmethod
    def __init_subclass__(cls, **kwargs):
        # not really necessary here, but ensures proper history
        # in cases of multiple inheritance.
        super().__init_subclass__(**kwargs)

        # Automatically adds any subclass to the _registry dict.
        BottleNumber._registry[cls.__name__] = cls

    @classmethod
    def from_number(cls, number):

        # Looks in the _registry dict for a class to handle the number.
        # If a matching class is not found, uses the parent.
        return BottleNumber._registry.get(f'BottleNumber{number}', BottleNumber)(number)

    def __str__(self):
        return f'{self.quantity} {self.container}'


class BottleNumber0(BottleNumber):

    @property
    def action(self):
        return 'Go to the store and buy some more'

    @property
    def quantity(self):
        return 'no more'

    @property
    def successor(self):
        return BottleNumber.from_number(99)


class BottleNumber1(BottleNumber):

    @property
    def pronoun(self):
        return 'it'

    @property
    def container(self):
        return 'bottle'

    @property
    def successor(self):
        return BottleNumber.from_number(self.number - 1)


class BottleNumber6(BottleNumber):

    @property
    def quantity(self):
        return '1'

    @property
    def container(self):
        return 'six-pack'

    @property
    def successor(self):
        return BottleNumber.from_number(self.number - 1)


class BottleNumber12(BottleNumber):

    @property
    def quantity(self):
        return '1'

    @property
    def container(self):
        return 'case'

    @property
    def successor(self):
        return BottleNumber.from_number(self.number - 1)