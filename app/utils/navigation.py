from app.main import main


SCREEN_MODULES = {
    "home.py": "HomeView",
    "login.py": "LoginView",
    "Registration.py": "RegisterView",
    "detect1.py": "DashboardView",
    "about_us1.py": "AboutView",
}


def open_script(script_name, *args):
    page_name = SCREEN_MODULES.get(script_name)

    if page_name is None:
        raise ValueError(f"Unknown screen: {script_name}")

    main(page_name)
