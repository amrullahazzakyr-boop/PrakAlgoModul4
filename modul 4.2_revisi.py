# Fungsi untuk mengecek apakah tahun kabisat
def is_kabisat(tahun):
    return (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)

# Daftar jumlah hari default untuk tiap bulan (indeks 1–12)
jumlah_hari = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Perulangan while untuk validasi input
while True:
    try:
        bulan = int(input("Masukkan bulan (1-12): "))
        tahun = int(input("Masukkan tahun: "))

        if 1 <= bulan <= 12:
            # Jika Februari dan tahun kabisat
            if bulan == 2 and is_kabisat(tahun):
                print("Jumlah hari: 29")
            else:
                print(f"Jumlah hari: {jumlah_hari[bulan]}")
            break  # Keluar dari loop jika input valid
        else:
            print("Bulan harus antara 1 hingga 12. Coba lagi.\n")
    except ValueError:
        print("Input tidak valid. Masukkan angka yang benar.\n")