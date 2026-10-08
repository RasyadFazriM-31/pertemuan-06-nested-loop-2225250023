# Latihan 1 - Pasangan Indeks
# Menampilkan seluruh pasangan (i, j) untuk i = 1..3 dan j = 1..4,
# lalu menampilkan banyak pasangan.

# Loop luar   : mengatur nilai i (1 sampai 3)
# Loop dalam  : mengatur nilai j (1 sampai 4), diulang penuh untuk setiap i
# Counter     : count, bertambah 1 setiap satu pasangan dicetak
# Prediksi    : 3 x 4 = 12 pasangan

count = 0
for i in range(1, 4):
    for j in range(1, 5):
        print(i, j)
        count += 1

print(f"Banyak pasangan = {count}")
