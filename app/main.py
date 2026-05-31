import os
import sys
from pathlib import Path


def configure_tcl_tk():
    if not hasattr(sys, "_MEIPASS"):
        return

    bundle_dir = Path(sys._MEIPASS)

    if str(bundle_dir) not in sys.path:
        sys.path.insert(0, str(bundle_dir))

    tcl_dir = bundle_dir / "_tcl_data"
    tk_dir = bundle_dir / "_tk_data"

    if not tcl_dir.exists():
        tcl_dir = bundle_dir / "tcl"

    if not tk_dir.exists():
        tk_dir = bundle_dir / "tk"

    if tcl_dir.exists():
        os.environ.setdefault("TCL_LIBRARY", str(tcl_dir))

    if tk_dir.exists():
        os.environ.setdefault("TK_LIBRARY", str(tk_dir))


configure_tcl_tk()

from app.app_controller import HandwritingApp


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def main(initial_page="HomeView"):
    app = HandwritingApp(initial_page=initial_page)
    app.mainloop()


if __name__ == "__main__":
    main()
