import cv2
from ambil_data import color_histogram_feature_extraction
from ambil_data import knn_classifier
import os
import os.path
import time
import RPi.GPIO as GPIO
servo1_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo1_pin, GPIO.OUT)
pwm1 = GPIO.PWM(servo1_pin, 50)
pwm1.start(7.5)
servo2_pin = 26
GPIO.setup(servo2_pin, GPIO.OUT)
pwm2 = GPIO.PWM(servo2_pin, 50)  
pwm2.start(7.5)  # Sudut tengah 
cap = cv2.VideoCapture(0)


(ret, frame) = cap.read()
prediction = ''
PATH = './training.data'
if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
    print ('training data is ready, classifier is loading...')
else:
    print ('training data is being created...')
    open('training.data', 'w')
    color_histogram_feature_extraction.training()
    print ('training data is ready, classifier is loading...')

def camera11():
    global prediction
    global ret
    (ret, frame) = cap.read()
    cv2.putText(frame,'Warna:' + prediction,(15,45),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,50)
    cv2.imshow("test", frame)
    color_histogram_feature_extraction.color_histogram_of_test_image(frame)
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
while True:
    camera11()
    key = cv2.waitKey(1)
    if key == 27:
        break
pwm1.stop()
pwm2.stop()
GPIO.cleanup()
cap.release()
cv2.destroyAllWindows()