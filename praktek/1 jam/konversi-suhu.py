# soal : Minta pengguna memasukkan suhu dalam Celsius, lalu konversi ke Fahrenheit (rumus: °F = (°C × 9/5) + 32).

celcius = int(input("Suhu celcius: "))

fahrenheit = celcius * 9/5 + 32

print(f"{celcius}C = {fahrenheit}F")