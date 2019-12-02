import os
import time
import bill_calculation
from bill_calculation import Calculation


def main():
    seconds = float(0)
    minutes = int(0)

    test = Calculation()
    total_watt = test.inili_home(800, 5000)

    run = input("press r to start : ")

    if run != 'r':
        raise ValueError("expected r value  :")

    while run.lower() == "r":
        if seconds > 59:
            seconds = 0
            minutes = minutes + 1
        os.system('clear')
        seconds = seconds + 30
        print("Time : ", minutes, ":", seconds)
        print()
        units = test.wattage_consumption(total_watt, minutes)
        print("consumption : ", units , "KWH")
        print("")
        bill = bill_calculation.bill_calc(units)
        print("BILL = ", round(bill, 3), " EGP .")
        print("")
        time.sleep(10)


if __name__ == '__main__':
    main()

