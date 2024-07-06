class Bottles:
    def song(self):
        return self.verses(99, 0)

    def verses(self, upper, lower):
        return '\n'.join(self.verse(n) for n in range(upper, lower - 1, -1))

    def verse(self, number):
        bottle_number = BottleNumber.given(number)

        return (
            f'{str(bottle_number).capitalize()} of beer on the wall, '
            f'{bottle_number} of beer.\n'
            f'{bottle_number.action()}, '
            f'{bottle_number.successor()} of beer on the wall.\n'
        )


# Pulled registration into its own class.
# The register method is written as a class decorator.
class Registrar:
    _registry = {}

    @classmethod
    def registry(cls):
        return cls._registry

    @staticmethod
    def register(cls):
        number = cls.handles(cls)
        Registrar.registry()[number] = cls
        return cls


# Class decorator.  Sends the class into the register method of Registrar
@Registrar.register
class BottleNumber:

    # This clssmethod stays the same, so the caller interface stays the same.
    @classmethod
    def given(cls, number):
        # cls = BottleNumber._registry.get(number, BottleNumber)
        # return cls(number)
        return Registrar.registry().get(number, cls)(number)

    # This is a kluge, and I think it's preferable to do the dict.get(number, BottleNumber)
    # trick to avoid having to remember a "magic" number for a default.
    @staticmethod
    def handles(cls):
        return -1

    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return f'{self.quantity()} {self.container()}'

    def quantity(self):
        return str(self.number)

    def container(self):
        return 'bottles'

    def action(self):
        return f'Take {self.pronoun()} down and pass it around'

    def pronoun(self):
        return 'one'

    def successor(self):
        return BottleNumber.given(self.number - 1)


@Registrar.register
class BottleNumber0(BottleNumber):
    @staticmethod
    def handles(cls):
        return 0

    def quantity(self):
        return 'no more'

    def action(self):
        return 'Go to the store and buy some more'

    def successor(self):
        return BottleNumber.given(99)


@Registrar.register
class BottleNumber1(BottleNumber):
    @staticmethod
    def handles(cls):
        return 1

    def container(self):
        return 'bottle'

    def pronoun(self):
        return 'it'


@Registrar.register
class BottleNumber6(BottleNumber):
    @staticmethod
    def handles(cls):
        return 6

    def quantity(self):
        return '1'

    def container(self):
        return 'six-pack'


@Registrar.register
class BottleNumber12(BottleNumber):
    @staticmethod
    def handles(cls):
        return 12

    def container(self):
        return 'case'

    def quantity(self):
        return '1'
