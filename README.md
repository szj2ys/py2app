
pyinstaller -i finance.png -Fw finance.py

pyinstaller -i finance.png -Fw finance.spec


datas=[
                 ( '*.py', '.' ),
                 ( 'datasets/*', 'datasets' ),
             ],

## REFERENCES

- [Tkinter](https://blog.csdn.net/nire_yeyu/category_9877892.html)
