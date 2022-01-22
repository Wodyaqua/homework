class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернул на {direction}')

    def show_speed(self):
        print(f'Скорость {self.name}: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super(TownCar, self).show_speed()
        
        if self.speed > 60:
            print(f'{self.name} Превышение разрешенной скорости!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super(WorkCar, self).show_speed()

        if self.speed > 40:
            print(f'{self.name} Превышение скорости!')


class PoliceCar(Car):
    pass


town_car = TownCar(65, 'Gray', 'Opel', False)
sport_car = SportCar(77, 'Yellow', 'Lada 8x8 Super Car edition', False)
work_car = WorkCar(38, 'Blue', 'KAMAZ', False)
police_car = PoliceCar(63, 'Black', 'Police Lada', True)

police_car.go()
sport_car.stop()
work_car.turn('left')
town_car.show_speed()
work_car.show_speed()
