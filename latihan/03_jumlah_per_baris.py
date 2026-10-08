# Latihan 3 - Jumlah per Baris
# Untuk i = 1..4 dan j = 1..3, hitung nilai i * j
# dan tampilkan jumlah setiap baris.

# Loop luar   : mengatur baris i (1 sampai 4)
# Loop dalam  : mengatur kolom j (1 sampai 3)
# Akumulator  : total_baris, direset ke 0 di awal setiap iterasi loop luar
#               (sebelum loop dalam) agar jumlah dihitung per baris
# Prediksi    : 4 x 3 = 12 kali perhitungan i * j

for i in range(1, 5):
    total_baris = 0
    for j in range(1, 4):
        total_baris += i * j
    print(f"Jumlah baris {i} = {total_baris}")
