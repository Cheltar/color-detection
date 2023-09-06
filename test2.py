from ambil_data import knn_classifier
import RPi.GPIO as GPIO
import time
servo1_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo1_pin, GPIO.OUT)
pwm1 = GPIO.PWM(servo1_pin, 50)
pwm1.start(7.5)


servo2_pin = 26
GPIO.setup(servo2_pin, GPIO.OUT)
pwm2 = GPIO.PWM(servo2_pin, 50)  
pwm2.start(7.5)  # Sudut tengah 

prediction = ''
while True:
    prediction = knn_classifier.main('training.data', 'test.data')
    if prediction == 'green':
            pwm1.ChangeDutyCycle(3.5)  # Putar servo 1 ke kiri
            time.sleep(1)
            pwm1.ChangeDutyCycle(7.5)  # Kembali ke tengah untuk servo 1
            time.sleep(1)
    elif prediction == 'blue':
            pwm1.ChangeDutyCycle(12.5)  # Putar servo 1 ke kanan
            time.sleep(1)
            pwm1.ChangeDutyCycle(7.5)  # Kembali ke tengah untuk servo 1q
            time.sleep(2)
            pwm2.ChangeDutyCycle(3.5)
            time.sleep(1)
            pwm2.ChangeDutyCycle(7.5)  
            time.sleep(1)   
    elif prediction == 'red':
            print("red")
            pwm1.ChangeDutyCycle(12.5)  # Putar servo 1 ke kanan
            time.sleep(1)
            pwm1.ChangeDutyCycle(7.5)  # Kembali ke tengah untuk servo 1q
            time.sleep(2)
            pwm2.ChangeDutyCycle(12.5)
            time.sleep(1)
            pwm2.ChangeDutyCycle(7.5)
            time.sleep(1)
pwm1.stop()
pwm2.stop()
GPIO.cleanup()
