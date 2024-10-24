'''

1. Inisialisasi Window:
    window = tkinter.Tk() membuat jendela utama untuk GUI.
    
2. Membuat Label dan Tombol:
    Label adalah widget untuk menampilkan teks di dalam jendela, seperti "LABEL 1", "LABEL 2", dan "LABEL 3".
    Button adalah widget untuk membuat tombol, seperti "TOMBOL 1", "TOMBOL 2", dan "TOMBOL 3".
3. Mengatur Tata Letak:
    pack() adalah metode yang digunakan untuk menambahkan widget ke jendela dan mengaturnya secara vertikal (satu di bawah yang lain).
4. Menampilkan GUI:
    window.mainloop() adalah loop utama yang menjaga agar jendela tetap terbuka dan aktif hingga pengguna menutupnya.
Pada catatan, penjelasan tentang class dan method:
    Komponen seperti Tk(), Label, dan Button adalah class, yaitu template objek.
    Metode seperti pack() digunakan untuk memanipulasi atau mengatur properti dari objek yang diciptakan dari kelas-kelas tersebut.
    Jika ingin mengatur posisi atau tata letak widget yang lebih kompleks, bisa juga menggunakan metode lain seperti grid() atau place().

'''



import tkinter
print(tkinter.__dict__)

# menginialisasi window
window = tkinter.Tk()

# atribut-atribut di window
label_1 = tkinter.Label(window, text="LABEL 1")  # (window -> label di dalam [window], text -> placeholder)
label_2 = tkinter.Label(window, text="LABEL 2")
label_3 = tkinter.Label(window, text="LABEL 3")
tombol_1 = tkinter.Button(window, text="TOMBOL 1")
tombol_2 = tkinter.Button(window, text="TOMBOL 2")
tombol_3 = tkinter.Button(window, text="TOMBOL 3")

# meletakkan atribut ke dalam window, pack()
label_1.pack()
label_2.pack()
label_3.pack()
tombol_1.pack()
tombol_2.pack()
tombol_3.pack()

# menampilkan GUI / Graphical User Interface
window.mainloop()


'''
catatan:

didalam package yang ada di python,
1. untuk yang awalnya huruf besar (misal : Tk(), Label, Button, dll) adalah == CLASS
2. untuk yang awalnya huruf kecil (misal : pack, dll) adalah == METHOD

# '''