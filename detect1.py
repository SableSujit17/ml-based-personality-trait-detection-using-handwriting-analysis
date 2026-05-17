import tkinter as tk
import sys
import os
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from classify1 import predict_personality

# ---------------- Root Window ----------------
root = tk.Tk()
root.title("Handwriting Analysis - Dashboard")
# Dynamic screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{screen_width}x{screen_height}")
root.state("zoomed")   # maximize window

# -------- Background Image --------
bg_img = Image.open("neural2.jpeg")
bg_img = bg_img.resize((screen_width, screen_height))
bg_photo = ImageTk.PhotoImage(bg_img)

bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

root.configure(bg="#0f1c2e")

# ---------------- Get Logged User ----------------
if len(sys.argv) > 1:
    logged_user = sys.argv[1]
else:
    logged_user = "User"

# Extract First Name
first_name = logged_user.split()[0]


# ---------------- Colors ----------------
bg_main = "#0f1c2e"
sidebar_color = "#1f2a3a"
card_color = "#1c2b40"
button_blue = "#3b82f6"
button_green = "#22c55e"
button_orange = "#f59e0b"
button_red = "#ef4444"

# ---------------- Hover Effect ----------------
def on_enter(e):
    e.widget["background"] = "#2563eb"

def on_leave(e):
    e.widget["background"] = button_blue

root.configure(bg=bg_main)

# ---------------- Global Variables ----------------
selected_img_path = None
uploaded_image = None

# ---------------- Sidebar ----------------
sidebar = Frame(root, bg=sidebar_color, width=220)
sidebar.pack(side="left", fill="y")

Label(sidebar, text="AI Handwriting",
      bg=sidebar_color, fg="white",
      font=("Arial", 16, "bold")).pack(pady=20)

def logout():
    root.destroy()
    os.system('login.py')

def aboutUs():
    root.destroy()
    os.system('about_us1.py')

Button(sidebar, text="Logout",
       bg=button_red, fg="white",
       width=18, relief="flat",
       command=logout).pack(side="bottom", pady=20)

Button(sidebar, text="About Us",
       bg="#0f1c2e", fg="white",
       width=18, relief="flat",
       command=aboutUs).pack(side="top", pady=20)

# ---------------- Header ----------------
welcome_label = Label(
    root,
    text=f"Welcome, {first_name}",
    bg=bg_main,
    fg="white",
    font=("Arial", 20, "bold")
)
welcome_label.place(x=250, y=20)


# ---------------- Modern Card Function ----------------
def create_card(x_pos, title):

    shadow = Frame(root, bg="#0a1422",
                   width=400, height=400)
    shadow.place(x=x_pos+8, y=128)

    frame = Frame(root,
                  bg=card_color,
                  width=400,
                  height=400,
                  highlightbackground="#2e3c55",
                  highlightthickness=1)
    frame.place(x=x_pos, y=120)

    frame.pack_propagate(False)

    Label(frame,
          text=title,
          bg=card_color,
          fg="white",
          font=("Arial", 15, "bold")).pack(pady=20)

    return frame


# -------- Center Both Cards --------
card_width = 400
spacing = 100
total_width = (card_width * 2) + spacing
start_x = (screen_width - total_width) // 2


# ---------------- Upload Section ----------------
upload_frame = create_card(start_x, "Upload Handwriting Sample")

preview_label = Label(upload_frame, bg=card_color)
preview_label.pack(pady=10)


def open_file():
    global selected_img_path, uploaded_image

    filename = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg *.png *.jpeg")]
    )

    if filename:
        selected_img_path = filename

        img = Image.open(filename)
        img = img.resize((250, 180))
        uploaded_image = ImageTk.PhotoImage(img)
        preview_label.config(image=uploaded_image)


choose_btn = Button(upload_frame,
       text="Choose Image",
       bg=button_blue,
       fg="white",
       width=20,
       relief="flat",
       command=open_file)

choose_btn.pack(pady=10)

# -------- Reset Function --------
def reset_all():
    global selected_img_path
    selected_img_path = None
    preview_label.config(image="")
    detected_trait_label.config(text="--")
    accuracy_label.config(text="--")
    percentage_label.config(text="0%")
    progress_bar["value"] = 0


# -------- Reset Button --------
Button(upload_frame,
       text="Reset",
       bg=button_orange,
       fg="white",
       width=20,
       relief="flat",
       command=reset_all).pack(pady=5)

choose_btn.bind("<Enter>", on_enter)
choose_btn.bind("<Leave>", on_leave)


# ---------------- Analysis Section ----------------
analysis_frame = create_card(start_x + card_width + spacing,
                             "AI Personality Analysis")

progress_bar = ttk.Progressbar(
    analysis_frame,
    orient="horizontal",
    length=300,
    mode="determinate"
)
progress_bar.pack(pady=15)

percentage_label = Label(analysis_frame,
                         text="0%",
                         bg=card_color,
                         fg="#22c55e",
                         font=("Arial", 16, "bold"))
percentage_label.pack()

Label(analysis_frame,
      text="Detected Trait:",
      bg=card_color,
      fg="white",
      font=("Arial", 12)).pack(pady=(15, 0))

detected_trait_label = Label(analysis_frame,
                             text="--",
                             bg=card_color,
                             fg="#3b82f6",
                             font=("Arial", 12, "bold"))
detected_trait_label.pack()

Label(analysis_frame,
      text="Accuracy:",
      bg=card_color,
      fg="white",
      font=("Arial", 12)).pack(pady=(10, 0))

accuracy_label = Label(analysis_frame,
                       text="--",
                       bg=card_color,
                       fg="#22c55e",
                       font=("Arial", 12, "bold"))
accuracy_label.pack()


def animate_progress(target_value):
    current = 0

    def step():
        nonlocal current
        if current < target_value:
            current += 2
            progress_bar["value"] = current
            percentage_label.config(text=f"{current}%")
            root.after(20, step)

    step()


def analyze_image():
    global selected_img_path

    if not selected_img_path:
        messagebox.showerror("Error", "Please select an image first!")
        return

    detected_trait_label.config(text="Analyzing...")
    accuracy_label.config(text="Processing...")
    progress_bar["value"] = 0
    percentage_label.config(text="0%")

    root.update()

    label, confidence = predict_personality(selected_img_path)
    if confidence >= 80:
        percentage_label.config(fg="#22c55e")  # Green
    elif confidence >= 50:
        percentage_label.config(fg="#f59e0b")  # Orange
    else:
        percentage_label.config(fg="#ef4444")  # Red

    animate_progress(int(confidence))

    detected_trait_label.config(text=label)
    accuracy_label.config(text=f"{confidence:.2f}%")


Button(analysis_frame,
       text="Analyze Now",
       bg=button_green,
       fg="white",
       width=20,
       relief="flat",
       command=analyze_image).pack(pady=20)

# ---------------- Footer ----------------
footer = Label(root,
      text="AI-Based Handwriting Analysis System | 2026",
      bg=bg_main,
      fg="gray",
      font=("Arial", 9))

footer.pack(side="bottom", pady=10)

# Start GUI
root.mainloop()