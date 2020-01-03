from random import randint
from Appliance import Appliance


def bill_calc(units):
    """
    this function takes the KWH usage on return it's price (EGP)
    based on it's sugment.
    :param units: double
    :return bill: double
    """
    bill = 0.0

    if units < 51:
        bill = units * 0.30
    elif 51 <= units <= 100:  # 49kwh
        bill = (50 * 0.30) + ((units - 50) * 0.40)
    elif 100 < units <= 200:
        # break point
        bill = units * 0.50
    elif 201 <= units <= 350:  # 150kwh
        bill = (200 * 0.50) + ((units - 200) * 0.82)
    elif 351 <= units <= 650:  # 301kwh
        bill = (200 * 0.50) + (150 * 0.82) + ((units - 350) * 1)
    elif 651 <= units <= 1000:  # 351kwh
        bill = (200 * 0.50) + (150 * 0.82) + 300 + ((units - 650) * 1.40)
    elif units > 1000:  # 1000kwh
        # break point
        bill = units * 1.45

    return bill


class Calculation(Appliance):
    kilo_watt = 1000

    def __init__(self, name=None, wattage=None):
        super().__init__(name, wattage)
        self.home = []
        # home is a list of appliance object
        self.turned_off_appliance = []
        self.total_wattage = 0
        self.units = 0.0
        self.bill = 0.0
        self.run = True

    def wattage_consumption(self, wattage, time_in_sec):
        """
        take time in mints, wattage in watt and convert time  to hours, watt to kilowatt
        to return unit.
        unit => total Wattage * Time / 10000
        :param time_in_min:
        :param wattage: running Total wattage
        :return: unit => KWH
        """

        time_in_hours = (time_in_sec / 60)
        unit = (wattage * time_in_hours) / self.kilo_watt
        return unit

    def init_random_home(self, minimum_wattage=None, maximum_wattage=None, appliance_mun=None):
        """
        initializing a home within random numbers of wattage
        and return total_wattage of home devices that's running together
        :param appliance_mun:
        :param minimum_wattage:
        :param maximum_wattage:
        :return: total_wattage : int,  of home devices that's running together
        """

        home_list = ["CoffeeMaker", "Microwave", "Toaster", "Dishwasher", "Washer"
                                                                          "Dryer", "Iron", "SpaceHeater", "HairDryer"]

        home_dic = {
            "CoffeeMaker": 1200,
            "Microwave": 1100,
            "Toaster": 1400,
            "Dishwasher": 2400,
            "Washer": 500,
            "Dryer": 4000,
            "Iron": 1800,
            "SpaceHeater": 5500,
            "HairDryer": 1875,
        }
        # making full random appliance
        if appliance_mun is not None:
            for n in range(5, appliance_mun):
                self.home.append(Appliance("unknown", randint(200, 4000)))
                print("appliance_mun is not none")

        elif minimum_wattage and maximum_wattage is not None and appliance_mun is None:
            for appliance_object in home_list:
                appliance_object = Appliance(appliance_object, randint(minimum_wattage, maximum_wattage))
                self.home.append(appliance_object)
                print("minimum_wattage and maximum_wattage is not None and appliance_mun is None")
        else:
            for device, wattage in home_dic.items():
                self.home.append(Appliance(device, wattage))
            # print("all = none")

        for obj in self.home:
            self.total_wattage += obj.wattage

        return self.total_wattage

    def calc_total_wattage(self):
        """
        get total of appliance wattage that's running
        :return: total wattage
        """
        for obj in self.home:
            self.total_wattage += obj.wattage
        return self.total_wattage

    def add_appliance(self, wattage, name="unknown"):
        obj = Appliance(name, wattage)
        self.home.append(obj)

    def turn_off(self, name):
        # TODO: ADD search algorithm and check if name is unknown
        for obj in self.home:
            if obj.get_name == name:
                self.turned_off_appliance.append(obj)
                self.home.remove(obj)

    def turn_on(self, name):
        for obj in self.turned_off_appliance:
            if obj.get_name == name:
                self.home.append(obj)
                self.turned_off_appliance.remove(obj)

    def increase_wattage(self, wattage):
        self.total_wattage += wattage

    def decrease_wattage(self, wattage):
        self.total_wattage -= wattage

    def set_total_wattage(self, total_wattage):
        self.total_wattage = total_wattage

    def setUnits(self, u):
        self.units = u

    def getUnits(self):
        return round(self.units, 2)

    def getBill(self):
        return round(self.bill, 3)

    def setTotalWatt(self, total):
        self.total_wattage = total

    def show_running_devices(self):
        strr= ""
        for device in self.home :
            strr += " {} : {} \n".format(device.name,device.wattage)

        return strr

    def show_of_devices(self):
        strr= ""
        for device in self.turned_off_appliance :
            strr += " {} : {} \n".format(device.name,device.wattage)

        return strr
