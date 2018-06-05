"""Exploring payload possibilities
"""
import json
import time

import paho.mqtt.client as mqtt

BROKER = 'iot.eclipse.org'


# noinspection PyUnusedLocal
def on_message(client, userdata, message):
    print(f'\n\tMESSAGE: {message.payload.decode()}')


if __name__ == '__main__':
    client = mqtt.Client('client')
    # client.on_log = on_log
    client.on_message = on_message

    client.connect(BROKER)
    client.loop_start()

    client.subscribe('dummy/test')

    client.publish('dummy/test', json.dumps({
        'key #1': 'value',
        'key #2': 0,
    }))

    time.sleep(.5)

    client.loop_stop()
