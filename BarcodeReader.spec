# -*- mode: python -*-
a = Analysis([os.path.join(HOMEPATH,'support\\_mountzlib.py'), os.path.join(HOMEPATH,'support\\useUnicode.py'), 'BarcodeReader.py'],
             pathex=['E:\\Workspace\\GitHub\\BarcodeReader'])
pyz = PYZ(a.pure)
exe = EXE( pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'BarcodeReader.exe'),
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='icon.ico')
app = BUNDLE(exe,
             name=os.path.join('dist', 'BarcodeReader.exe.app'))
