#soal: Buat program yang mengonversi nilai (0-100) ke dalam kategori:
# A (≥ 80)

# B (≥ 70)

# C (≥ 60)

# D (≥ 50)

# E (< 50)

nilai = int(input("Masukan nilai: "))

if nilai >= 80:
  print(f"Grade anda: A")
elif nilai >= 70:
  print(f"Grade anda: B")
elif nilai >= 60:
  print(f"Grade anda: C")
elif nilai >= 50:
  print(f"Grade anda: D")
else:
  print(f"Grade anda: E")