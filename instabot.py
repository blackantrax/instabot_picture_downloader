import instaloader
import stdiomask
import os

#Couleur Verte
#os.system('color a')

affichage = 'InstaDownloader> '
instabot = instaloader.Instaloader()

def Telecharger_posts():
    identifiant = str(input("Quel est le profil de la cible: "))
    state = True
    confimation_utilisateur = str(input("Voulez-vous télécharger tous les posts (y/n) ? "))
    if confimation_utilisateur == "y":
        state = False
       #instabot.download_post(identifiant,profile_pic_only=state)
        #instabot.download_post(identifiant,Profile.get_posts())
        for identifiant in instaloader.Hashtag.from_name(instabot.context, 'fineboys').get_posts():
            instabot.download_post(identifiant,target='#fineboys')

def Auth():
    identifiant = str(input("Entrez-votre nom d'utilisateur: ")) 
    mot_de_passe = str(stdiomask.getpass("Entrez-votre mot de passe: "))
    instabot.login(identifiant,mot_de_passe)
    

def Execution(f):
    try:
        f()
    except Exception as Error:
        print(Error)
while True:
    terminal = str(input(affichage))
    
    if terminal == 't':
        Execution(Telecharger_posts())
    if terminal == 'login':
        Execution(Auth())
    if terminal == 'q':
        break
    
    
    
#profile = Profile.from_username(L.context, USERNAME)
