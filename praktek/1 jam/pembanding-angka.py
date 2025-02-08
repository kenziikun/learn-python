#soal: Minta dua angka dari pengguna, lalu tampilkan angka yang lebih besar. Jika keduanya sama, tampilkan "Angka sama".

angka_pertama = int(input("Angka pertama: "))
angka_kedua = int(input("Angka kedua: "))

if angka_pertama > angka_kedua:
  print(f"{angka_pertama} lebih besar dari {angka_kedua}")
elif angka_pertama < angka_kedua:
  print(f"{angka_pertama} lebih kecil dari {angka_kedua}")
elif angka_pertama == angka_kedua:
  print(f"Angka sama")
