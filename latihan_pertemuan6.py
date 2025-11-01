L_nim = []
L_uts = []
L_uas = []
L_total = []

jumlah = int(input('Masukan Jumlah Siswa:'))

for i in range(jumlah):
    print("Data Mahasiswwa ke-" +str(i+1))
    L_nim.append(input("Masukan Nim Anda:"))
    L_uts.append(int(input("Masukan Nilai UTS:")))
    L_uas.append(int(input("Masukan Nilai UAS:")))

for i in range(jumlah):
    L_total.append((L_uts[i]) + (L_uas[i]) / 2)


print("\n")
print("==" * 30)
print("Nim\t\t""Nilai UTS\t""Nilai UAS\t""Total")
print("==" * 30)
for i in range(ulang):
 print ("%s \t %i \t\t %i \t\t\t %i" % (list_nim[i],list_uts[i],list_uas[i],list_total[i]))
print("==" * 30)