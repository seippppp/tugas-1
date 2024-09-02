import math
populasi = int(input("populasi yang ada: "))

jumlah_toilet = math.ceil(populasi/3)

magnitude = jumlah_toilet * 28
cost = jumlah_toilet * 150

print(f"jumlah air yang di perlukan adalah {magnitude} liter dan harga yang di butuhkan adalah {cost}$")