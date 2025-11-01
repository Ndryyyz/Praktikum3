from random import random

# Input nilai n dari user saat runtime
n = int(input("Masukkan nilai n: "))

# List untuk menyimpan bilangan acak
bilangan_acak = []

# Gunakan while loop untuk menghasilkan bilangan acak < 0.5
i = 0
while i < n:
    angka = random()
    # Hanya tambahkan jika angka < 0.5
    if angka < 0.5:
        bilangan_acak.append(angka)
        i += 1

# Gunakan for loop untuk menampilkan hasilnya
print(f"\n{n} bilangan acak yang lebih kecil dari 0.5:")
for idx, angka in enumerate(bilangan_acak, 1):
    print(f"{idx}. {angka:.6f}")
