# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['finance.py'],
             pathex=['/Users/a12345/Music/GithubProjects/py2app'],
             binaries=[],
             datas=[('README.md', '.'), ('datasets/*', 'datasets')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
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
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='news',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='finance.png')
app = BUNDLE(exe,
             name='news.app',
             icon='finance.png',
             bundle_identifier=None)
