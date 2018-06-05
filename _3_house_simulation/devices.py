import paho.mqtt.client as mqtt


class Device:
    def __init__(self, name: str, broker: str, topic: str):
        self.broker = broker
        self.topic = topic

        self.device = mqtt.Client(name)
        self.__setup_client()
        self.device.connect(broker)

    def __setup_client(self):
        self.device.on_connect = self.on_connect
        self.device.on_disconnect = self.on_disconnect

    def publish(self, message: str):
        self.log(f'{message}\tsuccessfully published on\t{self.topic}')
        self.device.publish(self.topic, message)

    # noinspection PyUnusedLocal
    def on_connect(self, client, userdata, rc):
        if rc:
            exit(f'Unable to connect to {self.broker}')
        self.log(f'Successfully connected to {self.broker}')

    # noinspection PyUnusedLocal
    def on_disconnect(self, client, userdata, rc):
        if rc:
            exit(f'Disconnected with errors')
        self.log(f'Successfully disconnected to {self.broker}')

    @staticmethod
    def log(msg: str):
        print(f'** [LOG]\t{msg}')
