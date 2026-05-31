import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

from app.data.database import register_user
from app.utils.paths import image_path
from app.ui.theme import (
    create_shadow,
    font,
    style_button
)


class RegisterView(tk.Frame):

    def __init__(self, parent, controller):

        super().__init__(parent)

        self.controller = controller

        self.configure(bg="#020617")

        # ================= SCREEN =================
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        WINDOW_WIDTH = screen_width
        WINDOW_HEIGHT = screen_height

        # ================= VARIABLES =================
        self.fname = tk.StringVar()
        self.lname = tk.StringVar()
        self.uname = tk.StringVar()
        self.pwd = tk.StringVar()
        
        # FIXED: Set explicitly to "None" placeholder string token. 
        # This prevents Tkinter from filling both circles with white dots on startup.
        self.gender = tk.StringVar(value="None")

        # ================= NAVIGATION =================
        def go_login():

            login_page = controller.frames["LoginView"]
            login_page.reset_fields()
            controller.show_frame("LoginView")

        # ================= REGISTER FUNCTION =================
        def submit():

            first_name = self.fname.get().strip()
            last_name = self.lname.get().strip()
            username = self.uname.get().strip()
            password = self.pwd.get().strip()
            selected_gender = self.gender.get()

            # FIXED: Validates against "None" to ensure the user has clicked an option
            if (
                first_name == ""
                or last_name == ""
                or username == ""
                or password == ""
                or selected_gender == "None"
            ):

                messagebox.showwarning(
                    "Input Error",
                    "All fields are required, including Gender!"
                )
                return

            try:

                register_user(
                    first_name=first_name,
                    last_name=last_name,
                    email="",
                    gender=selected_gender,
                    country="",    
                    username=username,
                    password=password
                )

                messagebox.showinfo(
                    "Registration Success",
                    "Account created successfully!"
                )

                self.reset_fields()

                login_page = controller.frames["LoginView"]
                login_page.reset_fields()
                controller.show_frame("LoginView")

            except Exception as exc:

                messagebox.showerror(
                    "Registration Failed",
                    str(exc)
                )

        # ================= LEFT IMAGE =================
        img = Image.open(image_path("hnd1.jpg"))

        image_width = min(
            650,
            int(WINDOW_WIDTH * 0.46)
        )

        img = img.resize(
            (image_width, WINDOW_HEIGHT),
            Image.LANCZOS
        )

        self.photo = ImageTk.PhotoImage(img)

        img_label = tk.Label(
            self,
            image=self.photo,
            bg="#020617"
        )
        img_label.place(x=0, y=0)

        # ================= DARK OVERLAY =================
        overlay = tk.Frame(self, bg="#081120")
        overlay.place(x=0, y=0, width=image_width, height=WINDOW_HEIGHT)
        overlay.lower(img_label)

        # ================= LEFT INFO PANEL =================
        left_panel = tk.Frame(self, bg="#101826", width=520, height=220, bd=0)
        left_panel.place(x=70, y=150)

        tk.Frame(left_panel, bg="#38bdf8", width=80, height=4).place(x=40, y=35)
        
        tk.Label(
            left_panel, text="Join Us Today", font=font(40, "bold"), bg="#111827", fg="white"
        ).place(x=38, y=65)

        tk.Label(
            left_panel, 
            text="Register to start using the\nAI-powered handwriting analysis platform", 
            justify="left", font=font(15), bg="#111827", fg="#cbd5e1"
        ).place(x=42, y=145)

        # ================= REGISTER CARD =================
        CARD_WIDTH = 500
        CARD_HEIGHT = 630  
        card_x = min(
             max(image_width + 90, WINDOW_WIDTH - CARD_WIDTH - 120),
             WINDOW_WIDTH - CARD_WIDTH - 60
         )
        card_y = (WINDOW_HEIGHT - CARD_HEIGHT) // 2

        # ================= SHADOW =================
        create_shadow(self, card_x, card_y, CARD_WIDTH, CARD_HEIGHT)

        # ================= MAIN CARD =================
        card = tk.Frame(
           self, bg="#1e293b", width=CARD_WIDTH, height=CARD_HEIGHT, 
           highlightbackground="#38bdf8", highlightthickness=1, bd=0
        )
        card.place(x=card_x, y=card_y)
        card.pack_propagate(False)

        # ================= INNER PANEL =================
        inner_panel = tk.Frame(
            card, bg="#1f2937", width=440, height=580, 
            highlightbackground="#475569", highlightthickness=1, bd=0
        )
        inner_panel.place(relx=0.5, rely=0.5, anchor="center")

        # ================= TOP GLOW STRIP & DOT =================
        glow_strip = tk.Frame(inner_panel, bg="#38bdf8", width=440, height=1)
        glow_strip.place(x=0, y=0)

        glow_dot = tk.Canvas(inner_panel, width=16, height=16, bg="#1f2937", highlightthickness=0)
        glow_dot.place(x=395, y=22)
        glow_dot.create_oval(2, 2, 14, 14, fill="#38bdf8", outline="")
        glow_dot.create_oval(5, 5, 11, 11, fill="#7dd3fc", outline="")

        # ================= CARD TITLE =================
        tk.Label(
            inner_panel, text="Create Account", font=font(26, "bold"), bg="#1b2533", fg="white"
        ).place(x=40, y=35)

        tk.Label(
            inner_panel, text="Register for a new account", font=font(11), bg="#334155", fg="#cbd5e1"
        ).place(x=42, y=85)

        # ================= FIRST NAME =================
        tk.Label(
            inner_panel, text="First Name", font=font(10, "bold"), bg="#1f2937", fg="white"
        ).place(x=40, y=125)

        fname_entry = tk.Entry(
            inner_panel, textvariable=self.fname, font=font(12), bg="#0f172a", fg="#e2e8f0",
            insertbackground="white", relief="flat", width=15, bd=0
        )
        fname_entry.place(x=40, y=150, height=40)
        fname_entry.configure(highlightbackground="#475569", highlightthickness=1)

        # ================= LAST NAME =================
        tk.Label(
            inner_panel, text="Last Name", font=font(10, "bold"), bg="#1f2937", fg="white"
        ).place(x=235, y=125)

        lname_entry = tk.Entry(
            inner_panel, textvariable=self.lname, font=font(12), bg="#111827", fg="white",
            insertbackground="white", relief="flat", width=16, bd=0
        )
        lname_entry.place(x=235, y=150, height=40)
        lname_entry.configure(highlightbackground="#475569", highlightthickness=1)

        # ================= USERNAME =================
        tk.Label(
            inner_panel, text="Username", font=font(10, "bold"), bg="#1f2937", fg="white"
        ).place(x=40, y=210)

        uname_entry = tk.Entry(
            inner_panel, textvariable=self.uname, font=font(12), bg="#0f172a", fg="#e2e8f0",
            insertbackground="white", relief="flat", width=34, bd=0
        )
        uname_entry.place(x=40, y=235, height=40)
        uname_entry.configure(highlightbackground="#475569", highlightthickness=1)

        # ================= PASSWORD =================
        tk.Label(
            inner_panel, text="Password", font=font(10, "bold"), bg="#1f2937", fg="white"
        ).place(x=40, y=295)

        password_entry = tk.Entry(
            inner_panel, textvariable=self.pwd, font=font(12), bg="#111827", fg="white",
            insertbackground="white", relief="flat", width=34, bd=0, show="*"
        )
        password_entry.place(x=40, y=320, height=40)
        password_entry.configure(highlightbackground="#475569", highlightthickness=1)

        # ================= GENDER =================
        tk.Label(
            inner_panel, text="Gender", font=font(10, "bold"), bg="#1f2937", fg="white"
        ).place(x=40, y=380)

        radio_frame = tk.Frame(inner_panel, bg="#1f2937")
        radio_frame.place(x=35, y=405)

        male_radio = tk.Radiobutton(
            radio_frame, text="Male", variable=self.gender, value="Male", bg="#1f2937", fg="white",
            selectcolor="#0f172a", activebackground="#1f2937", activeforeground="white",
            font=font(11), relief="flat", bd=0, highlightthickness=0, padx=8
        )
        male_radio.pack(side="left", padx=10)

        female_radio = tk.Radiobutton(
            radio_frame, text="Female", variable=self.gender, value="Female", bg="#1f2937", fg="white",
            selectcolor="#0f172a", activebackground="#1f2937", activeforeground="white",
            font=font(11), relief="flat", bd=0, highlightthickness=0, padx=8
        )
        female_radio.pack(side="left", padx=10)

        # ================= BUTTON CONTAINER =================
        button_container = tk.Frame(
            inner_panel, bg="#334155", width=360, height=115, highlightbackground="#0f172a", bd=0
        )
        button_container.place(x=40, y=455)

        # ================= REGISTER BUTTON =================
        register_btn = tk.Button(
            button_container, text="REGISTER", font=font(13, "bold"), bd=0, cursor="hand2", 
            relief="flat", fg="white", activeforeground="white", command=submit
        )
        style_button(register_btn, "#0f172a", "#020617")
        register_btn.configure(highlightbackground="#334155", highlightthickness=1, borderwidth=0)
        register_btn.place(x=10, y=15, width=340, height=40)

        # ================= LOGIN BUTTON =================
        login_btn = tk.Button(
            button_container, text="LOGIN", font=font(13, "bold"), bd=0, cursor="hand2", 
            relief="flat", fg="white", activeforeground="white", command=go_login
        )
        style_button(login_btn, "#0f172a", "#020617")
        login_btn.configure(highlightbackground="#334155", highlightthickness=1, borderwidth=0)
        login_btn.place(x=10, y=65, width=340, height=40)


    # ================= RESET FIELDS =================
    def reset_fields(self):

        self.fname.set("")
        self.lname.set("")
        self.uname.set("")
        self.pwd.set("")
        
        # FIXED: Resets variables to "None" so they visually clear back out perfectly
        self.gender.set("None")