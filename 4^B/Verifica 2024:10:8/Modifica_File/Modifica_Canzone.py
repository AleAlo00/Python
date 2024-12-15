import ClassCanzone as C

def aggiungi_canzone():
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

    return titolo, cantante, autore, durata, genere

#main
#inizializzazione
lista_canzoni = []
punta = open("Canzoni.txt", "a")
punta.close()
punta = open("Canzoni.txt", "r")
lista_record = punta.readlines()
punta.close()

# Lettura file
for record in lista_record:
    titolo, cantante, autore, durata, genere, playlist, eol = record.split(",")
    playlist = playlist.split(";")  # Dividi la playlist in base a ';'
    istanza_canzone = C.Canzone(titolo, cantante, autore, durata, genere)
    istanza_canzone.playlist = playlist
    lista_canzoni.append(istanza_canzone)

#menu
scelta = 0
while scelta != 7:
    try:
        scelta = int(input("""
        <~~~~~~~~~~~~~~~~~~~~~~~~~~ Opzioni Canzone ~~~~~~~~~~~~~~~~~~~~~~~~~~>
        [ 1 ] Aggiungi canzone
        [ 2 ] Modifica i dati della canzone
        [ 3 ] Visualizza canzone
        [ 4 ] Assegna la canzone a una playlist
        [ 5 ] Cerca canzone in playlist
        [ 6 ] Visulizza tutte le canzoni
        [ 7 ] Esci
                           
        -->| """))

        if scelta not in [1, 2, 3, 4, 5, 6,7]:
            print("Scelta non valida")

    except ValueError:
        print("Scelta non valida")

    #aggiungi
    if scelta == 1:
        titolo, cantante, autore, durata, genere = aggiungi_canzone()
        istanza_canzone = C.Canzone(titolo, cantante, autore, durata, genere)
        lista_canzoni.append(istanza_canzone)

    #modifica
    elif scelta == 2:
        print("Modifica")
        titolo = input("Inserisci il titolo della canzone da visualizzare: ")

        trovato = False

        for canzone in lista_canzoni:
            if canzone.titolo == titolo:
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

            canzone.modifica(titolo, cantante, autore, durata, genere)
            trovato = True

        except ValueError:
            print("Errore! Inserire un numero intero")
        
        if not trovato:
            print(f"La canzone {titolo} non esiste")

    #visualizza
    elif scelta == 3:
        titolo = input("Inserisci il titolo della canzone da visualizzare: ")

        trovato = False

        for canzone in lista_canzoni:
            if canzone.titolo == titolo:
                canzone.visualizza()
                trovato = True
        if not trovato:
            print(f"La canzone {titolo} non esiste")

    #assegnamento playlist
    elif scelta == 4:
        titolo = input("Inserisci il titolo della canzone da assegnare alla playlist: ")
        trovato = False
        for canzone in lista_canzoni:
            if canzone.titolo == titolo:
                playlist = input("Inserisci il nome della playlist: ")
                canzone.assegnamento_playlist(playlist)
                trovato = True
        if not trovato:
            print(f"La canzone {titolo} non esiste")

    elif scelta == 5:
        playlist = input("Inserisci il nome della playlist: ")
        trovato = False
        for canzone in lista_canzoni:
            if playlist in canzone.playlist:
                print(f"La canzone {canzone.titolo} è presente nella playlist {playlist}")
                trovato = True
        if not trovato:
            print(f"La playlist {playlist} non esiste")
    

    elif scelta == 6:
        if lista_canzoni:
            for canzone in lista_canzoni:
                 canzone.visualizza()
        else:
            print("Non ci sono canzoni nella lista.")

    #esci
    elif scelta == 7:
        print("Arrivederci e buona musica")

punta = open("Canzoni.txt", "w")
for canzone in lista_canzoni:
    if canzone.playlist != []:
        playlist_str = ";".join(canzone.playlist)
    else:
        playlist_str = ""

    record = canzone.titolo + "," + canzone.cantante + "," + canzone.autore + "," + str(canzone.durata) + "," + canzone.genere + "," + playlist_str + ","+ "\n"
    punta.write(record)
punta.close()
