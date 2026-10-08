# Tugas 3 - Tabel Perkalian dan Statistik
#
# Program membentuk tabel perkalian 1 sampai n, lalu menghitung:
#   - jumlah setiap baris,
#   - total seluruh hasil perkalian,
#   - banyak hasil perkalian yang genap.
#
# Peran komponen:
#   Loop luar  (i)           : mengatur baris tabel, i = 1..n
#   Loop dalam (j)           : mengatur kolom tabel, j = 1..n
#   total_baris (akumulator) : direset di awal tiap baris, jumlah per baris
#   total_semua (akumulator) : dibuat sebelum kedua loop, jumlah keseluruhan
#   count_genap (counter)    : bertambah 1 hanya jika hasil genap
#
# Badan loop dalam dijalankan n x n kali.

print("Tabel Perkalian dan Statistik")
n = int(input("n: "))

# Validasi: ulangi sampai n bilangan bulat positif
while n <= 0:
    print("n harus positif.")
    n = int(input("n: "))

# Inisialisasi sebelum kedua loop (berlaku untuk seluruh tabel)
total_semua = 0
count_genap = 0

for i in range(1, n + 1):
    total_baris = 0              # reset untuk setiap baris baru
    for j in range(1, n + 1):
        hasil = i * j
        print(f"{hasil:4}", end="")
        total_baris += hasil
        total_semua += hasil
        if hasil % 2 == 0:
            count_genap += 1
    print(f" | jumlah baris = {total_baris}")

print(f"Total seluruh hasil = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")
