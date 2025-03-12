class CompteBancaire:
    def __init__(self, proprietaire):
        self.proprietaire = proprietaire
        self.solde = 0
    
    def deposer(self, montant):
        self.solde = self.solde + montant
        print(f"{montant} € ont été ajoutés sur le compte de {self.proprietaire}")
    
    def retirer(self, montant):
        if self.solde - montant < 0:
            print("Montant trop haut pour être enlevé")
        else:
            self.solde = self.solde - montant
            print(f"{montant} € ont été retirés sur le compte de {self.proprietaire}")
    
    def afficher_infos(self):
        print(f"Solde de {self.proprietaire} : {self.solde} €")

mon_compte = CompteBancaire("Grégoire")
mon_compte.deposer(500)
mon_compte.retirer(200)
mon_compte.afficher_infos()
mon_compte.retirer(400)