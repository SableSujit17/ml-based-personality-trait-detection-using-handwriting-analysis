import tkinter as tk
from tkinter import Frame, Label, Button, Canvas, filedialog, messagebox
from PIL import Image, ImageTk
import logging

from app.ui.theme import (
    COLORS,
    font,
    style_button,
)

from app.utils.paths import image_path

logger = logging.getLogger(__name__)


class AboutView(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        self.configure(bg=COLORS["background"])

        # ================= BACKGROUND =================
        try:
            bg_image = Image.open(image_path("neural2.jpeg"))
            bg_image = bg_image.resize((screen_width, screen_height))
            self.bg_photo = ImageTk.PhotoImage(bg_image)

            bg_label = tk.Label(self, image=self.bg_photo, bd=0)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            bg_label.lower()
        except Exception:
            # Fallback smoothly if background image isn't found
            pass

        # ================= SIDEBAR =================
        sidebar = tk.Frame(
            self,
            bg="#020817",
            width=230
        )
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        tk.Label(
            sidebar,
            text="Handwriting\nAnalysis",
            font=font(20, "bold"),
            bg="#020817",
            fg="white",
            justify="center"
        ).pack(pady=(45, 10))

        tk.Label(
            sidebar,
            text="AI Personality Detection",
            font=font(10),
            bg="#020817",
            fg="#94a3b8"
        ).pack()

        # ================= NAVIGATION =================
        dashboard_btn = tk.Button(
            sidebar,
            text="Dashboard",
            font=font(11, "bold"),
            command=lambda: controller.show_frame("DashboardView"),
            width=18,
            bd=0,
            cursor="hand2"
        )
        style_button(
            dashboard_btn,
            COLORS["primary"],
            COLORS["primary_hover"]
        )
        dashboard_btn.pack(pady=(60, 12), ipady=4)

        logout_btn = tk.Button(
            sidebar,
            text="Logout",
            font=font(11, "bold"),
            command=lambda: controller.show_frame("LoginView"),
            width=18,
            bd=0,
            cursor="hand2"
        )
        style_button(
            logout_btn,
            COLORS["danger"],
            COLORS["danger_hover"]
        )
        logout_btn.pack(pady=4, ipady=4)

        # ================= HEADER =================
        tk.Label(
            self,
            text="About Our Project",
            font=font(28, "bold"),
            bg=COLORS["background"],
            fg="white"
        ).place(x=280, y=35)

        # ================= DESCRIPTION CARD =================
        desc_frame = tk.Frame(
            self,
            bg="#0f172a",
            highlightbackground="#334155",
            highlightthickness=1
        )
        desc_frame.place(x=280, y=100, width=980, height=160)

        description = (
            "This AI-based handwriting analysis system predicts personality traits using "
            "Machine Learning and image processing techniques.\n\n"
            "Users can upload handwriting samples and receive AI-generated personality predictions instantly.\n\n"
            "The project combines Deep Learning, Computer Vision, and behavioral pattern recognition "
            "into one seamless desktop application."
        )

        tk.Label(
            desc_frame,
            text=description,
            wraplength=920,
            justify="left",
            font=font(12),
            bg="#0f172a",
            fg="#cbd5e1",
            padx=25,
            pady=20
        ).pack(anchor="w")

        # ================= TEAM TITLE =================
        tk.Label(
            self,
            text="Project Team Members",
            font=font(22, "bold"),
            bg=COLORS["background"],
            fg="white"
        ).place(x=280, y=290)

        # ================= DYNAMIC TEAM MEMBERS GRID =================
        # Storing all 4 teammates data cleanly to run loops through positions flawlessly
        team_members = [
            {"image": "ankush.jfif", "name": "Ankush Lakade", "role": "Lead Developer"},
            {"image": "purva.jpeg", "name": "Purva Kale", "role": "ML Engineer"},
            {"image": "sujit.jpeg", "name": "Sujit Sable", "role": "UI Designer"},
            {"image": "img1.png", "name": "Rishikesh Jadhao", "role": "QA Engineer"}
        ]

        # Grid system parameters for pixel-perfect structural layouts
        start_x = 280
        start_y = 350
        card_width = 230
        gap_x = 20  # Explicit spacing separation boundary gap pixels between columns

        for index, member in enumerate(team_members):
            # Compute grid placement dynamically side-by-side
            calculated_x = start_x + index * (card_width + gap_x)
            
            self.create_member(
                x=calculated_x,
                y=start_y,
                image_name=member["image"],
                name=member["name"],
                role=member["role"]
            )

    # ================= MEMBER CARD BUILDER =================
    def create_member(self, x, y, image_name, name, role):
        card = tk.Frame(
            self,
            bg="#0f172a",
            width=230,
            height=330,
            highlightbackground="#334155",
            highlightthickness=1
        )
        card.place(x=x, y=y)
        card.pack_propagate(False) # Forces layout managers to respect manual heights

        # Safe Profile Graphic Vector Generator Block
        try:
            img = Image.open(image_path(image_name))
            img = img.resize((140, 140), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)

            img_label = tk.Label(card, image=photo, bg="#0f172a")
            img_label.image = photo
            img_label.pack(pady=(20, 10))
        except Exception:
            # Fallback Native Initials Canvas Module System if local disk graphic resource path misses
            fallback_box = tk.Canvas(card, width=140, height=140, bg="#0f172a", highlightthickness=0)
            fallback_box.pack(pady=(20, 10))
            
            # Smooth badge drawing logic using initials extracted dynamically
            initials = "".join([part[0] for part in name.split() if part])[:2].upper()
            fallback_box.create_oval(10, 10, 130, 130, fill="#1e293b", outline="#38bdf8", width=2)
            fallback_box.create_text(70, 70, text=initials, fill="white", font=font(22, "bold"))

        tk.Label(
            card,
            text=name,
            font=font(15, "bold"),
            bg="#0f172a",
            fg="white"
        ).pack()

        tk.Label(
            card,
            text=role,
            font=font(11),
            bg="#0f172a",
            fg="#9ca3af"
        ).pack(pady=2)

        tk.Label(
            card,
            text="AI | ML | Desktop App",
            font=font(9),
            bg="#0f172a",
            fg="#38bdf8"
        ).pack(pady=(15, 0))
