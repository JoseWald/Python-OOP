from Plat import Plat

class Menu(Plat):
    def __init__(self, nom: str = "", description: str = "", prix: int = 0, categorie: str = ""):
        super().__init__(nom, description, prix, categorie)
        self.menu=[
            [self.nom,self.description,self.prix,self.categorie]
        ]


    def ajouterPlat(self):
        self.platInfo()
        self.menu.append([self.nom,self.description,self.prix,self.categorie])
    
    def supprimerPlat(self):
        platAsupprimer=input("Entrer le nom du plat à supprimer:")
        i=0
        platTrouve="Undefined"
        while i<len(self.menu):
            if  self.menu[i][0].lower()==platAsupprimer.lower():
                self.menu.pop(i)
                platTrouve=platAsupprimer
                break
            i+=1
        if platTrouve==platAsupprimer:
            print(platTrouve+"supprimé avec succès")
        else :
            print("plat introuvable") 
    
    def modifierPlat(self):
        platAmodifier=input("Entrer le nom du plat à modifier")
        i=0
        platTrouve="Undefined"
        while i<len(self.menu):
            if  self.menu[i][0].lower()==platAmodifier.lower():
                platTrouve=platAmodifier
                break
            i+=1
        if platTrouve==platAmodifier:
            self.platInfo()
            self.menu[i]=[self.nom,self.description,self.prix,self.categorie]
            print(platTrouve+"modifié avec succès")
        else :
            print("plat introuvable") 


    def afficherMenu(self):
        for i in self.menu:
            print(i)
    
    def platInfo(self):
        super().demanderNom()
        super().demanderDescription()
        super().definitionPrix()
        super().definitionCategorie

"""
menu=Menu()
menu.ajouterPlat()
menu.ajouterPlat()
Menu.afficherMenu(menu)
menu.supprimerPlat()
menu.afficherMenu()
menu.modifierPlat()
menu.afficherMenu()
"""