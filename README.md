```shell
pyinstaller --noconfirm \
--name news \
--add-data="README.md:." \
--add-data="datasets/*:datasets" \
--hidden-import=sqlstar.backends.mysql \
--icon finance.ico \
-Fw finance.py
```


## Windows
```shell
pyinstaller --noconfirm --name news --add-data="README.md;." --add-data="datasets/*;datasets" --hidden-import=sqlstar.backends.mysql --icon finance.ico -Fw finance.py
```

excludes = [
    # https://github.com/pyinstaller/pyinstaller/wiki/Recipe-remove-tkinter-tcl
    "FixTk",
    "tcl",
    "tk",
    "_tkinter",
    "tkinter",
    "Tkinter",
    # Misc
    "PIL",
    "ipdb",
    "lib2to3",
    "numpy",
    "pydev",
    "scipy",
    "yappi",
]


## REFERENCES

- [Tkinter](https://blog.csdn.net/nire_yeyu/category_9877892.html)

- [icon8](http://www.ico8.net/index.php?action=make)

