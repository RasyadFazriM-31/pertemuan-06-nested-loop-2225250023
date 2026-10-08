# Latihan 4 - Menghitung Pasangan
# Untuk i dan j dari 1 sampai n, hitung banyak pasangan (i, j)
# yang memenuhi i + j <= n.

# Loop luar   : mengatur i (1 sampai n)
# Loop dalam  : mengatur j (1 sampai n)
# Kondisi     : if i + j <= n
# Counter     : count, bertambah 1 hanya jika kondisi terpenuhi
# Prediksi    : seluruh pasangan yang diperiksa = n x n

n = int(input("n: "))

# Validasi: ulangi sampai n positif
while n <= 0:
    print("n harus positif.")
    n = int(input("n: "))

count = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i + j <= n:
            count += 1

print(f"Banyak pasangan = {count}")
