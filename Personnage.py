class Personnage:
    def __init__(self, nom, classe, niveau, points_de_vie, force, intelligence):
        self.nom = nom
        self.classe = classe
        self.niveau = niveau
        self.points_de_vie = points_de_vie
        self.force = force
        self.intelligence = intelligence

    def afficher_info(self):
        print(f"Nom: {self.nom}")
        print(f"Classe: {self.classe}")
        print(f"Niveau: {self.niveau}")
        print(f"Points de vie: {self.points_de_vie}")
        print(f"Force: {self.force}")
        print(f"Intelligence: {self.intelligence}")

    def attaquer(self, cible):
        print(f"{self.nom} attaque {cible.nom}!")
        degats = self.force * 2
        cible.subir_degats(degats)

    def subir_degats(self, degats):
        self.points_de_vie -= degats
        print(f"{self.nom} subit {degats} points de dégâts!")
