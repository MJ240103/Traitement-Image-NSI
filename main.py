# Modules nécessaires
from flask import Flask, request, render_template, send_from_directory
from PIL import Image
import random
import requests

# Application serveur web
app = Flask(__name__)

# Dossier de téléchargement des images
# app.root_path permet de connaître le chemin physique de notre application
dossierImages = app.root_path + '/static/'

# Chargement de l'Hermione avec PIL au premier appel et vérification du fonctionnement
hermione = Image.open(dossierImages + "hermione.jpg")
print("Image de l'Hermione chargée avec succèss ", hermione.size)

# On sauvegarde l'image dans les deux seuls fichiers qui seront servis et affichés sur la page web
hermione.save(dossierImages + "originale.jpg")
hermione.save(dossierImages + "traitement.jpg")

# Fonctions 
from traitements import *


#image aléatoire
def image_web(largeur=400, hauteur=300):
    return Image.open(requests.get(f"https://picsum.photos/{largeur}/{hauteur}", stream = True).raw)

# Page d'accueil et d'affichage des images
@app.route("/" , methods=["GET","POST"])
def accueil():
  #choix image selon checkbox cochée ou non
  if request.args.get("picsum") == "on":
    originale = image_web()
    originale.save(dossierImages + "originale.jpg")
  else:
    originale = hermione
    originale.save(dossierImages + "originale.jpg")
  

  #image client
  #if request.args.get("file") != "":
    #file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

  #gérant du serveur voit le filtre appelé
  print(request.args.get("filtre"))

  #application du traitement
  traitee = originale.copy()
  traitee.save(dossierImages + "traitement.jpg")
  if request.args.get("filtre") == "please":
    traitee = originale.copy()
    traitee.save(dossierImages + "traitement.jpg")
  if request.args.get("filtre") == "bruit":
    traitee = bruit_30(traitee)
    traitee.save(dossierImages + "traitement.jpg")
  if request.args.get("filtre") == "symAxeVertical":
    traitee = sym_axe_vertical(traitee)
    traitee.save(dossierImages + "traitement.jpg")
  if request.args.get("filtre") == "variation_s_g":
    traitee = variation_s_g(traitee)
    traitee.save(dossierImages + "traitement.jpg")
  if request.args.get("filtre") == "filtreEmbossage":
    traitee = filtreEmbossage(traitee)
    traitee.save(dossierImages + "traitement.jpg")
  if request.args.get("filtre") == "filtreContraste":
    traitee = filtreContraste(traitee)
    traitee.save(dossierImages + "traitement.jpg")
  
  #retour hasard du querystring et page html avec images modifiées ou non
  return render_template("index.html" , hasard=random.randint(1,10000))




# Accès à une image dans le dossier images
@app.route('/static/<path:filename>')
def fichier(filename):
    return send_from_directory(dossierImages +  filename, mimetype='image/jpeg')

# Lancement du serveur à l'écoute sur le port 8080
app.run(host='0.0.0.0', port=8080)