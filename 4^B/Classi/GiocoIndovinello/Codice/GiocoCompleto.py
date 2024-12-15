class Personaggio(object):
    # Attributi
    nome = ""
    sponda = 0
    mangiato = False
    genere = ""

    # Metodi
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

    def mangia(self, other):
        print(f"{self.nome} ha mangiato {other.nome}\nHai perso!")
        other.mangiato = True
        if (self.genere == "carnivoro" and other.genere == "erbivoro") or (self.genere == "erbioro" and other.genere == "vegetale"):
            other.mangiato = True

def controllo_input():
    verifica = True
    while verifica:
        try:
            domanda = input("\n-->| ").capitalize()
            if domanda not in ["Capra", "Lupo", "Cavolo", "Nessuno"]:
                print("Input non valido.")
            else:
                verifica = False
                return domanda
        except ValueError:
            print("Input non valido.")

def VerificaMangia():
    for elemento1 in Elementi:
        for elemento2 in Elementi:
            if elemento1.sponda == elemento2.sponda and elemento1.sponda != Contadino.sponda:
                if (elemento1.genere == "carnivoro" and elemento2.genere == "erbivoro") or (elemento1.genere == "erbivoro" and elemento2.genere == "vegetale"):
                    elemento1.mangia(elemento2)
                    return True  
    return False  


def VerificaVittoria():
    for componente in Elementi:
        if componente.sponda != 1:
            return False
    return True

def MovimentoContadino():
    if Contadino.sponda == 0:
        sponda_0.remove(Contadino)
        sponda_1.append(Contadino)
    else:
        sponda_1.remove(Contadino)
        sponda_0.append(Contadino)
    Contadino.in_barca()

# Creazione dei personaggi
Contadino = Personaggio("Contadino", "umano")
Capra = Personaggio("Capra", "erbivoro")
Lupo = Personaggio("Lupo", "carnivoro")
Cavolo = Personaggio("Cavolo", "vegetale")

Elementi = [Lupo, Cavolo, Capra]
sponda_0 = [Contadino, Lupo, Cavolo, Capra]
sponda_1 = []

game = True
while game:
    print("\nSponda Destra:\n")
    for componente in sponda_0:
        print(componente.nome)

    print("\nSponda Sinistra:\n")
    for componente in sponda_1:
        print(componente.nome)


    if Contadino.sponda == 0:
        print("\nScegli chi spostare dalla sponda destra -- >| ") 
    else:
        print("\nScegli chi spostare dalla sponda sinistra -- >| ")
    
    disponibili = []
    for componenti in Elementi:
        if componenti.sponda == Contadino.sponda:
            disponibili.append(componenti.nome)
    disponibili.append("Nessuno")  
    print("Opzioni disponibili:", ", ".join(disponibili))
    
    spostare = controllo_input()

    if spostare != "Nessuno":
        for componenti in Elementi:
            if componenti.nome == spostare and componenti.sponda == Contadino.sponda:
                if Contadino.sponda == 0:
                    sponda_0.remove(componenti)
                    sponda_1.append(componenti)
                else:
                    sponda_1.remove(componenti)
                    sponda_0.append(componenti)
                componenti.in_barca()
                
    MovimentoContadino()


    if VerificaMangia():
        game = False
        
    if VerificaVittoria():
        game = False
        print("\nHai vinto!")
