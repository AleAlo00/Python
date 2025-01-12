"""
6)
Aggiungi alla gerarchia di classi dell’Esercizio 4 la classe Anatra che deriva dalla classe
base Animale. Aggiungi la nuova classe al diagramma UML, quindi definisci gli
attributi della nuova classe e inserisci un attributo che descrive come si muove.
"""

from Es4 import Animale

class Anatra(Animale):
    colore = ""
    tipo = ""
    muove = ""

    def __init__(self, nome, eta, colore, tipo,muove):
        super().__init__(nome, eta)
        self.colore = colore
        self.tipo = tipo
        self.muove = muove


    def modifica(self, nome, eta, colore, tipo, muove):
        super().modifica(nome, eta)
        if colore != "":
            self.colore = colore
        if tipo != "":
            self.tipo = tipo
        if muove != "":
            self.muove = muove

    def visualizza(self):
        super().visualizza()
        print(f"Colore: {self.colore}")
        print(f"Tipo: {self.tipo}")
        print(f"Come si muove: {self.muove}")

    def nuota(self):
        print("Quack quack!")

    