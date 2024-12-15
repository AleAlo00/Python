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
            domanda = input().capitalize()
            if domanda not in ["Capra", "Lupo", "Cavolo", "Nessuno"]:
                print("Input non valido.")
            else:
                verifica = False
                return domanda
        except ValueError:
            print("Input non valido.")


# Creazione dei personaggi
Contadino = Personaggio("Contadino", "umano")
Capra = Personaggio("Capra", "erbivoro")
Lupo = Personaggio("Lupo", "carnivoro")
Cavolo = Personaggio("Cavolo", "vegetale")

game = True
while game:
    print("\nScegli chi spostare dalla sponda sinistra (Capra, Lupo, Cavolo) -- >| ")
    spostare = controllo_input()
    
    if spostare == "Capra":
        Capra.in_barca()
        Contadino.in_barca()
        print("\nChi vuoi far tornare? (Capra, Nessuno) -->| ")
        ritorno = controllo_input()

        if ritorno == "Nessuno":
            Contadino.in_barca()
            print("\nScegli chi spostare tra Cavolo e Lupo -->|")
            spostare = controllo_input()
            if spostare == "Cavolo":
                Cavolo.in_barca()
                Contadino.in_barca()
                Capra.mangia(Cavolo)
                game = False
            elif spostare == "Lupo":
                Lupo.in_barca()
                Contadino.in_barca()
                print("\nChi vuoi far tornare? (Capra, Nessuno) -->| ")
                ritorno = controllo_input()
                if ritorno == "Nessuno":
                    Contadino.in_barca()
                    Lupo.mangia(Capra)
                    game = False
                elif ritorno == "Capra":
                    Capra.in_barca()
                    Contadino.in_barca()
                    print("\nScegli chi spostare tra Capra e Cavolo -->| ")
                    spostare = controllo_input()
                    if spostare == "Capra":
                        Capra.in_barca()
                        Contadino.in_barca()
                        Lupo.mangia(Capra)
                        game = False
                    elif spostare == "Cavolo":
                        Cavolo.in_barca()
                        Contadino.in_barca()
                        print("\nChi vuoi far tornare? (Lupo, Nessuno) -->| ")
                        ritorno = controllo_input()
                        if ritorno == "Lupo":
                            Lupo.in_barca()
                            Contadino.in_barca()
                            Lupo.mangia(Capra)
                            game = False
                        elif ritorno == "Nessuno":
                            Contadino.in_barca()
                            print("\nHai vinto!")
                            game = False

        elif ritorno == "Capra":
            Capra.in_barca()
            Contadino.in_barca()
            print("\nSei tornato indietro\nHai perso!")
            game = False

    elif spostare == "Lupo":
        Capra.mangia(Cavolo)
        game = False
    elif spostare == "Cavolo":
        Lupo.mangia(Capra)
        game = False
