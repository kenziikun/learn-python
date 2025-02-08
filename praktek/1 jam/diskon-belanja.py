#soal: Jika total belanja pengguna ≥ 500.000, berikan diskon 10%. Jika tidak, tidak ada diskon. Hitung total yang harus dibayar.

total_belanja = float(input("Total belanja: "))

if total_belanja >= 500000:
  diskon = total_belanja * 0.10
  total_bayar = total_belanja - diskon
  print(f"total bayar: {total_bayar} (diskon 10%)")
else:
  print(f"total bayar: {total_belanja} (tidak dapat diskon)")