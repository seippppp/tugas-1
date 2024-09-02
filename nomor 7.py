efisiensi = int(input("enter efficiency: "))
gallons = int(input ("enter amount of gallons: "))

barrel = gallons / 42

barrels_BTU = barrel * 5800000

BTU = float("{:.2f}".format (barrels_BTU * efisiensi / 100))

print(f"total BTU: {BTU}")