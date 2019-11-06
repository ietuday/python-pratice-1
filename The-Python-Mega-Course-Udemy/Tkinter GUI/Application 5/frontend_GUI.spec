# -*- mode: python -*-

block_cipher = None


a = Analysis(['frontend_GUI.py'],
             pathex=['/Users/tanmaygulati/Work/Python-Udemy/The-Python-Mega-Course-Udemy/Tkinter GUI/Application 5'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='frontend_GUI',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name='frontend_GUI.app',
             icon=None,
             bundle_identifier=None)
