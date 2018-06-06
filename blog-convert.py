#!/usr/bin/env python

import os
from subprocess import Popen
import sys

read_navbar = open('navbar.txt', 'r').read()
read_css = open('main_css.txt', 'r').read()
read_gs = open('main_js.txt','r').read()


inFile = sys.argv[1]
Popen('jupyter nbconvert '+inFile, shell=True).wait()
newFile = os.path.splitext(inFile)[0]+'.html'
body = open(newFile, 'r').read()

if read_navbar not in body:
    body = body.replace("<body>", "<body>\n" + read_navbar)

if read_gs not in body:
    body = body.replace("</body>", read_gs + "\n</body>")

if read_css not in body:
    body = body.replace("<body>", read_css + "\n<body>")


with open('blogpost.html', 'w') as f:
    f.write(body)








