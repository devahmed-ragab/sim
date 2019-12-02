import bill_calculation
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