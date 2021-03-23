"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""


class Car:

    def __init__(self, speed, color, name, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f'The {self.name} starts moving')

    def stop(self):
        self.speed = 0
        print(f'The {self.name} stopped')

    def turn(self, direction):
        print(f'The {self.name} turned {direction}')

    def show_speed(self):
        print(f'{self.name} speed {self.speed}')


class TownCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Violation of the speed limit - slow down!')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Violation of the speed limit - slow down!')


class PoliceCar(Car):
    pass


if __name__ == '__main__':
    car = Car(100, 'white', 'simple car', False)
    car.go()
    car.turn('left')
    car.show_speed()
    car.stop()
    car.show_speed()

    car = TownCar(61, 'white', 'town car', False)
    car.go()
    car.turn('left')
    car.show_speed()
    car.stop()
    car.show_speed()

    car = TownCar(61, 'white', 'town car', False)
    car.go()
    car.turn('left')
    car.show_speed()
    car.stop()
    car.show_speed()

    car = WorkCar(41, 'white', 'work car', False)
    car.go()
    car.turn('left')
    car.show_speed()
    car.stop()
    car.show_speed()
