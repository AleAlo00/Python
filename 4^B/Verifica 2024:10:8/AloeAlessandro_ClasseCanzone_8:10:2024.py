

class Canzone(object):
    #attributi
    titolo = ""
    cantante = ""
    autore = ""
    durata = 0.0
    genere = ""
    playlist = ""

    #metodi
    #costruttore
    def __init__(self, titolo, cantante, autore, durata, genere):
        self.titolo = titolo
        self.cantante = cantante
        self.autore = autore
        self.durata = durata
        self.genere = genere

    #modifica
    def modifica(self, titolo, cantante, autore, durata, genere):
        if titolo != "":
            self.titolo = titolo

        if cantante != "":
            self.cantante = cantante

        if autore != "":
            self.autore = autore

        if durata != 0:
            self.durata = durata

        if genere != "":
            self.genere = genere

    #visualizza
    def visualizza(self):
        print("<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>")
        print(f"Titolo: {self.titolo}")
        print(f"Cantante: {self.cantante}")
        print(f"Autore: {self.autore}")
        print(f"Durata: {self.durata}")
        print(f"Genere: {self.genere}")
        if self.playlist == "":
            print("Playlist non assegnata")
        else:
            print(f"Playlist: {self.playlist}")
        print("<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>")

    #assegnamento playlist
    def assegnamento_playlist(self,playlist):
        self.playlist = playlist




#main
#input
titolo = input("\nInserisci il titolo della canzone: ")
cantante = input(f"Inserisci il cantante della canzone {titolo}: ")
autore = input(f"Inserisci l'autore della canzone {titolo}: ")
durata = -1
while durata < 0:
    try:
        durata = float(input(f"Inserisci la durata della canzone {titolo}: "))
        if durata < 0:
            print("Inserisci valore positivo")

    except ValueError:
        print("Inserisci valore valido")

genere = input(f"Inserisci il genere della canzone {titolo}: ")

#creazione istanza
es_canzone = Canzone(titolo,cantante,autore,durata,genere)

#menu
scelta = 0
while scelta != 4:
    try:

        scelta = int(input("""
        <~~~~~~~~~~~~~~~~~~~~~~~~~~ Opzioni Canzone ~~~~~~~~~~~~~~~~~~~~~~~~~~>
        [ 1 ] Modifica i dati della canzone
        [ 2 ] Visualizza canzone
        [ 3 ] Assegna la canzone a una playlist
        [ 4 ] Esci
                           
        -->| """))

        if scelta not in [1,2,3,4]:
            print("Scelta non valida")

    except ValueError:
        print("Scelta non valida")

    #modifica
    if scelta == 1:
        print("Modifica")
        opzioni = ["titolo", "cantante", "autore", "durata", "genere"]

        for i in range(len(opzioni)):
            print(f"[ {i+1} ] {opzioni[i]}")

        try:
            scelta_modificata = int(input("Inserisci il numero corrispondente: "))
            if scelta_modificata not in [1, 2, 3, 4, 5]:
                print("Errore! Inserire un numero tra 1 e 5")

            if scelta_modificata == 1:
                titolo = input("Inserisci il titolo della nuova canzone: ")

            elif scelta_modificata == 2:
                cantante = input(f"Inserisci il nuovo cantante della canzone {titolo}: ")

            elif scelta_modificata == 3:
                autore = input(f"Inserisci il nuovo autore della canzone {titolo}: ")

            elif scelta_modificata == 4:
                durata = -1
                while durata < 0:
                    try:
                        durata = float(input(f"Inserisci la durata della canzone {titolo}: "))
                        if durata < 0:
                            print("Inserisci valore positivo")

                    except ValueError:
                        print("Inserisci valore valido")

            elif scelta_modificata == 5:
                genere = input(f"Inserisci il nuovo genere della canzone {titolo}: ")

            es_canzone.modifica(titolo,cantante,autore,durata,genere)

        except ValueError:
            print("Errore! Inserire un numero intero")

    #visualizza
    elif scelta == 2:
        print("Dati Canzone")
        es_canzone.visualizza()
    
    #assegnamento playlist
    elif scelta == 3:
        print("Assegnamento alla playlist")
        playlist = input("Inserisci il nome della playlist: ")
        es_canzone.assegnamento_playlist(playlist)
        
    #esci
    elif scelta == 4:
        print("Arrivederci e buona musica")

    else:
        print("Inserisci valore valido")
        
