import tkinter as tk
from tkinter import *

from app.ui.theme import (
    COLORS,
    font,
    style_button,
    style_entry,
)


# ---------------- Primary Button ----------------
def create_primary_button(
    parent,
    text,
    command,
    width=20
):

    btn = Button(
        parent,
        text=text,
        font=font(12, "bold"),
        width=width,
        command=command
    )

    style_button(
        btn,
        COLORS["primary"],
        COLORS["primary_hover"]
    )

    return btn


# ---------------- Secondary Button ----------------
def create_secondary_button(
    parent,
    text,
    command,
    width=20
):

    btn = Button(
        parent,
        text=text,
        font=font(11),
        width=width,
        command=command
    )

    style_button(
        btn,
        COLORS["secondary"],
        COLORS["secondary_hover"]
    )

    return btn


# ---------------- Danger Button ----------------
def create_danger_button(
    parent,
    text,
    command,
    width=20
):

    btn = Button(
        parent,
        text=text,
        font=font(11),
        width=width,
        command=command
    )

    style_button(
        btn,
        COLORS["danger"],
        COLORS["danger_hover"]
    )

    return btn


# ---------------- Input Field ----------------
def create_input_field(
    parent,
    label_text,
    variable,
    x,
    y,
    width=34,
    show=None
):

    Label(
        parent,
        text=label_text,
        font=font(11, "bold"),
        bg=COLORS["card"],
        fg="#374151"
    ).place(x=x, y=y)

    entry = Entry(
        parent,
        textvariable=variable,
        font=font(12),
        width=width,
        show=show
    )

    style_entry(entry)

    entry.place(
        x=x,
        y=y + 30,
        height=34
    )

    return entry


# ---------------- Card Title ----------------
def create_card_title(
    parent,
    title,
    subtitle=None
):

    Label(
        parent,
        text=title,
        font=font(20, "bold"),
        bg=COLORS["card"],
        fg=COLORS["text"]
    ).place(x=40, y=40)

    if subtitle:

        Label(
            parent,
            text=subtitle,
            font=font(11),
            bg=COLORS["card"],
            fg=COLORS["muted"]
        ).place(x=40, y=80)


# ---------------- Sidebar Header ----------------
def create_sidebar_header(
    parent,
    title,
    subtitle
):

    Label(
        parent,
        text=title,
        bg=COLORS["surface"],
        fg="white",
        font=font(16, "bold")
    ).pack(pady=(28, 8))

    Label(
        parent,
        text=subtitle,
        bg=COLORS["surface"],
        fg=COLORS["muted_light"],
        font=font(10)
    ).pack(pady=(0, 22))


# ---------------- Card Container ----------------
def create_card(
    parent,
    x,
    y,
    width,
    height,
    bg_color=None
):

    if bg_color is None:
        bg_color = COLORS["card"]

    card = Frame(
        parent,
        bg=bg_color,
        width=width,
        height=height,
        highlightbackground="#e2e8f0",
        highlightthickness=1
    )

    card.place(x=x, y=y)

    return card