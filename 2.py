from abc import ABC, abstractproperty


class Clother(ABC):
    def __init__(self, parameters):
        self.parameters = parameters

    @abstractproperty
    def calculator(self):
        return 'owo'


class Coat(Clother):
    @property
    def calculator(self):
        return (self.parameters / 6.5) + 0.5


class Suit(Clother):
    @property
    def calculator(self):
        return (self.parameters * 2) + 0.3


coat = Coat(40)
suit = Suit(173)
print(coat.calculator)
print(suit.calculator)
