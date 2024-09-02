length_yard = int(input("enter yard length: "))
width_yard = int(input("enter yard width: "))
length_house = int(input("enter house length: "))
width_house = int(input("enter house width: "))

luas_rumah = length_house * width_house
luas_taman = length_yard * width_yard

if luas_rumah > luas_taman:
    print("bro you don't have a yard")

else:
    luas_taman_berumput = luas_taman - luas_rumah
    total_waktu = luas_taman_berumput / 2

    print(f"total time to cut the grass {total_waktu} second")