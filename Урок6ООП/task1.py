# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
# и завершать скрипт.
from time import sleep


class TrafficLight:
    colors = {'Красный': 7, 'Желтый': 2, 'Зеленый': 5}

    def __init__(self, color):
        self.__color = color

    def running(self):
        print(f'Светофор начинает работать\n ')
        while True:
            for color, color_time in self.colors.items():
                self.__color = color
                print(f'Сигнал светофора: {self.__color}')
                sleep(color_time)


if __name__ == '__main__':
    tl = TrafficLight('Красный')
    tl.running()
