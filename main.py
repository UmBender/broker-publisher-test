import paho.mqtt.client as mqtt
import time

for i in range(4):

    client = mqtt.Client()
    connection = client.connect("localhost", 1883, 60)
    if connection != 0:
        print("Cannot connect")

    f = open("info.txt", "r")
    f = f.read()
    f = f.split("\n")
    for i in f:
        client.publish("test/status", i, 0)
        time.sleep(1)
    client.disconnect()
