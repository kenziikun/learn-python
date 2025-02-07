# input() = sebuah function untuk memasukan data,dan akan di return dalam bentuk string
'''
name = input("whats is your name: ")
age = int(input("how old are you: "))

# age = int(age)
age += 1


print(f"hello my name is {name}") #f string digunakan ketika kamu ingin memasukan varible
print("selamat ulang tahun!")
print(f"im {age} years old")
'''

#exercises 1
'''
length = float(input("enter the length: "))
width = float(input("enter the width: "))

area = length * width

print(f"hasilnya adalah {area}cm")
'''

#exercises 2
item = input("apa barang yang ingin kamu beli: ")
price = float(input("berapa harganya: "))
quantity = int(input("berapa jumlah barang yang kamu beli: "))

total = price * quantity

print(f"kamu membeli {quantity} item {item}")
print(f"harga yang harus kamu bayar ${total}")

