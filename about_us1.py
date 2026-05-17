import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import os

# ---------------- Root Window ----------------
root = tk.Tk()
root.title("Handwriting Analysis - About Us")
root.state("zoomed")   # Auto adjust to laptop resolution

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# ---------------- Colors ----------------
bg_main = "#0f1c2e"
sidebar_color = "#1f2a3a"
card_color = "#1c2b40"
button_blue = "#3b82f6"
button_red = "#ef4444"

root.configure(bg=bg_main)

# ---------------- Sidebar ----------------
sidebar = Frame(root, bg=sidebar_color, width=220)
sidebar.pack(side="left", fill="y")

Label(sidebar, text="AI Handwriting",
      bg=sidebar_color, fg="white",
      font=("Arial", 16, "bold")).pack(pady=20)

def go_dashboard():
    root.destroy()
    os.system("detect1.py")   # change if needed

Button(sidebar, text="Back to Dashboard",
       bg=button_blue, fg="white",
       width=18, relief="flat",
       command=go_dashboard).pack(pady=20)

Button(sidebar, text="Exit",
       bg=button_red, fg="white",
       width=18, relief="flat",
       command=root.destroy).pack(side="bottom", pady=20)

# ---------------- Header ----------------
Label(root,
      text="About Us",
      bg=bg_main,
      fg="white",
      font=("Arial", 22, "bold")).place(x=260, y=20)

# ---------------- Developer Card Function ----------------
def create_dev_card(parent, name, email, image_path, x, y):
    card = Frame(parent, bg=card_color, width=350, height=250)
    card.place(x=x, y=y)

    try:
        img = Image.open(image_path)
        img = img.resize((100, 100))
        photo = ImageTk.PhotoImage(img)
        img_label = Label(card, image=photo, bg=card_color)
        img_label.image = photo
        img_label.pack(pady=10)
    except:
        Label(card, text="No Image",
              bg=card_color, fg="white").pack(pady=10)

    Label(card, text=name,
          bg=card_color, fg="white",
          font=("Arial", 14, "bold")).pack()

    Label(card, text=email,
          bg=card_color, fg="#22c55e",
          font=("Arial", 11)).pack(pady=5)

# ---------------- Dynamic Layout Settings ----------------

left_margin = 260
top_margin = 120

dev_card_width = 350
dev_card_height = 250

column_gap = 60
row_gap = 50

summary_card_width = 420
summary_gap = 80

# Calculate dynamic positions
col1_x = left_margin
col2_x = col1_x + dev_card_width + column_gap
summary_x = col2_x + dev_card_width + summary_gap

# Prevent overflow on small screens
if summary_x + summary_card_width > screen_width:
    summary_x = screen_width - summary_card_width - 40

# ---------------- Developer Cards ----------------

create_dev_card(root,
                "Sujit Sable",
                "sujitsable1212@gmail.com",
                "sujit.jpeg",
                col1_x, top_margin)

create_dev_card(root,
                "Purva Kale",
                "purvakale1301@gmail.com",
                "purva.jpeg",
                col2_x, top_margin)

create_dev_card(root,
                "Rushikesh Jadhao",
                "rushikeshjadhao29@gmail.com",
                "img1.png",
                col1_x, top_margin + dev_card_height + row_gap)

create_dev_card(root,
                "Ankush Lakade",
                "lakadeankush2020@gmail.com",
                "ankush.jfif",
                col2_x, top_margin + dev_card_height + row_gap)

# ---------------- Summary Info Card ----------------

summary_card = Frame(root, bg=card_color,
                     width=summary_card_width, height=600)
summary_card.place(x=summary_x, y=top_margin)

Label(summary_card,
      text="About The System",
      bg=card_color,
      fg="white",
      font=("Arial", 18, "bold")).pack(pady=(20, 5))

Frame(summary_card, bg="#3b82f6",
      height=3, width=350).pack(pady=5)

description_text = """
Our AI-Based Handwriting Analysis System
uses machine learning techniques to
analyze handwriting samples and
predict personality traits.

The system processes image inputs,
extracts writing patterns, and applies
trained models to detect behavioral
characteristics with confidence scores.
"""

Label(summary_card,
      text=description_text,
      bg=card_color,
      fg="lightgray",
      justify="left",
      font=("Arial", 11),
      wraplength=360).pack(pady=10)

Label(summary_card,
      text="Key Features",
      bg=card_color,
      fg="#22c55e",
      font=("Arial", 14, "bold")).pack(pady=(20, 10))

features = [
    "✔ AI-powered personality prediction",
    "✔ Image-based handwriting analysis",
    "✔ Confidence percentage output",
    "✔ User-friendly dashboard UI",
    "✔ Fast & Accurate Results"
]

for feature in features:
    Label(summary_card,
          text=feature,
          bg=card_color,
          fg="white",
          anchor="w",
          font=("Arial", 11)).pack(fill="x", padx=40, pady=4)

# ---------------- Footer ----------------
Label(root,
      text="AI-Based Handwriting Analysis System | 2026",
      bg=bg_main,
      fg="gray",
      font=("Arial", 9)).place(x=350, y=screen_height - 80)

root.mainloop()
