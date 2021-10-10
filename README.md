
pyinstaller --noconfirm \
--name news \
--add-data="README.md:." \
--add-data="datasets/*:datasets" \
--hidden-import=sqlstar.backends.mysql \
--icon finance.png \
-Fw finance.py




## REFERENCES

- [Tkinter](https://blog.csdn.net/nire_yeyu/category_9877892.html)

- [icon8](http://www.ico8.net/index.php?action=make)

