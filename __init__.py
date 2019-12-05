import os
import time
import bill_calculation
from bill_calculation import Calculation


def main():
    seconds = float(0)
    minutes = int(0)
    home = Calculation()
    total_watt = home.init_random_home()

    run = input("press r to start : ")

    if run != 'r':
        raise ValueError("expected r value  :")

    while run.lower() == "r":
        if seconds > 59:
            seconds = 0
            minutes = minutes + 1
        os.system('clear')
        seconds = seconds + 30
        units = home.wattage_consumption(total_watt, minutes)
        bill = bill_calculation.bill_calc(units)

        print("total wattage : ", total_watt, "\n")
        print("Time : ", minutes, ":", seconds, "\n")
        print("consumption : ", units , "KWH", "\n")
        print("BILL = ", round(bill, 3), " EGP . \n")
        time.sleep(10)


if __name__ == '__main__':
    main()

