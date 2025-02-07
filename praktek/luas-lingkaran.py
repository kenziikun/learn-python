# soal : Minta pengguna memasukkan jari-jari lingkaran, lalu hitung dan tampilkan luasnya (rumus: π × r², gunakan π = 3.14).

import math

r = float(input("Masukan jari jari: "))

luas_lingkaran = math.pi * r

print(f"luas lingkaran: {round(luas_lingkaran, 2)}")