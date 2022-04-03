import RPi.GPIO as GPIO
import time
import threading
import keyboard
import car_init
import car_move
import move_test
import Ultrasonic



threads = []
t1 = threading.Thread(target=Ultrasonic.start_Ultrasonic())
threads.append(t1)
t2 = threading.Thread(target=move_test.move_test2())
threads.append(t2)


if __name__ == '__main__':


    for t in threads:
        print(t)
        t.start()

