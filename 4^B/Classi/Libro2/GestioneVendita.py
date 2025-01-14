import LibroClasseLibreria as lc

def aggiungi_libro(lista_autori):
    #input
    titolo = input("\nInserisci il titolo del libro: ")
    autori_input = input(f"Inserisci l'autore del libro {titolo} separati da - : ")
    autori = [autore.strip() for autore in autori_input.split("-")]

    for autore in autori:
        if autore not in lista_autori:
            lista_autori.append(autore)

    casa_editrice = input(f"Inserisci la casa editrice del libro {titolo}: ")
    try:
        prezzo = float(input(f"Inserisci il prezzo del libro {titolo}: "))
        if prezzo < 0:
            print("Inserisci un prezzo positivo")
    except ValueError:
        print("Inserisci un prezzo valido")
        
    try:
        numero_pagine = int(input(f"Inserisci il numero di pagine del libro {titolo}: "))
        if numero_pagine < 0:
            print("Inserisci un numero di pagine positivo")
    except ValueError:
        print("Inserisci un numero di pagine valido")


    return  lc.Libro(titolo, autori, casa_editrice, prezzo, numero_pagine)



def RicercaAvanzata(ricerca, lista_libri):
    #parte da cercare
    parti = ricerca.lower().split("*")
    #risultati
    risultati = []
    for libro in lista_libri:
        #se il titolo del libro inizia con la parte da cercare
        if libro.titolo.lower().startswith(parti[0]) == True:
            risultati.append(libro.titolo)

    
    for i, libro in enumerate(risultati):
        print(f"[ {i+1} ] {libro}")

    scelta = int(input("Scegli il libro: ")) 
    return risultati[scelta-1]

    
            

    
    

#main
lista_libri = []
lista_autori = []   
punta = open("LibroVendite.txt","a")
punta.close()
#lettura iniziale file dei libri
punta = open("LibroVendite.txt", "r")
lista_record = punta.readlines()
punta.close()

for record in lista_record:
    titolo, autori, casa_editrice, prezzo, numero_pagine, disponibilità, eol = record.split(",")
    autori = autori.split("-")
    instanza_libro = lc.Libro(titolo, autori, casa_editrice, prezzo, numero_pagine)
    disponibilità = int(disponibilità)
    instanza_libro.disponibilità = disponibilità
    lista_libri.append(instanza_libro)

