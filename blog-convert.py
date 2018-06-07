#!/usr/bin/env python

import os
from subprocess import Popen
import sys

inFile = sys.argv[1]
Popen('jupyter nbconvert '+inFile +' --template basic', shell=True).wait()
newFile = os.path.splitext(inFile)[0]+'.html'

template = open('custom/template.html', 'r').read()

read_navbar = open('custom/navbar.txt', 'r').read()
read_css = open('custom/main_css.txt', 'r').read()
read_gs = open('custom/main_js.txt','r').read()
read_body = open(newFile, 'r').read()
read_mathjax = open('custom/mathjax.txt', 'r').read()

template = template.replace("[--navbar--]", "\n" + read_navbar + "\n")
template = template.replace("[--js--]", "\n" + read_gs + "\n")
template = template.replace("[--css--]", "\n" + read_css + "\n")
template = template.replace("[--body--]", "\n" + read_body + "\n")
template = template.replace("[--mathjax--]", "\n" + read_mathjax + "\n")

with open(newFile, 'w') as f:
    f.write(template)


