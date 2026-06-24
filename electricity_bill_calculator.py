def electricity_bill(units,rate=8):
    bill = units * rate
    return bill
units=int(input("Enter units: "))
print("electricity bill",electricity_bill(units))
