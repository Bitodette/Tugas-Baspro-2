import math

r = float(input("Masukkan Jari-Jari Tabung: "))
t = float(input("Masukkan Tinggi Tabung: "))

v = round(math.pi * pow(r,2) * t,2)

print(f"Volume Tabung adalah: {v:,}")