import random


def genMotorData():
    temperature = random.randint(0, 100)
    state = random.choice([b"STOPPED", b"MOVING", b"BROKEN"])
    return {
        "temperature": str(temperature).encode(),
        "state": state
    }


def genGeneralData():
    speed = random.random() * 100
    lat = random.randrange(-90, 90, 0.001)
    long = random.randrange(-180, 180, 0.001)
    return {
        "speed": str(speed).encode(),
        "lat": str(lat).encode(),
        "long": str(long).encode()
    }
