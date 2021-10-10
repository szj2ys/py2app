
pyinstaller --noconfirm \
--name news \
--add-data="README.md:." \
--add-data="datasets/*:datasets" \
--hidden-import=pandas \
--icon finance.png \
-Fw finance.py


pyinstaller --noconfirm \
--name news \
--add-data="README.md:." \
--add-data="datasets/*:datasets" \
--icon finance.png \
-Fw finance.py


## REFERENCES

- [Tkinter](https://blog.csdn.net/nire_yeyu/category_9877892.html)
