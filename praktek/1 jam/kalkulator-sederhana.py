#soal: Minta dua angka dan operasi (+, -, *, /). Lakukan operasi yang sesuai dan tampilkan hasilnya. Jika operasi tidak valid, tampilkan pesan error.

angka_pertama = float(input("masukan angka: "))
angka_kedua = float(input("masukan angka: "))
operasi = input("masukan operasi yang ingin digunakan (+/-/*//): ")


if operasi == "+":
  hasil = angka_pertama + angka_kedua
elif operasi == "-":
  hasil = angka_pertama - angka_kedua
elif operasi == "*":
  hasil = angka_pertama * angka_kedua
elif operasi == "/":
  hasil = angka_pertama / angka_kedua
  if angka_kedua != 0:
    angka_pertama / angka_kedua
  else:
    hasil = "error: tidak bisa di bagi dengan nol"
else:
  hasil = "error: operasi tidak valid"
print(f"hasil: {round(hasil, 2)}")
