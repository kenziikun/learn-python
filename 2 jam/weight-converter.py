# weight converter program

unit = input("masukan unit yang anda convert, kilogram atau pounds (K atau L): ")
weight = float(input("masukan berat badan anda: "))

if unit == "K":
  weight = weight * 2.205
  unit = "Lbs"
  print(f"berat badan anda: {round(weight, 2)} {unit}")
elif unit== "L":
  weight = weight / 2.205
  unit = "Kg"
  print(f"berat badan anda: {round(weight, 2)} {unit}")
else:
  print(f"{unit} tidak valid")