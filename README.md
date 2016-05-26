# Pynstagooey

This is a GUI for the [pynstagram](https://github.com/mr0re1/pynstagram)
library. It uses [Pashua](https://www.bluem.net/en/mac/pashua/) for the GUI
through its [python bindings](https://github.com/BlueM/Pashua-Binding-Python).

The app is built with [py2app](https://pythonhosted.org/py2app/) and is
basically just a virtualenv with an icon file and an SSL certificate file.

## Bundling

Follow these steps to create an app bundle on OS X:

- Clone and `cd` into the repository.
- Initialize the virtualenv with
`virtualenv --no-site-packages --distribute .env && source .env/bin/activate && pip install -r requirements.txt`