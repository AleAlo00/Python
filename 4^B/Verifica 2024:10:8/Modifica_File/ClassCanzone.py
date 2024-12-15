
class Canzone(object):
    #attributi
    titolo = ""
    cantante = ""
    autore = ""
    durata = 0.0
    genere = ""
    playlist = []

    #metodi
    #costruttore
    def __init__(self, titolo, cantante, autore, durata, genere):
        self.titolo = titolo
        self.cantante = cantante
        self.autore = autore
        self.durata = str(durata)
        self.genere = genere

    #modifica
    def modifica(self, titolo, cantante, autore, durata, genere):
        if titolo != "":
            self.titolo = titolo

        if cantante != "":
            self.cantante = cantante

        if autore != "":
            self.autore = autore

        if str(durata) != "":
            self.durata = str(durata)

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
        if self.playlist == []:
            print("Playlist non assegnata")
        else:
            print(f"Playlist: {self.playlist}")
        print("<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>")

    #assegnamento playlist
    def assegnamento_playlist(self,playlist):
        self.playlist.append(playlist)

