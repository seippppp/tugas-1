skor_yang_dinginkan = input("enter desired grade: " )
skor_minimum = float(input("enter minimum average required: "))
skor_sekarang = float(input("enter your average grade: "))
persentase_skor_akhir= int(input("enter how much percentage the course grade:"))

if skor_minimum < skor_sekarang:
    print ("your current grade is already above the desired grade, have fun in the exam!")

if skor_minimum > skor_sekarang:
    persentase_skor_awal = 100 - persentase_skor_akhir

    skor_needed = float("{:.2f}".format ((skor_minimum - persentase_skor_awal * skor_sekarang / 100) * 100 / persentase_skor_akhir))

    if skor_needed > 100:
        print ("the grade you want is to high")
    if skor_needed < 100:
        print(f"you need the score of {skor_needed} on the final to get a {skor_yang_dinginkan}")