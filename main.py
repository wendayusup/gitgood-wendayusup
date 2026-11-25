def hitung_gaji(jam, tarif, bonus, tunjangan):
    return jam * tarif + bonus + tunjangan

if __name__ == "__main__":
    print("Total:", hitung_gaji (1000, 1000, 1000))

# TODO: tambahkan parameter pajak dinamis