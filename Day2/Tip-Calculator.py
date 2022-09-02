# Created By Mohammed at Sep, 2 2022
print("Welcom to Tip Calculator\n")
bill = input("Enter total bill: ")

bill = float(bill)

peoplCount = input("Enter how many people to split the bill: ")
peoplCount = int(peoplCount)

tipPercent = input("Enter tip percentage: ")
tipPercent = int(tipPercent) / 100

totalBill = (bill + tipPercent * bill) / peoplCount
toPayPerPerson = "{:.2f}".format( round(totalBill,2) )

print(f"Each one should pay ${toPayPerPerson}")