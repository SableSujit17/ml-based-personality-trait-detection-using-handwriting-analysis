import tkinter as tk
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk

from app.data.database import authenticate_user
from app.utils.paths import image_path
from app.ui.theme import (
    create_shadow,
    font,
    style_button
)


class LoginView(tk.Frame):

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
        self.uname = tk.StringVar()
        self.pwd = tk.StringVar()

        # ================= NAVIGATION =================
        def go_home():

            home_page = controller.frames["HomeView"]

            if hasattr(home_page, "reset_fields"):
                home_page.reset_fields()

            controller.show_frame("HomeView")

        # ================= LOGIN FUNCTION =================
        def login_user():

            username = self.uname.get().strip()
            password = self.pwd.get().strip()

            if username == "" or password == "":

                messagebox.showwarning(
                    "Input Error",
                    "All fields are required"
                )

                return

            try:

                result = authenticate_user(
                    username,
                    password
                )

            except sqlite3.Error as exc:

                messagebox.showerror(
                    "Database Error",
                    f"Could not check login details.\n{exc}"
                )

                return

            if result:

                dashboard = controller.frames["DashboardView"]

                dashboard.set_user(username)

                dashboard.reset_page()

                controller.show_frame("DashboardView")

                self.reset_fields()

            else:

                messagebox.showerror(
                    "Login Failed",
                    "Invalid Username or Password"
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

        img_label.place(
            x=0,
            y=0
        )

        # ================= DARK OVERLAY =================
        overlay = tk.Frame(
            self,
            bg="#081120"
        )

        overlay.place(
            x=0,
            y=0,
            width=image_width,
            height=WINDOW_HEIGHT
        )

        overlay.lower(img_label)

        # ================= LEFT INFO PANEL =================
        left_panel = tk.Frame(
            self,
            bg="#101826",
            width=520,
            height=220,
            bd=0
        )

        left_panel.place(
            x=70,
            y=150
        )

        # ================= ACCENT LINE =================
        tk.Frame(
            left_panel,
            bg="#38bdf8",
            width=80,
            height=4
        ).place(
            x=40,
            y=35
        )

        # ================= TITLE =================
        tk.Label(
            left_panel,
            text="Welcome Back",
            font=font(40, "bold"),
            bg="#111827",
            fg="white"
        ).place(
            x=38,
            y=65
        )

        # ================= SUBTITLE =================
        tk.Label(
            left_panel,
            text="Login to continue using the\nAI-powered handwriting analysis platform",
            justify="left",
            font=font(15),
            bg="#111827",
            fg="#cbd5e1"
        ).place(
            x=42,
            y=145
        )


    

        # ================= LOGIN CARD =================
        CARD_WIDTH = 500
        CARD_HEIGHT = 570
        card_x = min(
             max(
                 image_width + 90,
                WINDOW_WIDTH - CARD_WIDTH - 120
            ),
           WINDOW_WIDTH - CARD_WIDTH - 60
        )
        card_y = (
           WINDOW_HEIGHT - CARD_HEIGHT
        ) // 2

        # ================= AMBIENT GLOW =================
        
        # ================= SHADOW =================
        create_shadow(
            self,
            card_x,
            card_y,
            CARD_WIDTH,
            CARD_HEIGHT
        )

        # ================= MAIN CARD =================
        card = tk.Frame(
           self,
           bg="#1e293b",
           width=CARD_WIDTH,
           height=CARD_HEIGHT,
           highlightbackground="#38bdf8",
           highlightthickness=1,
           bd=0
        )
        card.place(
           x=card_x,
           y=card_y
        )
        card.pack_propagate(False)

    

        # ================= INNER PANEL =================
        inner_panel = tk.Frame(
            card,
            bg="#1f2937",
            width=440,
            height=510,
            highlightbackground="#475569",
            highlightthickness=1,
            bd=0
        )

        inner_panel.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # ================= TOP GLOW STRIP =================
        glow_strip = tk.Frame(
            inner_panel,
            bg="#38bdf8",
            width=440,
            height=1
        )

        glow_strip.place(
            x=0,
            y=0
        )

        # ================= GLOW DOT =================
        glow_dot = tk.Canvas(
            inner_panel,
            width=16,
            height=16,
            bg="#1f2937",
            highlightthickness=0
        )

        glow_dot.place(
            x=395,
            y=22
        )

        glow_dot.create_oval(
            2,
            2,
            14,
            14,
            fill="#38bdf8",
            outline=""
        )

        glow_dot.create_oval(
            5,
            5,
            11,
            11,
            fill="#7dd3fc",
            outline=""
        )

        # ================= ACCENT LINE =================


        # ================= CARD TITLE =================
        tk.Label(
            inner_panel,
            text="Handwriting Analysis",
            font=font(28, "bold"),
            bg="#1b2533",
            fg="white"
        ).place(
            x=42,
            y=60
        )

        tk.Label(
            inner_panel,
            text="Login to your account",
            font=font(12),
            bg="#334155",
            fg="#cbd5e1"
        ).place(
            x=44,
            y=110
        )

        # ================= USERNAME =================
        tk.Label(
            inner_panel,
            text="Username",
            font=font(11, "bold"),
            bg="#1f2937",
            fg="white"
        ).place(
            x=40,
            y=180
        )

        username_entry = tk.Entry(
            inner_panel,
            textvariable=self.uname,
            font=font(12),
            bg="#0f172a",
            fg="#e2e8f0",
            insertbackground="white",
            relief="flat",
            width=34,
            bd=0
        )

        username_entry.place(
            x=40,
            y=205,
            height=44
        )

        username_entry.configure(
            highlightbackground="#475569",
            highlightthickness=1
        )

        # ================= PASSWORD =================
        tk.Label(
            inner_panel,
            text="Password",
            font=font(11, "bold"),
            bg="#1f2937",
            fg="white"
        ).place(
            x=40,
            y=275
        )

        password_entry = tk.Entry(
            inner_panel,
            textvariable=self.pwd,
            font=font(12),
            bg="#111827",
            fg="white",
            insertbackground="white",
            relief="flat",
            width=34,
            bd=0,
            show="*"
        )

        password_entry.place(
            x=40,
            y=310,
            height=44
        )

        password_entry.configure(
            highlightbackground="#475569",
            highlightthickness=1
        )

        # ================= BUTTON CONTAINER =================
        button_container = tk.Frame(
            inner_panel,
            bg="#334155",
            width=360,
            height=135,
            highlightbackground="#0f172a",
            bd=0
        )

        button_container.place(
            x=40,
            y=365
        )

        # ================= LOGIN BUTTON =================
        login_btn = tk.Button(
            button_container,
            text="LOGIN",
            font=font(13, "bold"),
            bd=0,
            cursor="hand2",
            relief="flat",
            fg="white",
            activeforeground="white",
            command=login_user
        )

        style_button(
            login_btn,
            "#0f172a",
            "#020617"
        )

        login_btn.configure(
            highlightbackground="#334155",
            highlightthickness=1,
            borderwidth=0
        )

        login_btn.place(
            x=10,
            y=15,
            width=340,
            height=50
        )

        # ================= HOME BUTTON =================
        home_btn = tk.Button(
            button_container,
            text="HOME",
            font=font(13, "bold"),
            bd=0,
            cursor="hand2",
            relief="flat",
            fg="white",
            activeforeground="white",
            command=go_home
        )

        style_button(
            home_btn,
            "#0f172a",
            "#020617"
        )

        home_btn.configure(
            highlightbackground="#334155",
            highlightthickness=1,
            borderwidth=0
        )

        home_btn.place(
            x=10,
            y=75,
            width=340,
            height=50
        )

    # ================= RESET FIELDS =================
    def reset_fields(self):

        self.uname.set("")
        self.pwd.set("")
