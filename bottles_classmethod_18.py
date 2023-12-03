class Hybridmethod:
    def __init__(self, fclass, finstance=None, doc=None):
        self.fclass = fclass
        self.finstance = finstance
        self.__doc__ = doc or fclass.__doc__

    def classmethod(self, fclass):
        return type(self)(fclass, self.finstance, None)

    def instancemethod(self, finstance):
        return type(self)(self.fclass, finstance, self.__doc__)

    def __get__(self, instance, cls):
        if instance is None or self.finstance is None:

            # either bound to the class, or no instance method available
            return self.fclass.__get__(cls, None)
        return self.finstance.__get__(instance, cls)


class BottleVerse:
    def __init__(self, number):
        self.number = number
        self._bottle_number = BottleNumber.from_number(self.number)

    @Hybridmethod
    def lyrics(cls, number):
        return cls(number).lyrics()

    @lyrics.instancemethod
    def lyrics(self):
        return (
            f'{str(self._bottle_number).capitalize()} of beer on the wall, '
            f'{self._bottle_number} of beer.\n'
            f'{self._bottle_number.action()}, '
            f'{self._bottle_number.successor()} of beer on the wall.\n'
        )


class CountdownSong:
    def __init__(self, verse_template=BottleVerse, max=99, min=0):
        self.verse_template = verse_template
        self.min = min
        self.max = max

    def song(self):
        return self.verses(self.max, self.min)

    def verses(self, upper, lower):
        return '\n'.join(self.verse(n) for n in range(upper, lower - 1, -1))

    def verse(self, number):
        return self.verse_template.lyrics(number)


class BottleNumber:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'{self.quantity()} {self.container()}'

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
    def from_number(cls, number):
        # 'Factory' still has to know the names of the derived classes.
        #  The logic here also has to make many routing decisions based on the number.
        match number:
            case 0:
                cls = BottleNumber0
            case 1:
                cls = BottleNumber1
            case 6:
                cls = BottleNumber6
            case 12:
                cls = BottleNumber12

        return cls(number)


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
