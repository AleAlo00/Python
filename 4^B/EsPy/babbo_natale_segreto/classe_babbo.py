class Persona(object):

    nome = ""
    cognome = ""
    data = ""
    indirizzo = ""
    telefono = ""

    def __init__(self , nome , cognome , data_nascita , indirizzo , telefono ):
        
        self.nome = nome
        self.cognome = cognome
        self.data = data_nascita
        self.indirizzo = indirizzo
        self.telefono = telefono

    def modifica(self , nome , cognome , data_nascita , indirizzo , telefono):
        
        if nome != "":
            self.nome = nome
        if cognome != "":
            self.cognome = cognome
        if data_nascita != "":
            self.data = data_nascita
        if indirizzo != "":
            self.indirizzo = indirizzo
        if telefono != "":
            self.telefono = telefono

    def visualizza(self):
        
        print("\n------------------------------------\n")
        print(f"Nome: {self.nome}")
        print(f"Cognome: {self.cognome}")
        

class Amico(Persona):

    regalo_comprato = ""
    regalo_ricevuto = ""
    ricevuto = False
    donato = False

    def __init__(self, nome , cognome , data_nascita , indirizzo , telefono   ):
        super().__init__( nome , cognome , data_nascita , indirizzo , telefono )
        self.ricevuto = False
        self.donato = False
        

    def visualizza(self):
        super().visualizza()
        print(f"Regalo comprato: {self.regalo_comprato}")
        print(f"Regalo ricevuto: {self.regalo_ricevuto}")
        print(f"\n--------------------------------------\n")

    def regala(self , other):
        self.regalo_ricevuto = other.regalo_comprato
        other.ricevuto = True
        self.donato = True

    def compra_regalo(self , regalo):
        self.regalo_comprato = regalo