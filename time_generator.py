import random
from datetime import datetime


def generate_temp_and_humidity():
    now = datetime.now()
    hour = now.hour

    if 5 <= hour < 8:
        temp = round(random.uniform(15, 20))
        humidity = round(random.uniform(50, 60))
    elif 8 <= hour < 10:
        temp = round(random.uniform(20, 25))
        humidity = round(random.uniform(40, 50))
    elif 10 <= hour < 12:
        temp = round(random.uniform(18, 22))
        humidity = round(random.uniform(45, 55))
    elif 12 <= hour < 14:
        temp = round(random.uniform(22, 27))
        humidity = round(random.uniform(35, 45))
    elif 14 <= hour < 16:
        temp = round(random.uniform(25, 30))
        humidity = round(random.uniform(30, 40))
    elif 16 <= hour < 18:
        temp = round(random.uniform(20, 25))
        humidity = round(random.uniform(40, 50))
    elif 18 <= hour < 20:
        temp = round(random.uniform(15, 20))
        humidity = round(random.uniform(50, 60))
    elif 20 <= hour < 22:
        temp = round(random.uniform(10, 15))
        humidity = round(random.uniform(60, 70))
    elif 22 <= hour < 24:
        temp = round(random.uniform(8, 12))
        humidity = round(random.uniform(70, 80))
    else:
        temp = round(random.uniform(10, 15))
        humidity = round(random.uniform(60, 70))

    return temp, humidity


def generate_temp_and_humidity_outdoor():
    now = datetime.now()
    hour = now.hour

    if 5 <= hour < 8:
        temp = round(random.uniform(2, 4))
        humidity = round(random.uniform(40, 50))
    elif 8 <= hour < 10:
        temp = round(random.uniform(4, 6))
        humidity = round(random.uniform(30, 40))
    elif 10 <= hour < 12:
        temp = round(random.uniform(6, 8))
        humidity = round(random.uniform(35, 45))
    elif 12 <= hour < 14:
        temp = round(random.uniform(8, 10))
        humidity = round(random.uniform(25, 35))
    elif 14 <= hour < 16:
        temp = round(random.uniform(9, 11))
        humidity = round(random.uniform(20, 30))
    elif 16 <= hour < 18:
        temp = round(random.uniform(8, 10))
        humidity = round(random.uniform(30, 40))
    elif 18 <= hour < 20:
        temp = round(random.uniform(6, 8))
        humidity = round(random.uniform(40, 50))
    elif 20 <= hour < 22:
        temp = round(random.uniform(4, 5))
        humidity = round(random.uniform(50, 60))
    elif 22 <= hour < 24:
        temp = round(random.uniform(2, 4))
        humidity = round(random.uniform(60, 70))
    else:
        temp = round(random.uniform(0, 2))
        humidity = round(random.uniform(50, 60))

    return temp, humidity

def generate_tv(start: int, end: int):
    now = datetime.now()
    hour = now.hour
    # Adjust TV status based on the time of day
    if start <= hour < end:  # Evening (6 PM to 10 PM)
        return True

    if random.randint(0, 10) < 2:
        return None

    if random.randint(0, 10) < 6:
        return False

    return False


def generate_is_broken():
    now = datetime.now()
    hour = now.hour

    if 14 <= hour < 16:
        return True
    return False
