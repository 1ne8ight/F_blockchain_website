from application import app
from flask import render_template, redirect, url_for, request
from flask_mail import Mail, Message
from application.config import Config


#appliquer les config de notre boite mail de reception
app.config.from_object(Config)
mail = Mail(app)

# chemin vers notre index html
@app.route('/')
def index():
    return render_template('index.html')

# chemin vers notre index html au clic depuis une autre page
@app.route('/index.html')
def retour():
    return render_template('index.html')

#chemin vers a propos (about)
@app.route('/about.html')
def about():
    return render_template('about.html')

#chemin vers a nous contactez
@app.route('/contact.html')
def contact():
    return render_template('contact.html')

#parametrage de l'envoi de la preocupation d'un utilistateur
@app.route('/contact.html', methods=['POST'])
def envoyer():
    #recuperation des infos depuis notre formulaire html
    if request.method == 'POST' :
        nom = request.form['nom']
        prenom = request.form['prenom']
        telephone = request.form['telephone']
        email = request.form['email']
        preocupation = request.form['preocupation']

        #Configuration du corps du mail
        msg = Message('preocupation',
                      sender=email,
                recipients=['tanoheliezerbonny@gmail.com'])
        msg.body = "Nom: " + nom + "\n" +"Prenom: " + prenom + "\n" +"Telephone: " + telephone  + "\n" +"Email: " + email  + "\n" + "preocupation :" + preocupation
        # msg.html = "<p>" + preocupation + "</p>"
        mail.send(msg)
        
        return render_template("contact.html", sended="Message Envoyer!!")



#chemin vers la page de crypto
@app.route('/crypto.html')
def crypto():
    return render_template('crypto.html')

#chemin vers la page de metaverse
@app.route('/metaverse.html')
def metaverse():
    return render_template('metaverse.html')

#chemin vers la page de nft
@app.route('/nft.html')
def nft():
    return render_template('nft.html')

#chemin vers la page de web3
@app.route('/web3.html')
def web3():
    return render_template('web3.html')

