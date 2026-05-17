from tkinter import *
from tkinter import messagebox
import sqlite3
import os
from PIL import ImageTk, Image

# ---------------- Root Window ----------------
root = Tk()
root.title("Handwriting Analysis System")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{screen_width}x{screen_height}")
root.state("zoomed")

WINDOW_WIDTH = screen_width
WINDOW_HEIGHT = screen_height
root.configure(bg="#1f2933")

# ---------------- Variables ----------------
uname = StringVar()
pwd = StringVar()

# ---------------- Functions ----------------
def home():
    root.destroy()
    os.system('home.py')

def database():
    name1 = uname.get()
    name2 = pwd.get()

    if name1 == "" or name2 == "":
        messagebox.showwarning("Input Error", "All fields are required")
        return

    conn = sqlite3.connect('Form1.db')
    cursor = conn.cursor()
    cursor.execute(
        'SELECT * FROM user WHERE username=? AND password=?',
        (name1, name2)
    )
    result = cursor.fetchone()
    conn.close()

    if result:
        messagebox.showinfo("Login Success", "Welcome to the System!")
        root.destroy()
        os.system(f'detect1.py {name1}')
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

# ---------------- Left Image Panel ----------------
img = Image.open("hnd1.jpg")
img = img.resize((650, WINDOW_HEIGHT))
photo = ImageTk.PhotoImage(img)

img_label = Label(root, image=photo, bg="#1f2933")
img_label.place(x=0, y=0)

# ---------------- Right Login Card ----------------
CARD_WIDTH = 420
CARD_HEIGHT = 500

card_x = 800
card_y = (WINDOW_HEIGHT - CARD_HEIGHT) // 2

card = Frame(root, bg="#ffffff", width=CARD_WIDTH, height=CARD_HEIGHT)
card.place(x=card_x, y=card_y)

# ---------------- Titles ----------------
Label(
    card,
    text="Handwriting Analysis",
    font=("Segoe UI", 18, "bold"),
    bg="white",
    fg="#111827"
).place(x=40, y=40)

Label(
    card,
    text="Login to your account",
    font=("Segoe UI", 11),
    bg="white",
    fg="#6b7280"
).place(x=40, y=80)

# ---------------- Username ----------------
Label(
    card,
    text="Username",
    font=("Segoe UI", 11),
    bg="white",
    fg="#374151"
).place(x=40, y=140)

Entry(
    card,
    textvariable=uname,
    font=("Segoe UI", 12),
    width=32,
    relief=FLAT,
    bg="#f3f4f6"
).place(x=40, y=170)

# ---------------- Password ----------------
Label(
    card,
    text="Password",
    font=("Segoe UI", 11),
    bg="white",
    fg="#374151"
).place(x=40, y=220)

Entry(
    card,
    textvariable=pwd,
    font=("Segoe UI", 12),
    width=32,
    relief=FLAT,
    bg="#f3f4f6",
    show="*"
).place(x=40, y=250)

# ---------------- Buttons ----------------
Button(
    card,
    text="LOGIN",
    font=("Segoe UI", 12, "bold"),
    bg="#2563eb",
    fg="white",
    relief=FLAT,
    width=32,
    height=1,
    command=database
).place(x=40, y=320)

Button(
    card,
    text="HOME",
    font=("Segoe UI", 11),
    bg="#9ca3af",
    fg="white",
    relief=FLAT,
    width=32,
    height=1,
    command=home
).place(x=40, y=370)

# ---------------- Footer ----------------
Label(
    card,
    text="© Handwriting Analysis System",
    font=("Segoe UI", 9),
    bg="white",
    fg="#9ca3af"
).place(x=95, y=450)

root.mainloop()
