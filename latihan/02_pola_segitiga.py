# Latihan 2 - Pola Segitiga
# Menerima n positif lalu mencetak pola bintang:
# baris ke-1 berisi 1 simbol, ..., baris ke-n berisi n simbol.

# Loop luar   : mengatur baris i (1 sampai n)
# Loop dalam  : mencetak i buah simbol "*" pada baris tersebut
# print()     : setelah loop dalam, pindah ke baris berikutnya
# Prediksi    : total simbol = 1 + 2 + ... + n

n = int(input("n: "))

# Validasi: ulangi sampai n positif
while n <= 0:
    print("n harus positif.")
    n = int(input("n: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
