import random
import tkinter as tk
from tkinter import messagebox
import pyperclip

# Create character lists
char_1 = [chr(harf) for harf in range(ord('a'), ord('z') + 1)]
char_2 = [chr(harf) for harf in range(ord('A'), ord('Z') + 1)]
char_3 = [str(rakam) for rakam in range(10)]
char_4 = list("!@#$%^&*()-_=+[]{};:,.<>?/")

all_characters = char_1 + char_2 + char_3 + char_4

# Password generation function
def generate_password():
    try:
        length = int(entry_length.get())
        password = ''.join(random.choice(all_characters) for _ in range(length))
        entry_result.delete(0, tk.END)
        entry_result.insert(0, password)
    except:
        messagebox.showerror("Error", "Please enter a valid number!")

# Copy password function
def copy():
    password = entry_result.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# Main window
window = tk.Tk()
window.title("Strong Password Generator")
window.geometry("400x250")
window.resizable(False, False)
window.configure(bg="#282a36")

# Style definitions
label_font = ("Arial", 12, "bold")
entry_font = ("Consolas", 12)
button_font = ("Arial", 11, "bold")

# Password length label + entry
tk.Label(window, text="Password Length:", font=label_font, fg="white", bg="#282a36").pack(pady=10)
entry_length = tk.Entry(window, font=entry_font, justify="center", width=10)
entry_length.pack()

# Generate password button
tk.Button(
    window, text="Generate Password", font=button_font,
    command=generate_password, bg="#50fa7b", fg="black", relief="groove", bd=2
).pack(pady=10)

# Password result
entry_result = tk.Entry(window, font=entry_font, justify="center", width=30)
entry_result.pack(pady=5)

# Copy button
tk.Button(
    window, text="Copy", font=button_font,
    command=copy, bg="#ff79c6", fg="black", relief="groove", bd=2
).pack(pady=10)

window.mainloop()
