"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['Pynstagooey.py']
DATA_FILES = ['Pashua.app', 'Pashua.py', 'cacert.pem']
OPTIONS = {'argv_emulation': True,
	   'packages': ['pynstagram'],
           'iconfile': 'icon.icns'
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
