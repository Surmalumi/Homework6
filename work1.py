# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).

import time

class TrafficLight:
    __traffic_light_color = "traffic_light"

    def running(self):
        while True:
            print("Red light")
            time.sleep(7)
            print("Yellow light")
            time.sleep(2)
            print("Green light")
            time.sleep(5)

x = TrafficLight()
x.running()