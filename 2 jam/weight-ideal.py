# membuat program bb ideal dengan memasukan tinggi badan
# menggunakan rumus brocca : Berat badan ideal = (tinggi badan – 100) – [(tinggi badan – 100) x 10%] 


tinggi_badan = float(input("masukan tinggi badan anda: "))

operasi1 = tinggi_badan - 100
operasi2 = (tinggi_badan - 100) * 0.10
bb_ideal = operasi1-operasi2

print(f"{bb_ideal} adalah bb ideal anda")