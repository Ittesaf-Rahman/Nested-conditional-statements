units = int(input("please enter the number of units you consumed = "))
if units < 50:
    bill = units * 3.50
    surchearge = 25
elif units <= 100:
    bill = units * 4.50
    surchearge = 35
elif units <= 200:
    bill = units * 5.50
    surchearge = 55
elif units <= 300:
    bill = units * 6.50
    surchearge = 65
else:
    bill = units * 8
    surchearge = 120
total_bill = bill + surchearge
print("Your electricity bill is : ",total_bill,"BDT")