import random
import tkinter as tk
from tkinter import messagebox
import pyperclip

# Karakter listelerini oluştur
char_1 = [chr(harf) for harf in range(ord('a'), ord('z') + 1)]
char_2 = [chr(harf) for harf in range(ord('A'), ord('Z') + 1)]
char_3 = [str(rakam) for rakam in range(10)]
char_4 = list("!@#$%^&*()-_=+[]{};:,.<>?/")

tum_karakterler = char_1 + char_2 + char_3 + char_4

# Şifre oluşturma fonksiyonu
def sifre_olustur():
    try:
        uzunluk = int(entry_uzunluk.get())
        sifre = ''.join(random.choice(tum_karakterler) for _ in range(uzunluk))
        entry_sonuc.delete(0, tk.END)
        entry_sonuc.insert(0, sifre)
    except:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin!")

# Şifreyi kopyalama fonksiyonu
def kopyala():
    sifre = entry_sonuc.get()
    if sifre:
        pyperclip.copy(sifre)
        messagebox.showinfo("Kopyalandı", "Şifre panoya kopyalandı!")

# Ana pencere
pencere = tk.Tk()
pencere.title("Güçlü Şifre Oluşturucu")
pencere.geometry("400x250")
pencere.resizable(False, False)
pencere.configure(bg="#282a36")

# Stil tanımları
label_font = ("Arial", 12, "bold")
entry_font = ("Consolas", 12)
button_font = ("Arial", 11, "bold")

# Şifre uzunluğu label + entry
tk.Label(pencere, text="Şifre Uzunluğu:", font=label_font, fg="white", bg="#282a36").pack(pady=10)
entry_uzunluk = tk.Entry(pencere, font=entry_font, justify="center", width=10)
entry_uzunluk.pack()

# Şifre oluştur butonu
tk.Button(
    pencere, text="Şifre Oluştur", font=button_font,
    command=sifre_olustur, bg="#50fa7b", fg="black", relief="groove", bd=2
).pack(pady=10)

# Şifre sonucu
entry_sonuc = tk.Entry(pencere, font=entry_font, justify="center", width=30)
entry_sonuc.pack(pady=5)

# Kopyala butonu
tk.Button(
    pencere, text="Kopyala", font=button_font,
    command=kopyala, bg="#ff79c6", fg="black", relief="groove", bd=2
).pack(pady=10)

pencere.mainloop()
