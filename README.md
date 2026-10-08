# Pertemuan 06 Nested Loop Python

Nama: Rasyad Fazri Mulyono
NIM: 2225250023
Kelas: 3A
Program Studi: S1 Pendidikan Matematika FKIP Universitas Sultan Ageng Tirtayasa
Mata Kuliah: Algoritma dan Pemrograman

## Tujuan

Menggunakan nested loop, pola, akumulasi, dan pencacahan.

## Struktur Folder

```
pertemuan-06-nested-loop-2225250023/
|-- README.md
|-- .gitignore
|-- latihan/
|   |-- 01_pasangan_indeks.py
|   |-- 02_pola_segitiga.py
|   |-- 03_jumlah_per_baris.py
|   `-- 04_hitung_pasangan.py
`-- tugas/
    `-- tabel_perkalian_dan_statistik.py
```

## Cara Menjalankan

Jalankan dari folder utama proyek. Pada Windows gunakan `python`, pada macOS atau Linux gunakan `python3`.

```
python3 latihan/01_pasangan_indeks.py
python3 latihan/02_pola_segitiga.py
python3 latihan/03_jumlah_per_baris.py
python3 latihan/04_hitung_pasangan.py
python3 tugas/tabel_perkalian_dan_statistik.py
```

Program Latihan 2, Latihan 4, dan Tugas 3 meminta input `n` (bilangan bulat positif).

## Algoritma Tugas 3

Program `tugas/tabel_perkalian_dan_statistik.py` membentuk tabel perkalian n x n, lalu menghitung jumlah tiap baris, total seluruh hasil, dan banyak hasil genap.

Peran komponen:

| Komponen | Peran |
|---|---|
| Loop luar (`i`, 1 sampai n) | Mengatur baris tabel |
| Loop dalam (`j`, 1 sampai n) | Mengatur kolom tabel, dijalankan penuh untuk setiap `i` |
| `total_baris` (akumulator) | Jumlah hasil pada satu baris, direset ke 0 di awal setiap iterasi loop luar |
| `total_semua` (akumulator) | Jumlah seluruh hasil, diinisialisasi sebelum kedua loop |
| `count_genap` (counter) | Bertambah 1 hanya jika `hasil` genap, diinisialisasi sebelum kedua loop |

Langkah algoritma:

1. Baca n, ulangi dengan `while` selama n <= 0.
2. Set `total_semua = 0` dan `count_genap = 0`.
3. Ulangi `i` dari 1 sampai n.
4. Set `total_baris = 0` untuk baris `i`.
5. Ulangi `j` dari 1 sampai n.
6. Hitung `hasil = i * j`, lalu cetak.
7. Tambahkan `hasil` ke `total_baris` dan `total_semua`.
8. Jika `hasil % 2 == 0`, tambah `count_genap`.
9. Setelah loop dalam selesai, tampilkan `total_baris`.
10. Setelah kedua loop selesai, tampilkan `total_semua` dan `count_genap`.

## Hasil Pengujian

### Tugas 3

| Input n | Jumlah pasangan | Hasil yang diharapkan (total semua, genap) | Keluaran aktual (total semua, genap) | Status |
|---|---|---|---|---|
| 1 | 1 | 1, 0 | 1, 0 | Sesuai |
| 2 | 4 | 9, 3 | 9, 3 | Sesuai |
| 3 | 9 | 36, 5 | 36, 5 | Sesuai |
| 5 | 25 | 225, 16 | 225, 16 | Sesuai |
| 0, -2, lalu 3 | - | Diminta ulang sampai valid, lalu seperti n = 3 | Muncul pesan "n harus positif." dua kali, lalu seperti n = 3 | Sesuai |

Contoh keluaran untuk n = 3:

```
Tabel Perkalian dan Statistik
n:    1   2   3 | jumlah baris = 6
   2   4   6 | jumlah baris = 12
   3   6   9 | jumlah baris = 18
