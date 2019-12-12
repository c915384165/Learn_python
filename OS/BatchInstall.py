#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
libs = {"numpy", "matplotlib", "pillow", "sklearn", "requests",\
        "jieba", "beautifulsoup4", "wheel", "networkx", "sympy",\
        "pyinstaller", "django", "flask", "werobot", "pyqt5",\
        "pandas", "pyopengl", "pypdf2", "docopt", "pygame"}
try:
    for lib in libs:
        os.system('pip3 install' + ' ' + lib)
    print("Sucessful install!" )
except:
    print("Failed somehow")
