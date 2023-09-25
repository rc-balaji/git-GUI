from setuptools import setup
import py2exe

APP = "build.py"
OPTIONS = {
    "iconfile":'git_img.png',
    'packages':['tkinter','os','subprocess','git']
}
setup(
    app=APP,
    options={
        'py2exe': OPTIONS
    }
    
)
