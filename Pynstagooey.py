#!./python/bin/python
# -*- coding: utf-8 -*-
import Pashua
import os.path
import pynstagram

# os.environ['REQUESTS_CA_BUNDLE'] = os.path('cacert.pem')
os.environ['REQUESTS_CA_BUNDLE'] = os.path.join(os.getcwd(), 'cacert.pem')

app_bundle = os.path.dirname(os.path.dirname(Pashua.locate_pashua()))

conf = """
username.type = textfield
username.label = Utilisateur
username.width = 310
-
password.type = password
password.label = Mot de passe
password.width = 310
-
img.type = openbrowser
img.label = Sélectionner une image
img.filetype = jpg gif png jpeg
img.width = 310
-
cb.type = cancelbutton
cb.label = Annuler
-
description.type = textbox
description.default = Écrire[return]une[return]description!
description.width = 410
description.height = 110
"""

result = Pashua.run(conf)

description = result['description'].replace("[return]", "\n")

with pynstagram.client(result['username'], result['password']) as client:
    client.upload(result['img'], description)
