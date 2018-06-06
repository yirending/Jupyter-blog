# Jupyter-blog
Converting Jupyter notebook files to blog friendly html

## Who is this for?

If you already have a static website with a simple navigation bar, and some custom CSS and Javascript files, and you would like to convert a Jupyter Notebook file into a blog-friendly html file.


## Prerequirsites

First make sure you have latest Python installed in your machine. Next install nbconvert by typing

```
pip install nbconvert
```
in your command line.

## How to use
To use simply clone this to your local repository. Then follow the following steps:

* Replace the NHANES_analysis.ipynb with your own Jupyter Notebook file, say, yourfile.ipynb
* Remove blogpost.html (This is my output.)
* Modify navbar.txt to your own code for adding custom navigation bar on top of your web page
* Modify main_css.txt to match your website's theme
* Modify main_js to match your website's theme
* Open terminal and cd to this directory and run

```
python blog-convert.py yourfile.ipynb
```

You should now have a file named blogpost.html, modified to match the theme of your static website.

## More
For more customization, you can modify the Python script blog-convert.py.
