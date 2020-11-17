# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all

block_cipher = None

pf_datas, pf_binaries, pf_hiddenimports = collect_all("pyfiglet")

a = Analysis(['mkhost.py'],
             pathex=['/home/mansur/data/python/local-http'],
             binaries=pf_binaries+[],
             datas=pf_datas+[('settings.ini', '.'), ('templates/vhost-ssl.conf', 'templates'), ('templates/vhost-http.conf', 'templates')],
             hiddenimports=pf_hiddenimports+['os'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='mkhost',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='mkhost')
