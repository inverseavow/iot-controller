import paho.mqtt.client as mqtt

class MQTTClient:
    def __init__(self, broker, port, keepalive=60):
        self.client = mqtt.Client()
        self.broker = broker
        self.port = port
        self.keepalive = keepalive
        
        # MQTT Callbacks
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
    
    def on_connect(self, client, userdata, flags, rc):
        print(f"Connected with result code {rc}")
        # Subscribe to device topics
        self.subscribe("davinci/+/command")
        self.subscribe("wallwasher/+/status")

    def on_message(self, client, userdata, message):
        print(f"Message received: {message.topic} {str(message.payload)}")
        # Handle messages here based on the topic
        if message.topic.startswith("davinci"):
            self.handle_davinci_message(message)
        elif message.topic.startswith("wallwasher"):
            self.handle_wallwasher_message(message)

    def subscribe(self, topic):
        self.client.subscribe(topic)

    def publish(self, topic, payload):
        self.client.publish(topic, payload)

    def handle_davinci_message(self, message):
        # Process Davinci message
        print("Processing Davinci message...")
    
    def handle_wallwasher_message(self, message):
        # Process wallwasher message
        print("Processing Wallwasher message...")
    
    def connect(self):
        self.client.connect(self.broker, self.port, self.keepalive)

    def loop(self):
        self.client.loop_forever()

# Usage example
if __name__ == "__main__":
    mqtt_client = MQTTClient(broker="broker_address", port=1883)
    mqtt_client.connect()
    mqtt_client.loop()