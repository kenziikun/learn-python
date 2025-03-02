# belajar tentang logical operator
# and = kondisi dimana kedua kondisinya harus true
# or = kondisi dimana salah satu kondisi harus tue
# not = kondisi kebalikan

# soal 1 : diskon membership
# Seorang pelanggan mendapat diskon 20% jika mereka adalah member dan total belanja ≥ 300.000.
# Buat program yang:

# Minta input status member (True/False).

# Minta input total belanja.

# Tampilkan "Diskon 20%!" jika memenuhi syarat, atau "Tidak ada diskon."

'''
member = input("apakah anda member ? (ya / tidak): ")
total_belanja = float(input("total belanja: "))

if member == "ya" and total_belanja >= 300.000:
  member = True
  print("anda mendapatkan diskon 20%")
elif member == "ya" and total_belanja <= 300.000:
  member = True
  print("maaf anda tidak mendapatkan diskon")
elif member == "tidak" and total_belanja >= 300.000:
  member = False
  print("maaf anda tidak mendapatkan diskon")
elif member == "tidak" and total_belanja <= 300.000:
  member = False
  print("maaf anda tidak mendapatkan diskon")
else:
  print("masukan input yang benar")
'''

# soal 2 : cek tahun abad
# Tahun abad adalah tahun yang habis dibagi 100 (misal: 1900, 2000).
# Buat program yang:

# Minta input tahun.

# Tampilkan "Tahun abad!" jika tahun habis dibagi 100 dan (habis dibagi 400 atau tidak habis dibagi 400). 
'''
tahun = int(input("masukan tahun: "))

if tahun % 100 == 0 and (tahun % 400 == 0):
  print (f"{tahun} adalah tahun abad dan tahun kabisat")
elif tahun % 100 == 0:
  print (f"{tahun} adalah tahun abad tetapi bukan tahun kabisat")
else:
  print ("Bukan tahun Abad")
'''

# soal 3 : Password kuat
# Password dianggap "kuat" jika:

# Panjang ≥ 8 karakter,

# Mengandung angka,

# Mengandung huruf besar.
# Buat program yang memeriksa kekuatan password.

password = input("Masukan password: ")
