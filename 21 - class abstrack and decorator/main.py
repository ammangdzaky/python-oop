from abc import ABC, abstractmethod

class Button(ABC):
    def __init__(self, set_link):
        # Menggunakan _link sebagai variabel sementara untuk menyimpan nilai link awal
        self._link = set_link

    @abstractmethod
    def click(self): # harus ada pada class rutunan
        pass

    @property
    @abstractmethod
    def link(self): # harus ada pada class turunan
        pass

class PushButton(Button):
    def click(self):
        print(f"Go To: {self.link}")

    # Implementasi getter dan setter untuk properti link
    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, input):
        self._link = input

# Penggunaan
tombol1 = PushButton("www.kelasterbuka.id")
tombol1.click()  # Output: Go To: www.kelasterbuka.id
