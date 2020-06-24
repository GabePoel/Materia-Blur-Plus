import os
import sys

home = os.path.expanduser("~")
insdir = os.getcwd()
tardir = os.path.join(home, ".local", "share", "plasma", "desktoptheme")

def link(name):
    #if not os.path.exists(os.path.join(tardir, name)):
        #os.makedirs(os.path.join(tardir, name))
    os.system("ln -sf '" + os.path.join(insdir, name) + "' " + tardir)

def move(name):
    os.system("mvdir '" + os.path.join(insdir, name) + "' " + tardir)
    
themes = ["Materia-Blur-Plus"]

if len(sys.argv) == 1:
    raise ValueError("No input provided.\nPlease specify either 'link' or 'move'.")
for theme in themes:
    if sys.argv[1] == "link":
        link(theme)
    elif sys.argv[1] == "move":
        move(theme)
    else:
        raise ValueError("Invalid input provided.\nPlease specify either 'link' or 'move'.")
