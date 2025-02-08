#soal: Minta pengguna memasukkan usia. Jika usia ≥ 17, tampilkan "Anda boleh memilih!". Jika tidak, tampilkan "Anda belum boleh memilih."

usia = int(input("Masukan usia: "))

if usia >= 17:
  print(f"Anda boleh memilih!")
else:
  print(f"anda belum boleh memilih")