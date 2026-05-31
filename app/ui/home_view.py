import tkinter as tk
import random
from PIL import ImageTk, Image

from app.utils.paths import image_path
from app.ui.theme import (
    COLORS,
    font,
    style_button
)


class HomeView(tk.Frame):

    def __init__(self, parent, controller):

        super().__init__(parent)

        self.controller = controller

        # ================= SCREEN =================
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        WINDOW_WIDTH = screen_width
        WINDOW_HEIGHT = screen_height

        self.configure(bg=COLORS["background"])

        # ================= NAVIGATION =================
        def open_login():

            login_page = controller.frames["LoginView"]

            login_page.reset_fields()

            controller.show_frame("LoginView")

        def open_register():

            register_page = controller.frames["RegisterView"]

            register_page.reset_fields()

            controller.show_frame("RegisterView")

        # ================= CANVAS =================
        canvas = tk.Canvas(
            self,
            width=WINDOW_WIDTH,
            height=WINDOW_HEIGHT,
            highlightthickness=0
        )

        canvas.pack(fill="both", expand=True)

        # ================= BACKGROUND =================
        bg_img = Image.open(image_path("hnd1.jpg"))

        bg_img = bg_img.resize(
            (WINDOW_WIDTH, WINDOW_HEIGHT)
        )

        self.bg_photo = ImageTk.PhotoImage(bg_img)

        canvas.create_image(
            0,
            0,
            image=self.bg_photo,
            anchor="nw"
        )

        # ================= DARK OVERLAY =================
        canvas.create_rectangle(
            0,
            0,
            WINDOW_WIDTH,
            WINDOW_HEIGHT,
            fill="#020617",
            stipple="gray50",
            outline=""
        )

        # ================= ANIMATED NODES =================
        nodes = []

        node_count = 18

        for _ in range(node_count):

            x = random.randint(0, WINDOW_WIDTH)
            y = random.randint(0, WINDOW_HEIGHT)

            node = canvas.create_oval(
                x,
                y,
                x + 6,
                y + 6,
                fill="#38bdf8",
                outline=""
            )

            nodes.append({
                "id": node,
                "dx": random.uniform(-0.7, 0.7),
                "dy": random.uniform(-0.7, 0.7)
            })

        lines = []

        def draw_lines():

            for line in lines:
                canvas.delete(line)

            lines.clear()

            for i in range(len(nodes)):

                for j in range(i + 1, len(nodes)):

                    x1, y1, x2, y2 = canvas.coords(nodes[i]["id"])
                    x3, y3, x4, y4 = canvas.coords(nodes[j]["id"])

                    x1 += 3
                    y1 += 3

                    x3 += 3
                    y3 += 3

                    distance = (
                        ((x1 - x3) ** 2 + (y1 - y3) ** 2)
                    ) ** 0.5

                    if distance < 170:

                        line = canvas.create_line(
                            x1,
                            y1,
                            x3,
                            y3,
                            fill="#1e3a8a",
                            width=1
                        )

                        lines.append(line)

        def animate():

            for node in nodes:

                canvas.move(
                    node["id"],
                    node["dx"],
                    node["dy"]
                )

                x1, y1, x2, y2 = canvas.coords(node["id"])

                if x1 < 0 or x2 > WINDOW_WIDTH:
                    node["dx"] *= -1

                if y1 < 0 or y2 > WINDOW_HEIGHT:
                    node["dy"] *= -1

            draw_lines()

            self.after(45, animate)

        animate()

        # ================= HERO TITLE =================
        canvas.create_text(
            120,
            115,
            text="AI-Based Handwriting",
            font=font(40, "bold"),
            fill="white",
            anchor="w"
        )

        canvas.create_text(
            120,
            170,
            text="Personality Analysis System",
            font=font(30, "bold"),
            fill="#93c5fd",
            anchor="w"
        )

        canvas.create_text(
            120,
            240,
            text="AI-powered personality prediction using handwriting analysis",
            font=font(15),
            fill=COLORS["muted_light"],
            anchor="w"
        )

        # ================= FEATURE HIGHLIGHTS =================
        features = [
            "- Machine Learning",
            "- Image Processing",
            "- Personality Detection"
        ]

        feature_y = 320

        for feature in features:

            canvas.create_text(
                125,
                feature_y,
                text=feature,
                font=font(12),
                fill="#dbeafe",
                anchor="w"
            )

            feature_y += 38

        # ================= ACTION CARD =================
        CARD_WIDTH = 500
        CARD_HEIGHT = 420

        card_x = WINDOW_WIDTH - 650
        card_y = (WINDOW_HEIGHT - CARD_HEIGHT) // 2

        # ================= MAIN CARD =================
        card = tk.Frame(
            self,
            bg="#1e293b",
            width=CARD_WIDTH,
            height=CARD_HEIGHT,
            highlightbackground="#38bdf8",
            highlightthickness=1
        )

        card.place(
            x=card_x,
            y=card_y
        )

        card.pack_propagate(False)

        # ================= INNER PANEL =================
        inner_panel = tk.Frame(
            card,
            bg="#334155",
            width=460,
            height=380
        )

        inner_panel.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # ================= TOP GLOW =================
        glow_dot = tk.Canvas(
            inner_panel,
            width=14,
            height=14,
            bg="#334155",
            highlightthickness=0
        )

        glow_dot.place(x=25, y=22)

        glow_dot.create_oval(
            2,
            2,
            10,
            10,
            fill="#38bdf8",
            outline=""
        )

        # ================= ACCENT LINE =================
        tk.Frame(
            inner_panel,
            bg="#38bdf8",
            width=55,
            height=3
        ).place(x=52, y=28)

        # ================= TITLE =================
        tk.Label(
            inner_panel,
            text="Get Started",
            font=font(32, "bold"),
            bg="#334155",
            fg="white"
        ).place(x=48, y=85)

        # ================= SUBTITLE =================
        tk.Label(
            inner_panel,
            text="Access the AI-powered handwriting\nanalysis platform",
            justify="left",
            font=font(14),
            bg="#334155",
            fg="#cbd5e1"
        ).place(x=48, y=155)

        # ================= BUTTON COLORS =================
        BUTTON_BG = "#0f172a"
        BUTTON_HOVER = "#020617"

        # ================= LOGIN BUTTON =================
        login_btn = tk.Button(
            inner_panel,
            text="LOGIN",
            font=font(13, "bold"),
            width=28,
            height=1,
            bd=0,
            cursor="hand2",
            relief="flat",
            activeforeground="white",
            activebackground=BUTTON_HOVER,
            fg="white",
            command=open_login
        )

        style_button(
            login_btn,
            BUTTON_BG,
            BUTTON_HOVER
        )

        login_btn.configure(
            highlightbackground="#64748b",
            highlightthickness=1
        )

        login_btn.place(
            x=50,
            y=265,
            height=46
        )

        # ================= REGISTER BUTTON =================
        register_btn = tk.Button(
            inner_panel,
            text="REGISTER",
            font=font(13, "bold"),
            width=28,
            height=1,
            bd=0,
            cursor="hand2",
            relief="flat",
            activeforeground="white",
            activebackground=BUTTON_HOVER,
            fg="white",
            command=open_register
        )

        style_button(
            register_btn,
            BUTTON_BG,
            BUTTON_HOVER
        )

        register_btn.configure(
            highlightbackground="#64748b",
            highlightthickness=1
        )

        register_btn.place(
            x=50,
            y=325,
            height=46
        )

        # ================= DECORATIVE DOT =================
        bottom_dot = tk.Canvas(
            inner_panel,
            width=16,
            height=16,
            bg="#334155",
            highlightthickness=0
        )

        bottom_dot.place(x=58, y=345)

        bottom_dot.create_oval(
            4,
            4,
            10,
            10,
            fill="#0ea5e9",
            outline=""
        )

        # ================= SIDE DOT =================
        side_dot = tk.Canvas(
            inner_panel,
            width=16,
            height=16,
            bg="#334155",
            highlightthickness=0
        )

        side_dot.place(x=420, y=320)

        side_dot.create_oval(
            4,
            4,
            10,
            10,
            fill="#0ea5e9",
            outline=""
        )

        # ================= FOOTER =================
        canvas.create_text(
            WINDOW_WIDTH / 2,
            WINDOW_HEIGHT - 35,
            text="Final Year Engineering Project | AI-Based Handwriting Analysis",
            font=font(10),
            fill="#cbd5e1"
        )
