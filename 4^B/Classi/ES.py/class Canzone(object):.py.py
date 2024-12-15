class Canzone(object):
    '''classe che descrive una canzone, la durata è in secondi'''
    #attributi
    titolo = ""
    cantante = ""
    autori = ""
    durata = 0
    genere = ""
    playlist = [] 

    #metodi
    def __init__(self,titolo,cantante,autori,durata,genere):
        self.titolo = titolo
        self.cantante = cantante
        self.autori = autori
        self.durata = int(durata)
        self.genere = genere

    def modifica(self,titolo,cantante,autori,durata,genere):
        if titolo != "":
            self.titolo = titolo
        if cantante != "":
            self.cantante = cantante
        if autori != "":
            self.autori = autori
        if durata != "":
            self.durata = int(durata)
        if genere != "":
            self.genere = genere

    def visualizza(self):
        print("Titolo: ",self.titolo)
        print("Cantante: ",self.cantante)
        print("Autori: ",self.autori)
        print("Durata: ",self.durata)
        print("Genere: ",self.genere)
        print("Playlist: ",self.playlist)
        
    def aggiungi_playlist(self,playlist):
        self.playlist.append(playlist)

#main
lista_canzoni = []
punta = open("Canzoni.txt","a")
punta.close()
#lettura iniziale file delle canzoni
punta = open("Canzoni.txt", "r")
lista_record = punta.readlines()
punta.close()
#spacchettamento record e creazione istanze
for record in lista_record:
    titolo, cantante, autori, durata, genere, strplay, eol = record.split(',')
    istanza_canzone = Canzone(titolo,cantante,autori,durata,genere)
    if strplay != "":
        playlist = strplay.split(';')
        istanza_canzone.playlist= playlist
    lista_canzoni.append(istanza_canzone)

scelta = 0
while scelta != 7:
    print('''
          1. creare una istanza di canzone
          2. modificare i dati della canzone
          3. visualizzare i dati della canzone
          4. aggiungere una canzone a una playlist
          5. visualizzare le canzoni di una specifica playlist
          6. visualizzare tutte le canzoni
          7. esci''')
    scelta = int(input("Inserisci la tua scelta: "))
    if scelta == 1:
        titolo = input("Inserisci il titolo della canzone: ")
        cantante = input("Inserisci il cantante: ")
        autori = input("Inserisci gli autori separati da un trattino: ")
        durata = input("Inserisci la durata in sec: ")
        genere = input("Inserisci il genere: ")
        istanza_canzone = Canzone(titolo,cantante,autori,durata,genere)
        lista_canzoni.append(istanza_canzone)
    elif scelta == 2:
        titolo = input("Inserisci il titolo della canzone da visualizzare: ")
        trovato = False
        for canzone in lista_canzoni:
            if canzone.titolo == titolo:
                titolo = input("Inserisci il titolo della canzone, inserisci ENTER se non vuoi modificare: ")
                cantante = input("Inserisci il cantante, inserisci ENTER se non vuoi modificare: ")
                autori = input("Inserisci gli autori separati da un trattino, inserisci ENTER se non vuoi modificare: ")
                durata = input("Inserisci la durata in sec, inserisci ENTER se non vuoi modificare: ")
                genere = input("Inserisci il genere, inserisci ENTER se non vuoi modificare: ")
                canzone.modifica(titolo, cantante,autori,durata,genere)
                trovato = True
        if  not trovato:
            print("La canzone ",titolo," non esiste")
    elif scelta == 3:
        titolo = input("Inserisci il titolo della canzone da visualizzare: ")
        trovato = False
        for canzone in lista_canzoni:
            if canzone.titolo == titolo:
                canzone.visualizza()
                trovato = True
        if  not trovato:
            print("La canzone ",titolo," non esiste") 
    elif scelta == 4:
        titolo = input("Inserisci il titolo della canzone da assegnare alla playlist: ")
        play = input("Inserisci la playlist: ")
        trovato = False
        for canzone in lista_canzoni:
            if canzone.titolo == titolo:
                canzone.aggiungi_playlist(play)
                trovato = True
        if  not trovato:
            print("La canzone ",titolo," non esiste")
    elif scelta == 5:
        play = input("Inserisci la playlist di cui vuoi sapere le canzoni: ")
        trovato = False
        for canzone in lista_canzoni:
            if play in canzone.playlist:
                canzone.visualizza()
                trovato = True
        if  not trovato:
            print("Non ci sono canzoni nella playlist ",play)
    elif scelta == 6:
        for canzone in lista_canzoni:
            canzone.visualizza()
    elif scelta == 7:
        print("Grazie per aver usato il mio programma")
    else:
        print("Scegli una voce tra quelle del menu")
#scrittura istanze sul file
punta = open("Canzoni.txt", "w")
for canzone in lista_canzoni:
    if canzone.playlist != []:
        strplay = ';'.join(canzone.playlist)
    else:
        strplay = ""
    record = canzone.titolo + ',' + canzone.cantante + ',' + canzone.autori + ',' + str(canzone.durata)+ ',' + canzone.genere + ',' + strplay + ',\n'
    punta.write(record)
punta.close()