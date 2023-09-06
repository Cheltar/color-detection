import time
import requests

TOKEN = ""  # Put your TOKEN here
DEVICE_LABEL = "raspi"  # Put your device label here 
VARIABLE_LABEL_1 = "Biru"  # Put your first variable label here
VARIABLE_LABEL_2 = "Hijau"
VARIABLE_LABEL_3 = "Merah"
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
# Atur mode GPIO ke BCM
GPIO.setmode(GPIO.BCM)

# Tentukan pin Trig dan Echo untuk sensor pertama
trig_pin_1 = 16
echo_pin_1 = 24

# Tentukan pin Trig dan Echo untuk sensor kedua
trig_pin_2 = 20
echo_pin_2 = 23

trig_pin_3 = 6
echo_pin_3 = 13
# Atur pin sebagai output (Trig) dan input (Echo) untuk kedua sensor
GPIO.setup(trig_pin_1, GPIO.OUT)
GPIO.setup(echo_pin_1, GPIO.IN)
GPIO.setup(trig_pin_2, GPIO.OUT)
GPIO.setup(echo_pin_2, GPIO.IN)
GPIO.setup(trig_pin_3, GPIO.OUT)
GPIO.setup(echo_pin_3, GPIO.IN)

def get_distance(trig_pin, echo_pin):
    GPIO.output(trig_pin, True)
    time.sleep(0.00001)
    GPIO.output(trig_pin, False)

    pulse_start = time.time()
    pulse_end = time.time()

    while GPIO.input(echo_pin) == 0:
        pulse_start = time.time()

    while GPIO.input(echo_pin) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    return distance


def build_payload(variable_1, variable_2, variable_3):
        distance_1 = get_distance(trig_pin_1, echo_pin_1)
        distance_2 = get_distance(trig_pin_2, echo_pin_2)
        distance_3 = get_distance(trig_pin_3,echo_pin_3)
        print("Jarak Sensor 1:", distance_1, "cm")
        print("Jarak Sensor 2:", distance_2, "cm")
        print("Jarak Sensor 3:", distance_3, "cm")
        payload = {variable_1: distance_1,
                   variable_2: distance_2,
                   variable_3: distance_3}
        print(payload)
        return payload

def post_request(payload):
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(1)

    # Processes results
    print(req.status_code, req.json())
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True

def main():
    payload = build_payload(
        VARIABLE_LABEL_1, VARIABLE_LABEL_2, VARIABLE_LABEL_3)

    print("[INFO] Attemping to send data")
    post_request(payload)
    print("[INFO] finished")


if __name__ == '__main__':
    while (True):
        main()
        time.sleep(1)
