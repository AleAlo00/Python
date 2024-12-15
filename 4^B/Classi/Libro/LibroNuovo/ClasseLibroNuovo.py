#Classe Libro
#Libreria Libro

class Libro:
    #attributi
    titolo = ""
    autore = ""
    anno = 0
    pagine = 0
    editore = ""
    genere = ""
    InPrestito = False

    #metodi
    #costruttore
    def __init__(self, titolo, autore, anno, pagine, editore, genere):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.pagine = pagine
        self.editore = editore
        self.genere = genere

    #modifica dati
    def modifica(self, titolo, autore, anno, pagine, editore, genere):
        if titolo != "":
            self.titolo = titolo
        
        if autore != "":
            self.autore = autore
        
        if anno != 0:
            self.anno = anno

        if pagine != 0:
            self.pagine = pagine

        if editore != "":
            self.editore = editore

        if genere != "":
            self.genere = genere
        
    #metodo visualizza
    def visualizza(self):
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print("Titolo: ", self.titolo)
        print("Autore: ", self.autore)
        print("Anno: ", self.anno)
        print("Pagine: ", self.pagine)
        print("Editore: ", self.editore)
        print("Genere: ", self.genere)
        if self.InPrestito == True:
            print("In Prestito")
        else:
            print("Disponibile")
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    #metodo prestito
    def prestito(self, stato):
        if stato == "si":
            self.InPrestito = True
        else:
            self.InPrestito = False

    #metodo restituzione
    def restituisci(self, stato):
        if stato == "si":
            self.InPrestito = False
        else:
            self.InPrestito = True

