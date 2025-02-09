# membuat kalkulator sederhana dengan python


operator = input("masukan operator (+ - * /): ")
num1 = float(input("masukan angka pertama: "))
num2 = float(input("masukan angka kedua: "))

if operator == "+":
  hasil = num1 + num2
  print(round(hasil, 2))
elif operator == "-":
  hasil = num1 - num2
  print(round(hasil, 2))
elif operator == "*":
  hasil = num1 * num2
  print(round(hasil, 2))
elif operator == "/":
  hasil = num1 / num2
  print(round(hasil, 2))
else:
  print(f"{operator} bukan merupakan operator")