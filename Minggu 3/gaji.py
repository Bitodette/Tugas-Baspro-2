gajiPokok = {
    "Tetap": 1000000,
    "Honor": 750000
}

bonus = {
    "Tetap": {
        "A": 200000,
        "B": 400000,
        "C": 550000
    },
    "Honor": {
        "A": 150000,
        "B": 275000,
        "C": 480000
    }
}

nama = input("Masukkan Nama: ").title()
nik = int(input("Masukkan NIK: "))
status = input("Masukkan Status (Tetap/Honor): ").capitalize()
golongan = input("Masukkan Golongan (A/B/C): ").upper()

while True:
    if status == "Tetap" or status == "Honor":
        break
    else:
        print("Status harus 'Tetap' atau 'Honor'")
        status = input("Masukkan Status yang Benar (Tetap/Honor): ").capitalize()

while True:
    if golongan == "A" or golongan == "B" or golongan == "C":
        break
    else:
        print("Golongan harus 'A', 'B', atau 'C'")
        golongan = input("Masukkan Golongan yang Benar (A/B/C): ").upper()

gaji = gajiPokok.get(status)
bonusGolongan = bonus.get(status).get(golongan)
gajiTotal = gaji + bonusGolongan

print(f"\nData Pegawai")
print(f"Nama       : {nama}")
print(f"NIK        : {nik}")
print(f"Status     : {status}")
print(f"Golongan   : {golongan}")
print(f"Gaji       : Rp {gaji}")
print(f"Bonus      : Rp {bonusGolongan}")
print(f"Gaji Total : Rp {gajiTotal}")
