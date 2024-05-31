class Plat:
    
    def __init__(self,nom:str="",description:str="",prix:int=0,categorie:str=""):
        self.nom=nom
        if self.nom=="":self.demanderNom()
        
        self.description=description
        if self.description=="":self.demanderDescription()
       
        self.prix=prix if prix>0 and isinstance(prix,int) else 0
        if self.prix==0:self.definitionPrix()

        self.categorie=categorie
        if self.categorie=="":self.definitionCategorie()

    def demanderNom(self):
        self.nom=input("Entrer le nom du plat: ")

    def demanderDescription(self):
        self.description=input("Decrivez le plat :")

    def definitionPrix(self):
        self.prix=input("Veuillez définir le prix du plat :")

    def definitionCategorie(self):
        print("Catégorisez le plat :")
        categorie=["entrées","plats principaux","desserts","boissons"]
        i=0
        while i<len(categorie):
            print(categorie[i]+":("+str(i))
            i+=1
        while True:
            i=int(input(":"))
            if 0<=i<=4 : break
        self.categorie=categorie[i]

#plat1=Plat()
