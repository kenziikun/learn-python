#arithmatics & math

# friends = 10

# friends = friends + 1
# friends += 1
# friends = friends - 1
# friends -= 1
# friends = friends * 1
# friends *= 1
# friends = friends / 2
# friends /= 2
# friends = friends ** 2
# friends **= 2
# remainder = friends % 4

# x = 3.14
# y = 4
# z = 5

# # result = round(x)
# # result = abs(y)
# # result = pow(2, 3)
# # result = max(x, y, z)
# # result = min(x, y, z)


# print(result)

# import math

# # print(math.pi)
# # print(math.e)
# x = 10.8

# # result = math.sqrt(x)
# # result = math.ceil(x)
# result = math.floor(x)

# print(result)

# exercises
# menghitung jari jari lingkaran | rumus = C = 2 pi * r
import math
'''
radius = float(input("masukan radius dari lingkaran: "))

jari_jari = 2 * math.pi * radius

print(f"jari jari lingkarannya adalah: {round(jari_jari, 2)}")
'''

# menghitung area lingkaran | A = pi * r^2
'''
radius = float(input("masukan luas area lingkaran: "))

area = math.pi * radius

print(f"luas area nya adalah {round(area, 2)}cm^2")
'''

# menghitung sisi miring segitiga | c = akar dari a^2 + b^2

a = float(input("masukan sisi A: "))
b = float(input("masukan sisi B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"hasil dari sisi C adalah: {round(c, 2)}")