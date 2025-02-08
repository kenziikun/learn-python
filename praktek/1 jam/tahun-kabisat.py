#soal: Minta pengguna memasukkan tahun, lalu tentukan apakah tahun tersebut kabisat.
# Kriteria:

# Tahun kabisat habis dibagi 4,

# Tapi tidak habis dibagi 100 kecuali jika habis dibagi 400.


tahun = int(input("masukan tahun: "))

if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
  print(f"{tahun} adalah tahun kabisat")
else:
  print(f"{tahun} bukan tahun kabisat")