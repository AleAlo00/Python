"""
4)
Crea una classe Animale con attributi nome ed età e i metodi di base. 
Parti dalla classe Animale e crea una gerarchia di classi con la classe Cane e la classe Gatto che derivano
dalla classe Animale. Realizza il diagramma UML, evidenzia gli attributi della classe Cane
e della classe Gatto e aggiungi i metodi necessari per la loro gestione.
"""


class Animale(object):
    nome = ""
    eta = 0

    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def modifica(self, nome, eta):
        if nome != "":
            self.nome = nome
        if eta != 0:
            self.eta = eta


    def visualizza(self):
        print(f"\nNome: {self.nome}\nEtà: {self.eta}")



class Cane(Animale):
    razza = ""
    colore = ""

    def __init__(self, nome, eta, razza, colore):
        super().__init__(nome, eta)
        self.razza = razza
        self.colore = colore

    def modifica(self, nome, eta, razza, colore):
        super().modifica(nome, eta)
        if razza != "":
            self.razza = razza
        if colore != "":
            self.colore = colore

    def visualizza(self):
        super().visualizza()
        print(f"Razza: {self.razza}")
        print(f"Colore: {self.colore}")

    def abbaia(self):
        print("Woof woof!")


class Gatto(Animale):
    razza = ""
    colore = ""

    def __init__(self, nome, eta,razza, colore):
        super().__init__(nome, eta)
        self.razza = razza
        self.colore = colore

    def modifica(self, nome, eta, razza, colore):
        super().modifica(nome, eta)
        if razza != "":
            self.razza = razza
        if colore != "":
            self.colore = colore

    def visualizza(self):
        super().visualizza()
        print(f"Razza: {self.razza}")
        print(f"Colore: {self.colore}")

    def miagola(self):
        print("Miao miao!")