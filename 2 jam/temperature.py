# membuat program temperature

unit = input("masukan unit suhu yang ingin anda convert (C / F): ")
suhu = float(input("masukan angka yang ingin anda convert: "))
c = "Celcius"
f = "Fahrenheit"

if unit == "C":
  suhu = suhu * 9/5 + 32
  print(f"suhu setelah di convert {round(suhu, 1)} derajat {f}")
elif unit == "F":
  suhu = (suhu - 32) * 5/9
  print(f"suhu setelah di convert {round(suhu, 1)} derajat {c}")
else:
  print(f"maaf {unit} bukan unit suhu")