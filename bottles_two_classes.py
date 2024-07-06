class Bottles:
    def song(self):
        return self.verses(99, 0)

    def verses(self, upper, lower):
        return '\n'.join(self.verse(n) for n in range(upper, lower - 1, -1))

    def verse(self, number):
        bottle_number = BottleNumber(number)
        next_bottle_number = BottleNumber(bottle_number.successor)

        return (
            f'{str(bottle_number).capitalize()} of beer on the wall, '
            f'{bottle_number} of beer.\n'
            f'{bottle_number.action}, '
            f'{next_bottle_number} of beer on the wall.\n'
        )

class BottleNumber:
    def __init__(self, number, container='bottles', pronoun='one', quantity=None):
        self.number = number
        self.pronoun = pronoun
        self.action = f'Take {self.pronoun} down and pass it around'
        self.container = container
        self.quantity = str(number)
        self.successor = number - 1

        match self.number:
            case 0:
                self.quantity = 'no more'
                self.action = 'Go to the store and buy some more'
                self.successor = 99
            case 1:
                self.container = 'bottle'
                self.pronoun = 'it'
                self.action = f'Take {self.pronoun} down and pass it around'

    def __str__(self):
        return f'{self.quantity} {self.container}'
