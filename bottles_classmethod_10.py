from collections import defaultdict

class Bottles:
    def song(self):
        return self.verses(99, 0)

    def verses(self, upper, lower):
        return '\n'.join(self.verse(n) for n in range(upper, lower - 1, -1))

    def verse(self, number):
        bottle_number = BottleNumber.given(number)

        return (
            f'{str(bottle_number).capitalize()} of beer on the wall, ' \
            f'{bottle_number} of beer.\n'
            f'{bottle_number.action()}, '
            f'{bottle_number.successor()} of beer on the wall.\n'
        )


class BottleNumber:
    _registry = {}

    @classmethod
    def __init_subclass__(cls, **kwargs):
        # Not really necessary here, but ensures proper history
        # in cases of multiple inheritance.
        super().__init_subclass__(**kwargs)

        # Automatically adds any subclass to the _registry dict.
        # When this is called, cls refers to the derived class
        number = cls.handles()
        BottleNumber._registry[number] = cls

    @classmethod
    def given(cls, number):
        # cls = BottleNumber._registry.get(number, BottleNumber)
        # return cls(number)
        return BottleNumber._registry.get(number, cls)(number)

    @classmethod
    def handles(cls):
        return -1

    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'{self.quantity()} {self.container()}'

    def quantity(self):
        return str(self.number)

    def container(self):
        return 'bottles'

    def pronoun(self):
        return 'one'

    def action(self):
        return f'Take {self.pronoun()} down and pass it around'


    def successor(self):
        return BottleNumber.given(self.number - 1)


class BottleNumber0(BottleNumber):
    @classmethod
    def handles(cls):
        return 0

    def quantity(self):
        return 'no more'

    def action(self):
        return 'Go to the store and buy some more'

    def successor(self):
        return BottleNumber.given(99)


class BottleNumber1(BottleNumber):
    @classmethod
    def handles(cls):
        return 1

    def container(self):
        return 'bottle'

    def pronoun(self):
        return 'it'

    def action(self):
        return f'Take {self.pronoun()} down and pass it around'


class BottleNumber6(BottleNumber):
    @classmethod
    def handles(cls):
        return 6

    def quantity(self):
        return '1'

    def container(self):
        return 'six-pack'


class BottleNumber12(BottleNumber):
    @classmethod
    def handles(cls):
        return 12

    def container(self):
        return 'case'

    def quantity(self):
        return '1'
