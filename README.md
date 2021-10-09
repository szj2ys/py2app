
pyinstaller -i finance.png -Fw finance.py

pyinstaller -i finance.png -Fw finance.spec


datas=[
                 ( '*.py', '.' ),
                 ( 'datasets/*', 'datasets' ),
             ],


