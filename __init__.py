import os
import time
import bill_calculation
from bill_calculation import Calculation
import threading


seconds = float(0)
minutes = int(0)


def timer(bool):
    global seconds
    global minutes
    if seconds > 59:
        seconds = 0
        minutes = minutes + 1
    seconds = seconds + 1
    print("Time : ", minutes, ":", seconds, "\n")


def meter():

    home = Calculation()
    home.total_watt = home.init_random_home()
    units = home.wattage_consumption(home.total_watt, minutes)
    bill = bill_calculation.bill_calc(units)

    print("total wattage : ", home.total_watt, "\n")
    print("consumption : ", round(units, 4), "KWH", "\n")
    print("BILL = ", round(bill, 3), " EGP . \n")


def main():
    """
    t1 = threading.Thread(target=timer, args=(True,))
    t2 = threading.Thread(target=meter)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    """

    while True:
        timer(True)
        meter()
        time.sleep(1)
        os.system("clear")


if __name__ == '__main__':
    main()
