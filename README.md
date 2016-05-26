# Pynstagooey

This is a GUI for the [pynstagram](https://github.com/mr0re1/pynstagram)
library. It uses [Pashua](https://www.bluem.net/en/mac/pashua/) for the GUI
through its [python bindings](https://github.com/BlueM/Pashua-Binding-Python).

The app is built with [py2app](https://pythonhosted.org/py2app/) and is
basically just a virtualenv with an icon file and an SSL certificate file.

## Bundling

### First build

Follow these steps to create an app bundle on OS X (some commands require sudo):

- Install `pip` with `easy_install pip`
- Install `virtualenv` with `pip install virtualenv`
- Clone and `cd` into the repository
- Initialize the virtualenv with
`virtualenv --no-site-packages --distribute python && source python/bin/activate && pip install -r requirements.txt`
- Build the app using `python setup.py py2app`

The app is now in the `dist` folder.

### Rebuilding

If you wish to rebuild the app, just

- `cd` into the `git` repo
- Delete the `build` and `dist` folders with `rm -rf build dist`
- Activate the `virtualenv` with `source python/bin/activate`
- Build the app using `python setup.py py2app`

The app is now in the `dist` folder.

Note that you could start anew by also removing the `python` folder with `rm -rf python` and re-executing the `virtualenv` command described in the previous section.

## Instructions

This is a very crude app. Enter your Instagram username and password, give it a picture and description, and it takes care of the upload.

Make sure the images you upload have the proper dimensions for Instagram. I am not an Instagram user and so could not tell you what these are.

The errors are not very explicit. Look into the Console for details.

This app was only tested on El Capitan.
