"""Using wildcards to subscribe to specific topics

run_house
    Creating some devices (thermometer and hoven)
    Each of them publish on their specific channel

listen
    Creating a smoke detector
    Listening only to channels about temperature
    no matter the room
"""
import time

import paho.mqtt.client as mqtt

from _3_house_simulation.devices import Device

BROKER = 'iot.eclipse.org'


# noinspection PyUnusedLocal
def on_message(client, userdata, message):
    print(f'{message.topic}: {message.payload.decode()}')


def run_house():
    thermometer_b = Device(
        name='thermometer_b',
        broker=BROKER,
        topic='house/bathroom/temperature'
    )

    thermometer_k = Device(
        name='thermometer_k',
        broker=BROKER,
        topic='house/kitchen/temperature'
    )

    hoven_k = Device(
        name='hoven_k',
        broker=BROKER,
        topic='house/kitchen/hoven'
    )

    thermometer_b.publish('12°')
    hoven_k.publish('ON')
    thermometer_k.publish('15°')
    hoven_k.publish('OFF')


def listen(uptime: int):
    smoke_detector = mqtt.Client('smoke_detector')
    smoke_detector.connect(BROKER)

    smoke_detector.on_message = on_message
    smoke_detector.subscribe('house/+/temperature')

    smoke_detector.loop_start()
    time.sleep(uptime)
    smoke_detector.loop_stop()


if __name__ == '__main__':
    listen(uptime=60)
    # run_house()
