nama = input('Masukan nama karyawan:')
golongan = int(input('Masukan golongan karyawan [1/2/3]:'))
pendidikan = input('Pendidikan [SMA/D1/D3/S1]:')
jam_kerja = int(input('Masukan jam kerja:'))

gaji_pokok = 300000

if golongan == 1:
    tunjangan_golongan = 0.05 * 300000
elif golongan == 2:
    tunjangan_golongan = 0.1 * 300000
elif golongan == 3:
    tunjangan_golongan = 0.15 * 300000
else:
    print('Maaf yang anda masukkan tidak valid')

if pendidikan.upper() == 'SMA':
    tunjangan_pendidikan = 0.025 * 300000
elif pendidikan.upper() == 'D1':
    tunjangan_pendidikan = 0.05 * 300000
elif pendidikan.upper() == 'D3':
    tunjangan_pendidikan = 0.2 * 300000
elif pendidikan.upper() == 'S1':
    tunjangan_pendidikan = 0.3 * 300000
else:
    print('Maaf yang anda masukkan tidak valid')

if jam_kerja >= 8:
    jam = jam_kerja - 8
    lembur = jam * 3500
else:
    print('Anda tidak mendapatkan uang lembur')

total_gaji = gaji_pokok + tunjangan_golongan + tunjangan_pendidikan + lembur

rincian = 'RINCIAN GAJI KARYAWAN'
print(rincian.center(40))
print('==' * 17)
print('Nama karyawan:' +str(nama))
print('Honor yang di terima:', int(gaji_pokok))
print('Tunjangan jabatan: Rp.', int(tunjangan_golongan))
print('Tunjangan pendidikan: Rp.', int(tunjangan_pendidikan))
print('Honor lembur: Rp.', int(lembur))
print('Total Pendapatan: Rp.', int(total_gaji))
print('==' * 17)



