#Classe Libro

class Libro(object):
    #attributi
    titolo = ""
    autori = []
    casa_editrice = ""
    prezzo = 0.0
    numero_pagine = 0
    disponibilità = 0

    #metodi
    def __init__(self, titolo, autori, casa_editrice, prezzo, numero_pagine):
        self.titolo = titolo
        self.autori = autori
        self.casa_editrice = casa_editrice
        self.prezzo = float(prezzo)
        self.numero_pagine = numero_pagine 

    def modifica(self, titolo, autore, casa_editrice, numero_pagine):
        if titolo != "":
            self.titolo = titolo
        if autore != "":
            self.autore = autore
        if casa_editrice != "":
            self.casa_editrice = casa_editrice

        if numero_pagine != 0:
            self.numero_pagine = numero_pagine

    def visualizza(self):
        print("\n<~~~~~~~~~~~~~~~Libro~~~~~~~~~~~~~~~>")
        print("Titolo: ", self.titolo)
        for autore in self.autori:
            print("Autore: ", autore)
        print("Casa Editrice: ", self.casa_editrice)
        print("Prezzo: €{:.2f}".format(self.prezzo))
        print("Numero Pagine: ", self.numero_pagine)
        if self.disponibilità > 0:
            print(f"{self.disponibilità} copie disponibili")
        else:
            print("Non disponibile")
        print("<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>")

    def cambia_prezzo(self, percentuale):
        percentuale = float(percentuale)
        self.prezzo = float(self.prezzo)
        self.prezzo += self.prezzo * percentuale / 100
    
    def modifica_disponibilita(self, disponibilità):
        self.disponibilità = disponibilità

