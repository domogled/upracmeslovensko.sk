#!/usr/bin/env python3




import webbrowser as browser

from utils import *


for file in TPL.iterdir():
    print(file)
    url = f'http://localhost/upracmeslovensko.sk/src/html/templates/{file.name}'
    # print(url)
    browser.open_new_tab(url)