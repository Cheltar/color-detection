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

try:
    while True:
        print("Pilih:")
        print("1. Putar servo 1 ke kiri")
        print("2. Putar servo 1 ke kanan")
        print("3. Putar servo 2 ke kiri")
        print("4. Putar servo 2 ke kanan")
        print("5. Keluar")
        
        choice = input("Masukkan nomor tindakan yang Anda inginkan (1/2/3/4/5: ")

        if choice == '1':
            pwm1.ChangeDutyCycle(3.5)  # Putar servo 1 ke kiri
            time.sleep(1)
            pwm1.ChangeDutyCycle(7.5)  # Kembali ke tengah untuk servo 1
        elif choice == '2':
            pwm1.ChangeDutyCycle(12.5)  # Putar servo 1 ke kanan
            time.sleep(1)
            pwm1.ChangeDutyCycle(7.5)  # Kembali ke tengah untuk servo 1
        elif choice == '3':
            pwm2.ChangeDutyCycle(3.5)  # Putar servo 2 ke kiri
            time.sleep(1)
            pwm2.ChangeDutyCycle(7.5)  # Kembali ke tengah untuk servo 2
        elif choice == '4':
            pwm2.ChangeDutyCycle(12.5)  # Putar servo 2 ke kanan
            time.sleep(1)
            pwm2.ChangeDutyCycle(7.5)  # Kembali ke tengah untuk servo 2
        elif choice == '5':
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan 1, 2, 3, 4, dan 5")

except KeyboardInterrupt:
    pass


pwm1.stop()
pwm2.stop()
GPIO.cleanup()
