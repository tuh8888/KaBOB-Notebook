from ipywidgets import interactive
import ipywidgets as widgets
from IPython.display import Image, Markdown
import os


md_dir = "markdown/Ontologies/"
md_files = [f.split('.')[0] for f in os.listdir(md_dir) if f.endswith('.md')]

img_dir = 'images/Rules/'
img_files = [f.split('.')[0] for f in os.listdir(img_dir) if f.endswith('.png')]
   
def display_markdown(md_file):
    display(Markdown(md_dir + md_file + ".md"))

def display_image(img_file, scale):
    display(Image(img_dir + img_file + '.png', 
    	height=512*scale, 
    	width=512*scale, 
    	unconfined=True))

    

ontology_viewer = interactive(display_markdown, md_file=md_files)
rule_viewer = interactive(display_image, img_file=img_files, scale=widgets.FloatSlider(min=0.5, max=1.5, step=0.1, value=1))