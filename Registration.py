
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

# ---------------- Variables ----------------
fname = StringVar()
lname = StringVar()
Email = StringVar()
gender = IntVar()
country = StringVar()
uname = StringVar()
pwd = StringVar()

# ---------------- Navigation ----------------
def home():
    root.destroy()
    os.system('home.py')

def register():
    if not all([
        fname.get(), lname.get(), Email.get(),
        uname.get(), pwd.get(), country.get()
    ]):
        messagebox.showwarning("Input Error", "All fields are required")
        return

    conn = sqlite3.connect('Form1.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user (
            fname TEXT,
            lname TEXT,
            email TEXT,
            gender TEXT,
            country TEXT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)

    cursor.execute("""
        INSERT INTO user
        (fname, lname, email, gender, country, username, password)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        fname.get(),
        lname.get(),
        Email.get(),
        gender.get(),
        country.get(),
        uname.get(),
        pwd.get()
    ))

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Registration Successful")
    root.destroy()
    os.system('login.py')

# ---------------- Background Image ----------------
bg_img = Image.open("hnd1.jpg")
bg_img = bg_img.resize((WINDOW_WIDTH, WINDOW_HEIGHT))
bg_photo = ImageTk.PhotoImage(bg_img)

Label(root, image=bg_photo).place(x=0, y=0)

# ---------------- Page Heading ----------------
Label(
    root,
    text="Create Your Account",
    font=("Segoe UI", 28, "bold"),
    fg="white",
    bg="#000000",
    padx=25,
    pady=10
).place(x=60, y=80)

Label(
    root,
    text="Join the AI-powered handwriting analysis system",
    font=("Segoe UI", 14),
    fg="#e5e7eb",
    bg="#000000",
    padx=25,
    pady=6
).place(x=60, y=145)

# ---------------- Registration Card ----------------
CARD_WIDTH = 500
CARD_HEIGHT = 560

card_x = 800
card_y = (WINDOW_HEIGHT - CARD_HEIGHT) // 2

card = Frame(root, bg="white", width=CARD_WIDTH, height=CARD_HEIGHT)
card.place(x=card_x, y=card_y)

# ---------------- Card Header ----------------
Label(
    card,
    text="User Registration",
    font=("Segoe UI", 20, "bold"),
    bg="white",
    fg="#111827"
).place(x=40, y=30)

Label(
    card,
    text="Fill in the details below",
    font=("Segoe UI", 11),
    bg="white",
    fg="#6b7280"
).place(x=40, y=70)

# ---------------- Input Fields ----------------
def field(label, var, y, show=None):
    Label(
        card,
        text=label,
        font=("Segoe UI", 11),
        bg="white",
        fg="#374151"
    ).place(x=40, y=y)

    Entry(
        card,
        textvariable=var,
        font=("Segoe UI", 12),
        width=34,
        relief=FLAT,
        bg="#f3f4f6",
        show=show
    ).place(x=40, y=y+30)

field("First Name", fname, 110)
field("Last Name", lname, 170)
field("Email Address", Email, 230)

# ---------------- Gender ----------------
Label(
    card,
    text="Gender",
    font=("Segoe UI", 11),
    bg="white",
    fg="#374151"
).place(x=40, y=290)

Radiobutton(
    card, text="Male", variable=gender, value=1,
    bg="white", font=("Segoe UI", 10)
).place(x=40, y=320)

Radiobutton(
    card, text="Female", variable=gender, value=2,
    bg="white", font=("Segoe UI", 10)
).place(x=120, y=320)

# ---------------- Country ----------------
Label(
    card,
    text="Country",
    font=("Segoe UI", 11),
    bg="white",
    fg="#374151"
).place(x=260, y=290)

countries = ['India', 'USA', 'UK', 'Nepal', 'China', 'South Africa']
OptionMenu(card, country, *countries).place(x=260, y=320)
country.set("Select")

# ---------------- Username & Password ----------------
field("Username", uname, 360)
field("Password", pwd, 420, show="*")

# ---------------- Buttons ----------------
Button(
    card,
    text="REGISTER",
    font=("Segoe UI", 12, "bold"),
    bg="#2563eb",
    fg="white",
    relief=FLAT,
    width=34,
    command=register
).place(x=40, y=480)

Button(
    card,
    text="HOME",
    font=("Segoe UI", 11),
    bg="#9ca3af",
    fg="white",
    relief=FLAT,
    width=34,
    command=home
).place(x=40, y=520)

root.mainloop()
