class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income['wage'] + income['bonus']


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income


name = 'Alexander'
surname = 'Ivanov'
position = 'Engineer'
income = {'wage': 35000, 'bonus': 5000}

w = Worker(name, surname, position, income)
p = Position(name, surname, position, income)
print(p.get_full_name())
print(p.get_total_income())
