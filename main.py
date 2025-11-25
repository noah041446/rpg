from Personnage import Personnage
from Arme import Arme

# Exemple d'utilisation de la classe Personnage
epee_legendaire = Arme("Épée légendaire", 10)
joueur1 = Personnage("Aragorn", "Guerrier", 10, 100, 15, 5, epee_legendaire)
joueur2 = Personnage("Gandalf", "Magicien", 10, 80, 5, 15)

joueur1.afficher_info()
joueur2.afficher_info()

joueur1.attaquer(joueur2)
joueur2.afficher_info()