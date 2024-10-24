'''
Dalam Python, private variable adalah variabel yang tidak ingin diakses langsung dari luar kelas. Meskipun Python tidak benar-benar memiliki mekanisme untuk memproteksi variabel dengan ketat seperti di beberapa bahasa lain, Python menggunakan konvensi untuk menandai variabel sebagai "private".

Variabel private diindikasikan dengan menambahkan dua garis bawah (__) di awal nama variabel. Ini menyebabkan Python melakukan proses yang disebut name mangling, di mana nama variabel tersebut diubah sehingga tidak dapat diakses langsung dari luar kelas.


ctt: tekan alt+z supaya enak baca dokumentasi

'''

class AkunBank:
    def __init__(self, pemilik, saldo_awal):
        self.pemilik = pemilik               # Variabel publik
        self.__saldo = saldo_awal            # Variabel private (tidak bisa diakses langsung dari luar)

    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
        else:
            print("Jumlah setor harus lebih dari 0")

    def tarik(self, jumlah):
        if jumlah <= self.__saldo:
            self.__saldo -= jumlah
        else:
            print("Saldo tidak cukup")

    def cek_saldo(self):
        return f"Saldo saat ini: {self.__saldo}"

# Membuat objek AkunBank
akun_budi = AkunBank("Budi", 1000000)

# Mencoba mengakses variabel private secara langsung
# print(akun_budi.__saldo)  # Akan menyebabkan error: AttributeError

# Menggunakan metode untuk mengakses saldo
akun_budi.tarik(1000000)
print(akun_budi.cek_saldo())  

# Akses dengan name mangling (tidak disarankan, hanya untuk ilustrasi)
print(akun_budi._AkunBank__saldo)  