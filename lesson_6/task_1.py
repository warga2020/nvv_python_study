"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

import time
import itertools as itt


class TrafficLight:

    def __init__(self, colors_conf):
        self.__color = None
        self.__colors_conf = colors_conf

    def running(self):
        i = 0
        for it in itt.cycle(self.__colors_conf):
            color = it['color']
            delay = it['delay']
            print(color)
            if i > 10:
                break
            else:
                i += 1
            time.sleep(delay)


traffic_light_config = [{'color': 'красный', 'delay': 1},
                        {'color': 'желтый', 'delay': 1},
                        {'color': 'зеленый', 'delay': 1}]

trafficLightTest = TrafficLight(traffic_light_config)
trafficLightTest.running()
