import tkinter as tk

COLORS = {
    "background": "#0f172a",
    "background_alt": "#111827",

    "surface": "#111827",
    "surface_light": "#1f2937",
    "surface_soft": "#273449",

    "border": "#334155",

    "card": "#ffffff",
    "card_soft": "#f8fafc",

    "text": "#111827",
    "text_light": "#f8fafc",

    "muted": "#6b7280",
    "muted_light": "#cbd5e1",

    "white": "#ffffff",

    "primary": "#2563eb",
    "primary_hover": "#1d4ed8",

    "secondary": "#64748b",
    "secondary_hover": "#475569",

    "success": "#16a34a",
    "success_hover": "#15803d",

    "warning": "#f59e0b",
    "warning_hover": "#d97706",

    "danger": "#dc2626",
    "danger_hover": "#b91c1c",

    "input": "#f1f5f9",
}


FONT_FAMILY = "Segoe UI"


# ---------------- Fonts ----------------
def font(size, weight="normal"):

    if weight == "normal":
        return (FONT_FAMILY, size)

    return (FONT_FAMILY, size, weight)


# ---------------- Button Styling ----------------
def style_button(
    button,
    background,
    hover_background=None
):

    normal_background = background

    hover_color = (
        hover_background
        if hover_background
        else background
    )

    button.configure(
        bg=normal_background,
        fg=COLORS["white"],

        activebackground=hover_color,
        activeforeground=COLORS["white"],

        relief="flat",
        bd=0,

        cursor="hand2",

        highlightthickness=0,

        padx=8,
        pady=6,
    )

    def on_enter(event):
        event.widget.configure(bg=hover_color)

    def on_leave(event):
        event.widget.configure(bg=normal_background)

    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)


# ---------------- Entry Styling ----------------
def style_entry(entry):

    entry.configure(
        bg=COLORS["input"],
        fg=COLORS["text"],

        relief="flat",
        bd=0,

        highlightthickness=1,
        highlightbackground="#dbe3ef",
        highlightcolor=COLORS["primary"],

        insertbackground=COLORS["text"],
    )


# ---------------- Card Shadow ----------------
def create_shadow(
    parent,
    x,
    y,
    width,
    height
):

    shadow = tk.Frame(
        parent,
        bg="#0b1220",
        width=width,
        height=height
    )

    shadow.place(
        x=x + 8,
        y=y + 8
    )

    return shadow


# ---------------- Reusable Card ----------------
def create_card(
    parent,
    width,
    height,
    bg=None
):

    frame = tk.Frame(
        parent,
        bg=bg or COLORS["card"],
        width=width,
        height=height,
        highlightbackground="#e2e8f0",
        highlightthickness=1,
    )

    return frame