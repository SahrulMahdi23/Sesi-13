def konversiinteger(teks):
    try:
        nilai_integer = int(teks)
        print(f"Nilai integer adalah {nilai_integer}")
    except ValueError:
        print("Kesalahan: Integer tidak valid")

konversiinteger("123") 
konversiinteger("abc")
[10.26, 3/6/2024]

def akseselemen(daftar_list, indeks):
    try:
        elemen = daftar_list[indeks]
        print(f"Elemen di indeks {indeks} adalah {elemen}")
    except IndexError:
        print("Kesalahan: Indeks di luar jangkauan")

list_saya = [1, 2, 3]
akseselemen(list_saya, 1) 
akseselemen(list_saya, 5)