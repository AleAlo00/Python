#Classe Atleta
#Libreria Atleta

class Atleta:
    #attributi
    nome = ""
    cognome = ""
    squadra = ""
    sport = ""
    visita_medica = False

    #metodi
    #costruttore
    def __init__(self, nome, cognome, sport):
        self.nome = nome
        self.cognome = cognome
        self.sport = sport

    #modifica dati
    def modifica(self, nome, cognome, sport):
        if nome != "":
            self.nome = nome

        if cognome != "":
            self.cognome = cognome

        if sport != "":
            self.sport = sport

    #stampa dati
    def visualizza(self):
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print("Nome: ", self.nome)
        print("Cognome: ", self.cognome)
        print("Squadra: ", self.squadra)
        print("Sport: ", self.sport)
        print("Visita Medica: ", self.visita_medica)
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        

    #assegna squadra
    def assegna_squadra(self, squadra):
        self.squadra = squadra

    #effettua visita
    def effettua_visita(self, risposta):
        if risposta == "si":
            self.visita_medica = True
        else:
            self.visita_medica = False



