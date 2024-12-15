#Classe Personaggio per il gioco di ruolo

class Personaggio(object):
    #Attributi
    nome = ""
    sponda = 0
    mangiato = False
    genere = ""

    #Metodi
    def __init__(self, nome, genere):
        self.nome = nome
        self.genere = genere


    def modifica(self, nome):
        if nome != "":
            self.nome = nome


    def visualizza(self):
        print("<~~~~~~~~~~Personaggio~~~~~~~~~~>")
        print(f"Nome: {self.nome}")
        if self.sponda == 0:
            print("Sponda: Destra")
        else:
            print("Sponda: Sinistra")
        print(f"Genere: {self.genere}")
        if self.mangiato:
            print("Mangiato")
        else:  
            print("Non mangiato")
        print("<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>")

    def in_barca(self):
        if self.sponda == 1:
            self.sponda = 0
        else:
            self.sponda = 1
        


    def mangia(self,other):
        print(f"{self.nome} ha mangiato {other.nome}")
        if (self.genere == "carnivoro" and other.genere == "erbivoro") or (self.genere == "erbioro" and other.genere == "vegetale"):
            other.mangiato = True


