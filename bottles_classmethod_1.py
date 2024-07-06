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
        # 'Factory' still has to know the names of the derived classes.
        #  The logic here also has to make many routing decisions based on the number.
        match number:
            case 0:
                return BottleNumber0(number)
            case 1:
                return BottleNumber1(number)
            case 6:
                return BottleNumber6(number)
            case 12:
                return BottleNumber12(number)
            case _:
                return cls(number)

    def __str__(self):
        return f'{self.quantity} {self.container}'


class BottleNumber0(BottleNumber):

    def __init__(self, number):
        # Calls the parent 'constructor' back and overrides the attributes that are different.
        super().__init__(number, action='Go to the store and buy some more', quantity='no more')

    @property
    def successor(self):
        return BottleNumber.from_number(99)


class BottleNumber1(BottleNumber):

    def __init__(self, number):
        super().__init__(number, container='bottle', pronoun='it')

    @property
    def successor(self):
        return BottleNumber.from_number(self.number - 1)


class BottleNumber6(BottleNumber):

    def __init__(self, number):
        super().__init__(number, container='six-pack', quantity='1')

    @property
    def successor(self):
        return BottleNumber.from_number(self.number - 1)


class BottleNumber12(BottleNumber):

    def __init__(self, number):
        super().__init__(number, container='case', quantity='1')

    @property
    def successor(self):
        return BottleNumber.from_number(self.number - 1)