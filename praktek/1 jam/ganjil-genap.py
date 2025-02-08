#soal : Minta pengguna memasukkan sebuah angka, lalu tampilkan apakah angka tersebut ganjil atau genap.

angka = int(input("Masukan angka: "))

if angka % 2 == 0:
  print(f"{angka} adalah bilangan genap")
else:
  print(f"{angka} adalah bilangan ganjil")

