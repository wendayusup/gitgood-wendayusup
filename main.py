def hitung_gaji(jam, tarif, bonus, tunjangan):
    return (jam * tarif + bonus + tunjangan) * 0.9

if __name__ == "__main__":
    print("Total:", hitung_gaji(8, 50000, 100000, 50000))