# Created By Mohammed at Sep, 2 2022
# Tip Calculator
print("Welcome to Tip Calculator\n")
bill = input("Enter total bill: ")

bill = float(bill)

peopleCount = input("Enter how many people to split the bill: ")
peopleCount = int(peopleCount)

tipPercent = input("Enter tip percentage: ")
tipPercent = int(tipPercent) / 100

totalBill = (bill + tipPercent * bill) / peopleCount
toPayPerPerson = "{:.2f}".format(round(totalBill, 2))

print(f"Each one should pay ${toPayPerPerson}")
