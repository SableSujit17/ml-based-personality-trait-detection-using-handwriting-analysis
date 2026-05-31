import tkinter as tk

from app.utils.paths import ASSETS_DIR
from app.ui.home_view import HomeView
from app.ui.login_view import LoginView
from app.ui.register_view import RegisterView
from app.ui.dashboard_view import DashboardView
from app.ui.about_view import AboutView


class HandwritingApp(tk.Tk):

    def __init__(self, initial_page="HomeView"):
        super().__init__()

        self.title("Handwriting Analysis System")
        self.set_window_icon()

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        self.geometry(
            f"{screen_width}x{screen_height}"
        )

        self.state("zoomed")

        container = tk.Frame(self)

        container.pack(
            fill="both",
            expand=True
        )

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        pages = (
            HomeView,
            LoginView,
            RegisterView,
            DashboardView,
            AboutView
        )

        for Page in pages:

            page_name = Page.__name__

            frame = Page(
                parent=container,
                controller=self
            )

            self.frames[page_name] = frame

            frame.grid(
                row=0,
                column=0,
                sticky="nsew"
            )

        self.show_frame(initial_page)

    def set_window_icon(self):
        icon_file = ASSETS_DIR / "icon.ico"

        if not icon_file.exists():
            return

        try:
            self.iconbitmap(default=str(icon_file))
        except tk.TclError:
            pass

    def show_frame(self, page_name):

        frame = self.frames[page_name]

        if hasattr(frame, "refresh_user"):
            frame.refresh_user()

        frame.tkraise()
