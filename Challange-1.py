angka = input("masukan Nilai: ")
hasil =  usm(int(1) for i in angka)
print("Total",hasil)
while hasil >= 10:
    hasil = sum(int(i) for i in str(hasil))

print(hasil)
