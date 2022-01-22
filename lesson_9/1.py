import time
import itertools


class TrafficLight:
    def __init__(self):
        self.__color = (('Красный', 7), ('Желтый', 2), ('Зеленый', 5))

    def running(self):
        for color, sec in itertools.cycle(self.__color):
            print(color)
            time.sleep(sec)


traffic_light = TrafficLight()
traffic_light.running()
