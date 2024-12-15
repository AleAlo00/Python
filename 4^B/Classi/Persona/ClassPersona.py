#Persona con la Classe
#Libreria Persona

class Persona(object):
    #attributi
    nome = ""
    cognome = ""
    data_nascita = ""
    indirizzo = ""
    telefono = ""
    professione = ""

    #metodi
    #costruttore
    def __init__(self, nome, cognome, data_nascita, indirizzo, telefono):
        self.nome = nome
        self.cognome = cognome
        self.data_nascita = data_nascita
        self.indirizzo = indirizzo
        self.telefono = telefono
    
    #modifica
    def modifica(self, nome, cognome, data_nascita, indirizzo, telefono):
        #controllo
        if nome != "":
            #modifica
            self.nome = nome
        #controllo
        if cognome != "":
            #modifica
            self.cognome = cognome
        #controllo
        if data_nascita != "":
            #modifica
            self.data_nascita = data_nascita
        #controllo
        if indirizzo != "":
            #modifica
            self.indirizzo = indirizzo
        #controllo
        if telefono != "":
            #modifica
            self.telefono = telefono

    #visualizza
    def visualizza(self):
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print("Nome: ", self.nome)
        print("Cognome: ", self.cognome)
        print("Data di nascita: ", self.data_nascita)
        print("Indirizzo: ", self.indirizzo)
        print("Telefono: ", self.telefono)
        if self.professione != "":
            print("Professione: ", self.professione)
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    def setProfessione(self, professione):
        self.professione = professione
        


        