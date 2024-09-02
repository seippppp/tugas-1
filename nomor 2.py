tinggi = float(input("Masukkan tinggi bendungan: "))
aliran_air = float(input("Masukkan aliran air: "))

massa_air = aliran_air * 1000

daya = float("{:.2f}".format (massa_air * 9.80 * tinggi))

efisiensi = daya * 0.90

daya_mw = efisiensi / 10**6

print(f"Daya yang dihasilkan oleh bendungan: {daya_mw}MW")