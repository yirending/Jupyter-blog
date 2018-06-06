# Jupyter-blog
Converting Jupyter notebook files to blog friendly html

To use simply clone this repository to your local machine first. Then follow the following steps:

* Replace the NHANES_analysis.ipynb with your own Jupyter Notebook file, yourfile.ipynb
* Remove NAHNES_analysis.html and blogpost.html (These are my outputs.)
* Modify navbar.txt to your own html code for navigation bar
* Modify main_css.txt to your own custom css styles
* Modify main_js to your own custom js code
* Open terminal and cd to this directory and run

```
python blog-convert.py yourfile.ipynb
```

You should now have a file named blogpost.html, modified to match the theme of your static website.
