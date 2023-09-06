import RPi.GPIO as GPIO
import time
from ambil_data import knn_classifier
GPIO.setwarnings(False)
servo_pin = 17
servo_pin2 = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin,GPIO.OUT)
GPIO.setup(servo_pin2,GPIO.OUT)
# 50 Hz or 20 ms PWM period
pwm = GPIO.PWM(servo_pin,50) 
pwm2 = GPIO.PWM(servo_pin2,50) 
pwm.start(5)
pwm2.start(5)
def setAngle(angle):
    duty = angle / 18 + 3
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(duty)
pwm.ChangeDutyCycle(5)

def setAngle2(angle):
    duty = angle / 18 + 3
    GPIO.output(servo_pin2, True)
    pwm2.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo_pin2, False)
    pwm2.ChangeDutyCycle(duty)
pwm2.ChangeDutyCycle(5)

while True:
	prediction = knn_classifier.main('training.data', 'test.data')
	if prediction == 'red':
		setAngle(-30)
		setAngle(50)
	elif prediction == 'blue':
		setAngle(150)
		setAngle(50)
		time.sleep(1)
		setAngle2(150)
		setAngle2(90)
	elif prediction == 'green':
		setAngle(150)
		setAngle(50)
		time.sleep(1)
		setAngle2(20)
		setAngle2(90)
# def on_subscribe(client, userdata, mid, granted_qos):
#     print("Subscribed: "+str(mid)+" "+str(granted_qos))

# def on_message(client, userdata, msg):   
#     if msg.payload == b'green':
#            SetAngle(10)
#     elif msg.payload == b'blue':
#           SetAngle(100)
# client = paho.Client()
# client.on_subscribe = on_subscribe
# client.on_message = on_message
# client.connect('broker.mqttdashboard.com', 1883)
# client.subscribe('masuk/warnadetection', qos=1)
# client.loop_forever()

pwm.stop() 
GPIO.cleanup()
print("Program stopped")
