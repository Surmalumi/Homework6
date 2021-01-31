# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).

class Car:

    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Car {self.name} go.'

    def stop(self):
        return f'Car {self.name} stop.'

    def turn(self, direction):
        return f'Car {self.name} turned {direction}.'

    def show_speed(self):
        return f'Your car speed is {self.speed}.'

   # def color(self):
       # return f'Car {self.color}.'

    def police(self):
        if self.is_police:
            return 'Police car'
        else:
            return 'City car'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 60:
            return f'Your speed is too high. Your car speed is {self.speed}.'
        else:
            return f'Your car speed is normal. Your car speed is {self.speed}.'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Your speed is too high. Your car speed is {self.speed}.'
        else:
            return f'Your car speed is normal. Your car speed is {self.speed}.'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


town = TownCar(100, 'Green', 'Wolksvagen', False)
sport = SportCar(140, 'Red', 'Ferrari', False)
work = WorkCar(70, 'Orange', 'Kamaz', False)
police = PoliceCar(110, 'Black',  'GMC', True)
print('1:\n' + town.go(), town.show_speed(), town.turn('left'), town.turn('right'), town.stop(), town.color, town.police())
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('left'), sport.turn('left'), sport.stop(), sport.color, sport.police())
print('3:\n' + work.go(), work.show_speed(), work.turn('right'), work.turn('right'), work.stop(), work.color, work.police())
print('4:\n' + police.go(), police.show_speed(), police.turn('right'), police.turn('left'), police.stop(), police.color, police.police())
