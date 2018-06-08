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

* Replace the jupyter-blog.ipynb with your own Jupyter Notebook file. For example, yourfile.ipynb
* Modify the `.txt` files in the `custom` folder to your own. (This step is very important. You can refer to `template.html`).
* Open terminal and cd to this directory and run

```
python blog-convert.py yourfile.ipynb
```

You should now have new a file named your.html, modified to match the theme of your static website.

## More
Please visit my website [https://elanding.xyz/blog/2018/jupyter-blog.html](https://elanding.xyz/blog/2018/jupyter-blog.html) for more detailed instructions.
