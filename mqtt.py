import paho.mqtt.client as paho
import time
from ambil_data import knn_classifier
def on_publish(client, userdata, mid):
    print("mid: "+str(mid))
 
client = paho.Client()
client.on_publish = on_publish
client.connect('broker.mqttdashboard.com', 1883)
client.loop_start()

while True:
    prediction = knn_classifier.main('training.data', 'test.data')
    (mid) = client.publish('apaiyanih/haichelthekodir'), str(prediction, qos=1)
    time.sleep(30)