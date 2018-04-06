from ipywidgets import interactive
from IPython.display import Image, Markdown, display
import os

def display_image(img_file, scale):
	img = Image(img_dir + img_file + '.png', height=512*scale, width=512*scale, unconfined=True)
	display(img)

def display_markdown(md_file):	
	display(Markdown(md_dir + md_file + ".md"))


def markdown_viewer(md_files):
	if type(md_files) is str:
		md_files = [f.split('.')[0] for f in os.listdir(md_files) if f.endswith('.md')]
	return interactive(display_markdown, md_file=md_files)


def image_viewer(img_files):
	if type(img_files) is str:
		img_files = [f.split('.')[0] for f in os.listdir(img_files) if f.endswith('.png')]
	
	return interactive(display_image, img_file=img_files, scale=widgets.FloatSlider(min=0.5, max=1.5, step=0.1, value=1))