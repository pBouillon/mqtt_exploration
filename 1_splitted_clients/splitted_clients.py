"""Another sample splitting subscriber and publisher

run_device
    Create a 'fridge' and a 'tv' publishing events
    on the channel of their own rooms

run_home
    Create a device subscribed to all rooms

"""
import time

import paho.mqtt.client as mqtt

BROKER = 'iot.eclipse.org'


def on_message(client, userdata, message):
    print(f'{message.topic}: {message.payload.decode()}')


def run_device(uptime: int):
    client = mqtt.Client('Device')
    client.connect(BROKER)

    client.on_message = on_message
    client.subscribe('room/+')  # single level wilcard, see

    client.loop_start()
    time.sleep(uptime)
    client.loop_stop()


def run_house():
    fridge = mqtt.Client('Fridge')
    fridge.connect(BROKER)

    tv = mqtt.Client('TV')
    tv.connect(BROKER)

    fridge.publish('room/kitchen', 'Door opened')
    tv.publish('room/living-room', 'TV turned on')
    fridge.publish('room/kitchen', 'Door closed')
    fridge.publish('room/kitchen', 'Door opened')
    fridge.publish('room/kitchen', 'Door closed')
    tv.publish('room/living-room', 'TV turned off')


if __name__ == '__main__':
    run_device(uptime=30)  # run first
    # run_house()   # run in another interpreter
