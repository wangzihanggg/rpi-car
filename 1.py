import RPi.GPIO as GPIO
import time
import threading
from threading import Thread
import keyboard
import car_init
import car_move
import move_test
import Ultrasonic


threads = []
threads.append(threading.Thread(target=Ultrasonic.start_Ultrasonic()))
threads.append(threading.Thread(target=move_test.move_test1()))
print(threads)


if __name__ == '__main__':

    init = car_init.init()

    for t in threads:
        print(t)
        t.start()


