#  Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}

class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + " ('_') " + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

x = Position('Cat', 'Zilla', 'Catsaur', 1000000, 250000)
print(x.get_full_name(), x.get_total_income())
