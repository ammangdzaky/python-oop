import tkinter

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

