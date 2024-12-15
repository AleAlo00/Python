# Description: Gioco dell'indovinello
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
        print(f"{self.nome} ha mangiato {other.nome}\nHai perso")

        if (self.genere == "carnivoro" and other.genere == "erbivoro") or (self.genere == "erbioro" and other.genere == "vegetale"):
            other.mangiato = True

def VisualizaSponde():
    print("\n<~~~~~~~~~~Disposizione~~~~~~~~~~>\n")
    print("Sponda destra:")
    for componenti in sponda_0:
        print(f"{componenti.nome}")
    print("\nSponda sinistra:")
    for componenti in sponda_1:
        print(f"{componenti.nome}")

#Gestione gioco
#Creazione personaggi
Contadino = Personaggio("Contadino","umano")
Capra = Personaggio("Capra","erbivoro")
Lupo = Personaggio("Lupo","carnivoro")
Cavolo = Personaggio("Cavolo","vegetale")

Elementi = [Lupo,Cavolo,Capra]
sponda_0 = [Capra,Lupo,Cavolo]
sponda_1 = []



game = True
while game:
    try:
        print("\n<~~~~~~~~~~Personaggi~~~~~~~~~~>")
        for i,componenti in enumerate(Elementi):
            print(f"{i+1} - {componenti.nome}")
            
        Spostare = int(input("\nChi vuoi spostare? --->| "))

        if Spostare not in [1,2,3]:
            print("Elemento non valido")
    except ValueError:
        print("Elemento non valido")

    if Spostare == 1:
        Capra.mangia(Cavolo)
        game = False

    elif Spostare == 2:
        Lupo.mangia(Capra)
        game = False

    elif Spostare == 3:
        Capra.in_barca()
        sponda_0.remove(Capra)
        sponda_1.append(Capra)
        Contadino.in_barca()
        VisualizaSponde()
        

        try:
            domanda_riportare = input("\nVuoi riportare qualcuno? (Y / N) --->| ").lower()
            if domanda_riportare not in ["y","n"]:
                print("Elemento non valido")
        except ValueError:
            print("Elemento non valido")



        if domanda_riportare == "y":

            print("\n<~~~~~~~~~~Personaggi~~~~~~~~~~>")
            for i, componenti in enumerate(sponda_1):
                print(f"{i+1} - {componenti.nome}")
            print(f"{len(sponda_1)+1} - Nessuno")

            try:
                Riportare = int(input("\nChi vuoi riportare? --->| "))

                if Riportare > len(sponda_1) + 1:
                    print("Elemento non valido")
                    
            except ValueError:
                print("Elemento non valido")

            if Riportare == 1:
                Capra.in_barca()
                Contadino.in_barca()
                print("Sei tortato all'inizio")
                game = False

            if Riportare == 2:
                domanda_riportare = "n"

        if domanda_riportare == "n":
            VisualizaSponde()
            print("\n<~~~~~~~~~~Personaggi~~~~~~~~~~>")
            for i,componenti in enumerate(sponda_0): 
                print(f"{i+1} - {componenti.nome}")
                
            try:
                Spostare = int(input("\nChi vuoi spostare? --->| "))
                if Spostare > len(sponda_0):
                    print("Elemento non valido")
            except ValueError:
                print("Elemento non valido")

            if Spostare == 1:
                Lupo.in_barca()
                Contadino.in_barca()
                sponda_1.append(Lupo)
                sponda_0.remove(Lupo)

                VisualizaSponde()
                print("\n<~~~~~~~~~~Personaggi~~~~~~~~~~>")
                for i, componenti in enumerate(sponda_1):
                    print(f"{i+1} - {componenti.nome}")
                print(f"{len(sponda_1)+i} - Nessuno")
                try:
                    Riportare = int(input("\nChi vuoi riportare? --->| "))

                    if Riportare > len(sponda_1)+1:
                        print("Elemento non valido")
                except ValueError:
                    print("Elemento non valido")

                if Riportare == 1:
                    Capra.in_barca()
                    sponda_0.append(Capra)
                    sponda_1.remove(Capra)
                    Contadino.in_barca()

                    VisualizaSponde()

                    for i, componenti in enumerate(sponda_0):
                        print(f"{i+1} - {componenti.nome}")
                    
                    try:
                        Spostare = int(input("\nChi vuoi spostare? --->| "))
                        if Spostare > len(sponda_0):
                            print("Elemento non valido")
                    except ValueError:
                        print("Elemento non valido")

                    if Spostare == 1:
                        Cavolo.in_barca()
                        sponda_1.append(Cavolo)
                        sponda_0.remove(Cavolo)
                        Contadino.in_barca()

                        VisualizaSponde()

                        print("\n<~~~~~~~~~~Personaggi~~~~~~~~~~>")
                        for i, componenti in enumerate(sponda_1):
                            print(f"{i+1} - {componenti.nome}")
                        print(f"{len(sponda_1)+i} - Nessuno")

                        try:
                            Riportare = int(input("\nChi vuoi riportare? --->| "))
                            if Riportare > len(sponda_1)+1:
                                print("Elemento non valido")
                        except ValueError:
                            print("Elemento non valido")

                        if Riportare == 1:
                            Lupo.in_barca()
                            Contadino.in_barca()
                            Lupo.mangia(Capra)
                            game = False

                        elif Riportare == 2:
                            Capra.in_barca()
                            Contadino.in_barca()
                            Capra.mangia(Cavolo)
                            game = False

                        elif Riportare == 3:
                            Contadino.in_barca()

                            VisualizaSponde()

                            print("\n<~~~~~~~~~~Personaggi~~~~~~~~~~>")
                            for i, componenti in enumerate(sponda_0):
                                print(f"{i+1} - {componenti.nome}")

                            try:
                                Spostare = int(input("\nChi vuoi spostare? --->| "))
                                if Spostare > len(sponda_0):
                                    print("Elemento non valido")
                            except ValueError:
                                print("Elemento non valido")
                            
                            if Spostare == 1:
                                Capra.in_barca()
                                sponda_0.remove(Capra)
                                sponda_1.append(Capra)
                                Contadino.in_barca()
                                Lupo.mangia(Capra)
                                VisualizaSponde()
                                
                                print("\nHai visto ")
                                game = False

                    elif Spostare == 2:
                        Capra.in_barca()
                        Contadino.in_barca()
                        Lupo.mangia(Capra)
                        game = False
                
                elif Riportare == 2:
                    Contadino.in_barca()
                    Lupo.in_barca()
                    print("Sei tornato all'inizio")
                    game = False

                elif Riportare == 3:
                    Lupo.mangia(Capra)
                    game = False

            if  Spostare == 2:
                Cavolo.in_barca()
                Contadino.in_barca()
                Capra.mangia(Cavolo)
                game = False