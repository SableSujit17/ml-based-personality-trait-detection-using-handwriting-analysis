# Installer Notes

The project includes a PyInstaller spec for creating a Windows executable.

## Build

```powershell
.\.venv\Scripts\python.exe -m PyInstaller --noconfirm --workpath build_final_app --distpath FINAL_DESKTOP_APP "Handwriting Personality Analyzer.spec"
```

## Output

PyInstaller creates:

```text
FINAL_DESKTOP_APP/
  Handwriting Personality Analyzer/
    Handwriting Personality Analyzer.exe
```

## Optional Setup Installer

After the PyInstaller build succeeds, you can wrap `FINAL_DESKTOP_APP/Handwriting Personality Analyzer` with a Windows installer tool such as Inno Setup.

Recommended installer settings:

- Application name: `Handwriting Personality Analyzer`
- Main executable: `Handwriting Personality Analyzer.exe`
- Install mode: per-user
- Shortcut: desktop and Start Menu