scelta = 0
while scelta != 9:
    print('''
            1. Aggiungere un libro
            2. Modificare i dati di un libro
            3. Visualizzare i libri
            4. Cambiare il prezzo di un libro
            5. Modificare la disponibilità di un libro
            6. Visualizzare tutti i libri
            7. Vendere un libro
            8. Acquistare un libro
            9. Esci''')
    
    try:
        scelta = int(input("\nInserisci la tua scelta: "))
        if scelta not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print("Errore! Inserire un numero tra 1 e 9")
    except ValueError:
        print("Errore! Inserire un numero intero")
    
    if scelta == 1:
        istanza_libro = aggiungi_libro(lista_autori)
        lista_libri.append(istanza_libro)
    
    elif scelta == 2:
        print("Modifica")
        titolo = RicercaAvanzata(input("Inserisci il titolo del libro da modificare: "), lista_libri)

        trovato = False

        for libro in lista_libri:
            if libro.titolo == titolo:
                opzioni = ["titolo", "autore", "casa editrice", "numero pagine"]

                for i in range(len(opzioni)):
                    print(f"[ {i+1} ] {opzioni[i]}")

                try:
                    scelta_modificata = int(input("Inserisci il numero corrispondente: "))
                    if scelta_modificata not in [1, 2, 3, 4]:
                        print("Errore! Inserire un numero tra 1 e 4")

                    if scelta_modificata == 1:
                        nuovo_titolo = input("Inserisci il nuovo titolo del libro: ")
                        libro.titolo = nuovo_titolo if nuovo_titolo != "" else libro.titolo

                    elif scelta_modificata == 2:
                        # Visualizza gli autori del libro
                        print("Autori attuali:")
                        for i, autore in enumerate(libro.autori):
                            print(f"[ {i+1} ] {autore}")

                        # Scelta dell'autore da modificare
                        scelta_autore = int(input("Scegli il numero dell'autore da modificare: ")) - 1

                        # Richiede il nuovo nome dell'autore
                        nuovo_autore = input("Inserisci il nuovo nome dell'autore: ").strip()

                        # Aggiorna l'autore nella lista del libro e in lista_autori
                        autore_precedente = libro.autori[scelta_autore]
                        libro.autori[scelta_autore] = nuovo_autore
                        if autore_precedente in lista_autori:
                            lista_autori[lista_autori.index(autore_precedente)] = nuovo_autore

                        print("Autore aggiornato con successo.")


                    elif scelta_modificata == 3:
                        nuova_casa_editrice = input(f"Inserisci la nuova casa editrice del libro '{libro.titolo}': ")
                        libro.casa_editrice = nuova_casa_editrice if nuova_casa_editrice != "" else libro.casa_editrice

                    elif scelta_modificata == 4:
                        nuovo_numero_pagine = -1
                        while nuovo_numero_pagine < 0:
                            try:
                                nuovo_numero_pagine = input(f"Inserisci il nuovo numero di pagine per '{libro.titolo}': ")
                                if nuovo_numero_pagine == "":
                                    nuovo_numero_pagine = libro.numero_pagine
                                else:
                                    nuovo_numero_pagine = int(nuovo_numero_pagine)
                                    if nuovo_numero_pagine < 0:
                                        print("Inserisci un valore positivo")
                            except ValueError:
                                print("Inserisci un valore valido")
                        libro.numero_pagine = nuovo_numero_pagine

                    trovato = True
                    print("Modifica completata.")

                except ValueError:
                    print("Errore! Inserire un numero intero")
            
        if not trovato:
            print(f"Il libro '{titolo}' non esiste.")

    
    elif scelta == 3:
        titolo = RicercaAvanzata(input("Inserisci il titolo del libro da visualizzare: "), lista_libri)
        trovato = False
        for libro in lista_libri:
            if libro.titolo == titolo:
                libro.visualizza()
                trovato = True
        if not trovato:
            print("Il libro ", titolo, " non esiste")
    
    elif scelta == 4:
        titolo = RicercaAvanzata(input("Inserisci il titolo del libro di cui modificare il prezzo: "), lista_libri)
        percentuale = float(input("Inserisci la percentuale (positiva per aumento, negativa per diminuire): "))
        trovato = False
        for libro in lista_libri:
            if libro.titolo == titolo:
                libro.cambia_prezzo(percentuale)
                trovato = True
        if not trovato:
            print("Il libro ", titolo, " non esiste")
    
    elif scelta == 5:
        titolo = RicercaAvanzata(input("Inserisci il titolo del libro di cui modificare la disponibilità: "), lista_libri)
        try:
            disponibilita = int(input("Inserisci il numero di libri disponibili: "))
            if disponibilita < 0:
                print("Inserisci un valore positivo")
        except ValueError:
            print("Inserisci un valore valido")

        trovato = False
        for libro in lista_libri:
            if libro.titolo == titolo:
                libro.modifica_disponibilita(disponibilita)
                trovato = True
        if not trovato:
            print("Il libro ", titolo, " non esiste")
    
    elif scelta == 6:
        for libro in lista_libri:
            libro.visualizza()

    elif scelta == 7:
        titolo = RicercaAvanzata(input("Inserisci il titolo del libro da vendere: "), lista_libri)
        venduto = False
        for libro in lista_libri:
            if libro.titolo == titolo: 
                if libro.disponibilità > 0:
                    libro.modifica_disponibilita(libro.disponibilità - 1)
                    venduto = True
                    print(f"Il libro {libro.titolo} è stato venduto.")
        if not venduto:
            print("Non ci sono libri disponibili.")

    elif scelta == 8:
        titolo = RicercaAvanzata(input("Inserisci il titolo del libro da acquistare: "), lista_libri)
        try:
            N_acquisti = int(input("Inserisci il numero di copie da acquistare: "))
            if N_acquisti < 0:
                print("Inserisci un valore positivo") 
        except ValueError:
            print("Inserisci un valore valido")
        for libro in lista_libri:
            if libro.titolo == titolo:
                libro.modifica_disponibilita(libro.disponibilità + N_acquisti)
                print(f"Il libro {libro.titolo} è stato acquistato.")
        

    elif scelta == 9:
        print("Grazie per aver usato il programma.")
    
    else:
        print("Scegli una voce tra quelle del menu.")

#scrittura istanze sul file
punta = open("LibroVendite.txt", "w")

for libro in lista_libri:
    libro.prezzo = "{:.2f}".format(float(libro.prezzo))
    libro.prezzo = str(libro.prezzo)
    autori_str = "-".join(libro.autori)
    record = libro.titolo + "," + autori_str + "," + libro.casa_editrice + "," + libro.prezzo + "," + str(libro.numero_pagine) + "," + str(libro.disponibilità) + "," + "\n"
    punta.write(record)
punta.close()
