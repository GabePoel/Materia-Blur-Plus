import os
import sys

home = os.path.expanduser("~")
usr = os.path.expanduser("/usr")
insdir = os.getcwd()
locdir = os.path.join(home, ".local", "share", "plasma", "desktoptheme")
usrdir = os.path.join(usr, "share", "plasma", "desktoptheme")

atroot = False

def link(name, root=False):
    prefix = ""
    tardir = locdir
    if root:
        prefix = "sudo "
        tardir = usrdir
    os.system(prefix + "ln -sf '" + os.path.join(insdir, name) + "' " + tardir)

def move(name, root=False):
    prefix = ""
    tardir = locdir
    if root:
        prefix = "sudo "
        tardir = usrdir
    os.system(prefix + "mvdir '" + os.path.join(insdir, name) + "' " + tardir)
    
themes = ["Materia-Blur-Plus"]

if len(sys.argv) == 1:
    raise ValueError("No input provided.\nPlease specify either 'link' or 'move'.")
try:
    if sys.argv[2] == "-root":
        atroot = True
except:
    pass
for theme in themes:
    if sys.argv[1] == "link":
        link(theme, atroot)
    elif sys.argv[1] == "move":
        move(theme, atroot)
    else:
        raise ValueError("Invalid input provided.\nPlease specify either 'link' or 'move'.")
