"""First program using MQTT

Creating a client
Connecting the client to the broket BROKER
Subscribing the client to the topic TOPIC
Publishing MSG on TOPIC
"""

import time
import paho.mqtt.client as mqtt

BROKER = 'iot.eclipse.org'
CLIENT_NAME = 'mqqt_test_client'

MSG = 'Hello World !'
TOPIC = 'hello/world'


def info(message: str):
    print(f'** [INFO]\t{message}')


def on_log(client, userdata, level, buff):
    print(f'** [LOG]\t{buff}')


def on_message(client, userdata, message):
    print(
        '---'
        '\nData received:'
        f'\n\tTOPIC: {message.topic}'
        f'\n\tMESSAGE: {message.payload.decode()}'
        '\n---'
    )


if __name__ == '__main__':
    client = mqtt.Client(CLIENT_NAME)
    # client.on_log = on_log
    client.on_message = on_message

    info(f'Connecting to broker "{BROKER}"')
    client.connect(BROKER)
    client.loop_start()

    info(f'subscribing client to "{TOPIC}"')
    client.subscribe(TOPIC)

    info(f'publishing "{MSG}" to "{TOPIC}"')
    client.publish(TOPIC, MSG)

    info(f'waiting for a message')
    time.sleep(.5)

    client.loop_stop()
