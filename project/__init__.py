import os
import time
from bill_calculation import Calculation
import bill_calculation

seconds = float(0)
minutes = int(0)
hours = int(0)
home = Calculation()


def timer(bool):
    global seconds
    global minutes
    if seconds > 59:
        seconds = 0
        minutes = minutes + 1

    seconds = seconds + 1
    print("Time : ", minutes, ":", seconds, "\n")


def meter():
    if seconds == 30:
        home.units = home.wattage_consumption(home.total_wattage, seconds)
        home.bill = bill_calculation.bill_calc(home.units)
        print("total wattage : ", home.total_wattage, "\n")
        print("consumption : ", home.getUnits(), "KWH", "\n")
        print("BILL = ", home.getBill(), " EGP . \n")


def main():
    home.show_running_devices()
    while home.run:
        timer(True)
        meter()
        time.sleep(1)
        os.system("clear")


if __name__ == '__main__':
    main()
