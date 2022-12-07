def saisir_produit() :
    global nom
    nom = input ('Entrer nom : ')
    global puht
    puht=float(input("Entrer puht :"))
    global qt
    qt=int(input('Entrer quantite :'))
    return nom,puht,qt

def afficher_produit(nom,puht,qt):
    print("{:<8s}|{:<8.2f}|{:<5d}".format(nom,puht,qt)) 

def produit2chaine(nom,puht,qt):
    m=('{};{};{}\n'.format(nom,puht,qt))
    # m=('%s;%.2f;%d\n'%(nom,puht,qt))
    return m

def chaine2produit(m):
    m.rstrip() #message[:-1] and removes "\n"
    nom,puht,qt=m.split(";")
    return nom,float(puht),int(qt)
