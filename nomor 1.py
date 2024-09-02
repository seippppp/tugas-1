print("TAXI FARE CALCULATOR")
awal = float(input("enter beginning odometer reading: "))
akhir = float(input("enter ending odometer reading: "))

total_dis = float("{:.2f}".format (akhir - awal))

harga = total_dis * 1.50

print(f"you traveled a distance of {total_dis} miles at 1.5$ per mile, your fare is {harga}$")