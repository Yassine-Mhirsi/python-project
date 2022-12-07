import produit
class Stock :
    def __init__(self) :
        self.produits=[]
    def ajouter_produit(self,nom,puht,qt):
        self.produits.append(nom)
        self.produits.append(puht)
        self.produits.append(qt)
    def saisir(self,n):
        for i in range(n):
            nom,puht,qt=produit.saisir_produit()
            self.ajouter_produit(nom,puht,qt)
    def afficher(self):
        start = 0
        end = len(self.produits)
        step = 3
        print("NOM     |PUHT    |QUANTITE")
        for i in range(start, end, step):
            x = i
            h=self.produits[x:x+step]
            print("{:<8}|{:<8}|{}".format(self.produits[i],self.produits[i+1],self.produits[i+2]))
    def rechercher_produit(self,nom) :
        se_trouve=False
        indice=None
        for i in range(len(self.produits)):
            if self.produits[i]==nom :
                se_trouve=True
                indice=i
        return se_trouve,indice
    def supprimer(self,nom):
        se_trouve,indice=self.rechercher_produit(nom)
        if se_trouve==True:
            del self.produits[indice+2] 
            del self.produits[indice+1] 
            del self.produits[indice] 
            return True
        else : 
            return False
    def modifier_produit(self,nom,new_nom='',new_puht=-1,new_qt=-1):
        se_trouve,indice=self.rechercher_produit(nom)
        if se_trouve==True:
            if new_nom=='':
                self.produits[indice]=self.produits[indice]   
                self.produits[indice+1]=new_puht  
                self.produits[indice+2]=new_qt  
            if new_puht==-1:
                self.produits[indice]=new_nom  
                self.produits[indice+1]=self.produits[indice+1]  
                self.produits[indice+2]=new_qt   
            if new_qt==-1:
                self.produits[indice]=new_nom  
                self.produits[indice+1]=new_puht  
                self.produits[indice+2]=self.produits[indice+2]   
        else:
            return True
    def acheter_produit(self,nom,qt_p):
        se_trouve,indice=self.rechercher_produit(nom)
        global quantite_max
        quantite_max=100
        h=self.produits[indice+2]+qt_p  
        while qt_p>=1 :
            if se_trouve==True and h<=100:
                self.produits[indice+2]=h  
                return True
            else : 
                return False
    def vendre_produit(self,nom,qt_u):
        se_trouve,indice=self.rechercher_produit(nom)
        h=self.produits[indice+2]-qt_u  
        while qt_u>1 :
            if se_trouve==True and h>1:
                self.produits[indice+2]=h  
                return True
            elif se_trouve==True and h==0 :
                self.supprimer(nom)
                return True
            else : 
                return False 
    def enregistrer(self,f):
        fich=open(f,'w+')
        for i in range(len(self.produits)):
            prds=produit.produit2chaine(self.produits[i],self.produits[i+1],self.produits[i+2])
            fich.write(prds)
        fich.close()
    def charger(self,f):
        fich = open(f,'r+')
        for ligne in fich :
            nom,puht,qt=produit.chaine2produit(ligne) 
            self.produits.append(nom)
            self.produits.append(puht)
            self.produits.append(qt)
        fich.close()