jumlah_siswa = int(input('enter jumlah siswa: '))

total_section = jumlah_siswa // 30
student_left = jumlah_siswa % 30

print(f"the amount of student {jumlah_siswa} so there will be {total_section} section and {student_left} student left")