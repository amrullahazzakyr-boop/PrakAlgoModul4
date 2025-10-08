# Input bulan dan tahun
bulan = int(input("Masukkan bulan (1-12): "))
tahun = int(input("Masukkan tahun: "))

    # Periksa validitas bulan
if bulan < 1 or bulan > 12:
        print("❌ Bulan tidak valid! Silakan masukkan antara 1 - 12.")
else:
        # Tentukan jumlah hari
        if bulan in [1, 3, 5, 7, 8, 10, 12]:
            hari = 31
        elif bulan in [4, 6, 9, 11]:
            hari = 30
        else:  # bulan == 2
            # Cek tahun kabisat
            if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
                hari = 29
            else:
                hari = 28
        
        print(f"\nBulan ke-{bulan} tahun {tahun} memiliki {hari} hari.")