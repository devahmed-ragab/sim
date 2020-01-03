import bill_calculation
from bill_calculation import bill_calc
"""
testing bailing function accuracy
"""
test = bill_calculation()

for i in range(0,100):
    print("bill for " + str(i) + " = " + str(round(bill_calc(i), 2)))

print("100 to 200")
print("--------------------------------------")

for i in range(100,200):
    print("bill for " + str(i) + " = " + str(round(bill_calc(i), 2)))

print("200 to 1000")
print("--------------------------------------")

for i in range(200,1000):
    print("bill for " + str(i) + " = " + str(round(bill_calc(i), 2)))

print("1000 to 1100")
print("--------------------------------------")

for i in range(1000,1100):
    print("bill for " + str(i) + " = " + str(round(bill_calc(i), 2)))


"""

"""

""""
def init_rondom_home(self, minimum_wattage, maximum_wattage, appliance_mun):
    
    initializing a home within random numbers of wattage
    and return total_wattage of home devices that's running together
    :param minimum_wattage:
    :param maximum_wattage:
    :return: total_wattage : int,  of home devices that's running together
    

    home_list = ["CoffeeMaker", "Microwave", "Toaster", "Dishwasher", "Washer"
                                                                      "Dryer", "Iron", "SpaceHeater", "HairDryer"]

    for appliance_object in home_list:
        appliance_object = Appliance(appliance_object, randint(minimum_wattage, maximum_wattage))
        self.home.append(appliance_object)

    for obj in self.home:
        self.total_wattage += obj.wattage

    return self.total_wattage"""