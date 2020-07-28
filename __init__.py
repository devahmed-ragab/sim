import os
import time
from bill_calculation import Calculation
from bill_calculation import bill_calc
from api import update_ser_local, update_SER_consumption

seconds = float(0)
minutes = int(0)
hours = int(0)
home = Calculation()
total_sec = int(0)


def timer(bool):
    global seconds
    global minutes
    global total_sec
    if seconds > 59:
        seconds = 0
        minutes = minutes + 1
    seconds = seconds + 1
    total_sec = total_sec + 1
    print("Time : ", minutes, ":", seconds, "\n")


def meter():
    if seconds % 2 == 0:
        home.units = home.wattage_consumption(home.total_wattage, total_sec)
        home.bill = bill_calc(home.units)
        update_SER_consumption(home.getUnits(), home.getBill(), home.getUnits())


def main():
    home.show_running_devices()
    while home.run:
        timer(True)
        meter()
        time.sleep(1)
        os.system("clear")


if __name__ == '__main__':
    main()
