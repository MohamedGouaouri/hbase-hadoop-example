import happybase
from generator import *
from cars import *


connection = happybase.Connection('hostname')
table = connection.table('cars')


for _ in range(1000):
    car = random.choice(cars)
    motor_data = genMotorData()
    general_data = genGeneralData()
    table.put(car.encode(), {
        b'motor:temperature': motor_data["temperature"],
        b'motor:state': motor_data['state'],
        b'general:speed': general_data['speed'],
        b'general:lat': general_data['lat'],
        b'general:long': general_data['long']
    })