Total seluruh hasil = 36
Banyak hasil genap = 5
```

Pembuktian `count_genap` untuk n = 3: hasil genap adalah 2, 4, 6, 2, 6, yaitu 5 buah. Nilai ini sama dengan keluaran program. Untuk n = 5, nilai yang ganjil hanya muncul dari pasangan i dan j yang keduanya ganjil (3 x 3 = 9 pasangan), sehingga genapnya 25 - 9 = 16, sama dengan keluaran program.

### Latihan

| Latihan | Input | Hasil yang diharapkan | Keluaran aktual | Status |
|---|---|---|---|---|
| 1. Pasangan indeks | - | 12 pasangan, count = 12 | 12 pasangan, count = 12 | Sesuai |
| 2. Pola segitiga | n = 1 | 1 baris berisi 1 bintang | 1 baris berisi 1 bintang | Sesuai |
| 2. Pola segitiga | n = 3 | baris berisi 1, 2, 3 bintang | baris berisi 1, 2, 3 bintang | Sesuai |
| 2. Pola segitiga | n = 5 | baris berisi 1 sampai 5 bintang | baris berisi 1 sampai 5 bintang | Sesuai |
| 3. Jumlah per baris | - | 6, 12, 18, 24 | 6, 12, 18, 24 | Sesuai |
| 4. Hitung pasangan | n = 2 | 1 | 1 | Sesuai |
| 4. Hitung pasangan | n = 3 | 3 | 3 | Sesuai |
| 4. Hitung pasangan | n = 5 | 10 | 10 | Sesuai |

## Tracing

### Tugas 3, n = 2

| i | j | hasil = i * j | total_baris sesudah | total_semua sesudah | count_genap sesudah |
|---|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 1 | 0 |
| 1 | 2 | 2 | 3 | 3 | 1 |
| 2 | 1 | 2 | 2 (direset lalu bertambah) | 5 | 2 |
| 2 | 2 | 4 | 6 | 9 | 3 |

Setelah i = 1 selesai, `total_baris` dicetak (3) lalu direset ke 0 pada awal i = 2. Variabel `total_semua` dan `count_genap` tidak direset sehingga terus terkumpul sampai nilai akhir 9 dan 3.

### Latihan 4, n = 3 (kondisi i + j <= 3)

| i | j | i + j | Memenuhi? | count sesudah |
|---|---|---|---|---|
| 1 | 1 | 2 | Ya | 1 |
| 1 | 2 | 3 | Ya | 2 |
| 1 | 3 | 4 | Tidak | 2 |
| 2 | 1 | 3 | Ya | 3 |
| 2 | 2 | 4 | Tidak | 3 |
| 2 | 3 | 5 | Tidak | 3 |
| 3 | 1 | 4 | Tidak | 3 |
| 3 | 2 | 5 | Tidak | 3 |
| 3 | 3 | 6 | Tidak | 3 |

Dari 9 pasangan yang diperiksa, 3 pasangan memenuhi, yaitu (1,1), (1,2), dan (2,1).

## Analisis Efisiensi

Untuk input n, loop luar berjalan n kali dan loop dalam berjalan n kali pada setiap iterasi luar. Jadi badan loop dalam dieksekusi n x n = n² kali. Pernyataan `hasil = i * j` juga dieksekusi n² kali.

| n | Iterasi badan loop dalam |
|---|---|
| 1 | 1 |
| 2 | 4 |
| 3 | 9 |
| 5 | 25 |
| 10 | 100 |
| 100 | 10.000 |

Tidak ada loop atau perhitungan yang berulang tanpa diperlukan. Setiap pasangan (i, j) diproses tepat satu kali, dan batas `range(1, n + 1)` sudah sesuai kebutuhan tabel. Ketika n membesar, bagian yang paling banyak melakukan operasi adalah loop dalam.

## Refleksi

Kesalahan nested loop yang saya analisis itu ada di penempatan inisialisasi akumulator per baris. Kalau `total_baris = 0` ditaruh sebelum loop luar, nilainya tidak akan direset setiap kali masuk ke baris baru. Akibatnya, untuk `n = 3`, jumlah yang tercetak jadi 6, 18, dan 36 karena hasilnya terus menumpuk, padahal seharusnya 6, 12, dan 18. Jadi, perbaikannya adalah memindahkan `total_baris = 0` ke dalam loop luar, tepat sebelum loop dalam, supaya setiap baris dimulai lagi dari nol. Sementara itu, `total_semua` memang harus diletakkan sebelum kedua loop karena nilainya digunakan untuk menghitung total dari seluruh tabel.

## Sumber dan Bantuan

- Bahan ajar Pertemuan 6 Algoritma dan Pemrograman (Dr. Aan Hendrayana, S.Si., M.Pd.), yang menjadi acuan soal dan contoh kode.
- Bantuan AI (Claude) digunakan untuk menyusun draf kode latihan, Tugas 3, dan README. Kode, tracing, dan analisis sudah saya jalankan dan pelajari sehingga dapat saya jelaskan.
