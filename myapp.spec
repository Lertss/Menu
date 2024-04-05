# Файл: myapp.spec

a = Analysis(['main.py'],
             pathex=['C:\\Users\\sergz\\AppData\\Local\\Temp\\ONEFIL~1'],
             hookspath=['C:\\Users\\sergz\\AppData\\Local\\Temp\\ONEFIL~1\\PyInstaller\\hooks'],
             datas=[
                 ('ui/qt_base_ui', '.'),
                 ('intro', '.')
             ])

pyz = PYZ(a.pure)
exe = EXE(pyz, a.scripts, a.binaries, a.zipfiles, a.datas, name='myapp')