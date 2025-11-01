# Modal awal
modal = 100_000_000

# Persentase laba per bulan
laba_bulanan = [0, 0, 1, 1, 5, 5, 5, 3]  # dalam persen

print("=" * 50)
print("PERHITUNGAN KEUNTUNGAN USAHA")
print("=" * 50)
print(f"Modal Awal: Rp {modal:,}")
print("\nRincian Keuntungan per Bulan:")
print("-" * 50)

total_keuntungan = 0

for bulan in range(1, 9):
    persentase = laba_bulanan[bulan - 1]
    keuntungan = modal * persentase / 100
    total_keuntungan += keuntungan
    
    print(f"Bulan {bulan}: {persentase}% = Rp {keuntungan:,.0f}")

print("-" * 50)
print(f"\nTOTAL KEUNTUNGAN (8 bulan): Rp {total_keuntungan:,.0f}")
print(f"Modal + Keuntungan: Rp {modal + total_keuntungan:,.0f}")
print("=" * 50)
