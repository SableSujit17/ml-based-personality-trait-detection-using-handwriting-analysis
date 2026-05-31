# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all
from pathlib import Path
import sys

python_base = Path(sys.base_prefix)

datas = [('assets', 'assets'), ('models', 'models'), ('app/data', 'app/data')]
binaries = []
hiddenimports = [
    'tkinter',
    '_tkinter',
    'tkinter.filedialog',
    'tkinter.messagebox',
    'sklearn',
    'sklearn.utils._cython_blas',
    'sklearn.neighbors._typedefs',
    'sklearn.neighbors._quad_tree',
    'sklearn.tree._utils',
    'joblib',
    'numpy',
    'scipy',
]

tkinter_pkg = python_base / 'Lib' / 'tkinter'
tcl_root = python_base / 'tcl'
dll_dir = python_base / 'DLLs'

if tkinter_pkg.exists():
    datas.append((str(tkinter_pkg), 'tkinter'))

if (tcl_root / 'tcl8.6').exists():
    datas.append((str(tcl_root / 'tcl8.6'), 'tcl'))
    datas.append((str(tcl_root / 'tcl8.6'), '_tcl_data'))

if (tcl_root / 'tk8.6').exists():
    datas.append((str(tcl_root / 'tk8.6'), 'tk'))
    datas.append((str(tcl_root / 'tk8.6'), '_tk_data'))

if (tcl_root / 'tcl8').exists():
    datas.append((str(tcl_root / 'tcl8'), 'tcl8'))

for dll_name in ('_tkinter.pyd', 'tcl86t.dll', 'tk86t.dll'):
    dll_path = dll_dir / dll_name
    if dll_path.exists():
        binaries.append((str(dll_path), '.'))

tmp_ret = collect_all('sklearn')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('joblib')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]


block_cipher = None


a = Analysis(
    ['home.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Handwriting Personality Analyzer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['assets\\icon.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Handwriting Personality Analyzer',
)
