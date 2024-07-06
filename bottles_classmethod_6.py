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
            f'{bottle_number.action()}, '
            f'{bottle_number.successor()} of beer on the wall.\n'
        )

class BottleNumber:
    _registry = {}

    def __init__(self, number):
        self.number = number

    def pronoun(self):
        return 'one'

    def container(self):
        return 'bottles'

    def action(self):
        return f'Take {self.pronoun()} down and pass it around'

    def quantity(self):
        return str(self.number)

    def successor(self):
        return BottleNumber.from_number(self.number - 1)


    @classmethod
    def __init_subclass__(cls, **kwargs):
        # Not really necessary here, but ensures proper history
        # in cases of multiple inheritance.
        super().__init_subclass__(**kwargs)

        # Automatically adds any subclass to the _registry dict.
        # Here I've trimmed the name to extract only the number for the registry.
        number = int(cls.__name__[12:])
        BottleNumber._registry[number] = cls

    @classmethod
    def from_number(cls, number):

        # Looks in the _registry dict for a class to handle the number.
        # If a matching class is not found, it uses the parent.
        return BottleNumber._registry.get(number, BottleNumber)(number)

    def __str__(self):
        return f'{self.quantity()} {self.container()}'


class BottleNumber0(BottleNumber):

    def action(self):
        return 'Go to the store and buy some more'

    def successor(self):
        return BottleNumber.from_number(99)

    def quantity(self):
        return 'no more'


class BottleNumber1(BottleNumber):

    def container(self):
        return 'bottle'

    def pronoun(self):
        return 'it'


class BottleNumber6(BottleNumber):

    def container(self):
        return 'six-pack'

    def quantity(self):
        return '1'


class BottleNumber12(BottleNumber):

    def container(self):
        return 'case'

    def quantity(self):
        return '1'

