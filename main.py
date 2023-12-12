from time import sleep

from home_data import House
from publisher import Publisher

p = Publisher()

while True:
    sleep(1)
    h = House()

    p.publish(h.to_dict())
