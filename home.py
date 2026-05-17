from tkinter import *
import os
import random
from PIL import ImageTk, Image

# ---------------- Root Window ----------------
root = Tk()
root.title("Handwriting Analysis System")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{screen_width}x{screen_height}")
root.state("zoomed")
root.resizable(False, False)

WINDOW_WIDTH = screen_width
WINDOW_HEIGHT = screen_height

# ---------------- Navigation Functions ----------------
def run_login():
    root.destroy()
    os.system('login.py')

def run_signup():
    root.destroy()
    os.system('Registration.py')

# ---------------- Canvas ----------------
canvas = Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# ---------------- Background Image ----------------
bg_img = Image.open("hnd1.jpg")
bg_img = bg_img.resize((WINDOW_WIDTH, WINDOW_HEIGHT))
bg_photo = ImageTk.PhotoImage(bg_img)

canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# ---------------- Neural Network Animation ----------------
nodes = []
node_count = 25

for i in range(node_count):

    x = random.randint(0, WINDOW_WIDTH)
    y = random.randint(0, WINDOW_HEIGHT)

    node = canvas.create_oval(
        x, y, x+6, y+6,
        fill="#38bdf8",
        outline=""
    )

    nodes.append({
        "id": node,
        "x": x,
        "y": y,
        "dx": random.uniform(-1,1),
        "dy": random.uniform(-1,1)
    })

lines = []

def draw_lines():

    for line in lines:
        canvas.delete(line)

    lines.clear()

    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):

            x1,y1,x2,y2 = canvas.coords(nodes[i]["id"])
            x3,y3,x4,y4 = canvas.coords(nodes[j]["id"])

            x1+=3
            y1+=3
            x3+=3
            y3+=3

            distance = ((x1-x3)**2 + (y1-y3)**2)**0.5

            if distance < 150:

                line = canvas.create_line(
                    x1,y1,x3,y3,
                    fill="#60a5fa",
                    width=1
                )

                lines.append(line)

def animate():

    for node in nodes:

        canvas.move(node["id"], node["dx"], node["dy"])

        x1,y1,x2,y2 = canvas.coords(node["id"])

        if x1 < 0 or x2 > WINDOW_WIDTH:
            node["dx"] *= -1

        if y1 < 0 or y2 > WINDOW_HEIGHT:
            node["dy"] *= -1

    draw_lines()

    root.after(40, animate)

animate()

# ---------------- Floating Title ----------------
canvas.create_text(
    120,
    120,
    text="Handwriting Analysis System",
    font=("Segoe UI", 38, "bold"),
    fill="white",
    anchor="w"
)

canvas.create_text(
    120,
    180,
    text="AI Based Personality Detection Through Handwriting",
    font=("Segoe UI", 16),
    fill="#e5e7eb",
    anchor="w"
)

canvas.create_text(
    120,
    240,
    text="Machine Learning • Image Processing • Personality Prediction",
    font=("Segoe UI", 13),
    fill="#d1d5db",
    anchor="w"
)

# ---------------- Action Card ----------------
CARD_WIDTH = 420
CARD_HEIGHT = 300

card_x = WINDOW_WIDTH - 520
card_y = (WINDOW_HEIGHT - CARD_HEIGHT) // 2

card = Frame(root, bg="white", width=CARD_WIDTH, height=CARD_HEIGHT)
card.place(x=card_x, y=card_y)

# ---------------- Card Content ----------------
Label(
    card,
    text="Get Started",
    font=("Segoe UI", 22, "bold"),
    bg="white",
    fg="#111827"
).place(x=40, y=40)

Label(
    card,
    text="Login or create a new account",
    font=("Segoe UI", 11),
    bg="white",
    fg="#6b7280"
).place(x=40, y=85)

# ---------------- Buttons ----------------
Button(
    card,
    text="LOGIN",
    font=("Segoe UI", 12, "bold"),
    bg="#2563eb",
    fg="white",
    relief=FLAT,
    width=30,
    cursor="hand2",
    command=run_login
).place(x=40, y=140)

Button(
    card,
    text="SIGN UP",
    font=("Segoe UI", 12),
    bg="#9ca3af",
    fg="white",
    relief=FLAT,
    width=30,
    cursor="hand2",
    command=run_signup
).place(x=40, y=195)

# ---------------- Footer ----------------
canvas.create_text(
    WINDOW_WIDTH/2,
    WINDOW_HEIGHT-40,
    text="© Personality Detection System Using Handwriting Analysis System ",
    font=("Segoe UI", 10),
    fill="#d1d5db"
)

root.mainloop()