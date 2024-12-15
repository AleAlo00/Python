import ClasseLibroNuovo as L

def aggiungiLibro():
    #input dati libro   
    titolo = input("\nInserisci il titolo del libro: ")
    autore = input("Inserisci l'autore del libro: ")

    anno = -1
    while anno < 0:
        try:
            anno = int(input("Inserisci l'anno di pubblicazione del libro: "))
            if anno < 0:
                print("Errore! Inserire un numero positivo")
        except ValueError:
            print("Errore! Inserire un numero intero")

    pagine = -1
    while pagine < 0:
        try:
            pagine = int(input("Inserisci il numero di pagine del libro: "))
            if pagine < 0:
                print("Errore! Inserire un numero positivo")

        except ValueError:
            print("Errore! Inserire un numero intero")

    editore = input("Inserisci l'editore del libro: ")
    genere = input("Inserisci il genere del libro: ")

    return titolo, autore, anno, pagine, editore, genere

#main
lista_libri = []

#menu
scelta = 0
while scelta != 7:
    try:
        scelta = int(input("""
        <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Opzioni Libro ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
        Scegli un'operazione:
                [ 1 ] Inserisci nuovo libro
                [ 2 ] Modifica dati
                [ 3 ] Visualizza libro
                [ 4 ] Visualizza tutti i libri
                [ 5 ] Prestito libro
                [ 6 ] Restituzione libro
                [ 7 ] Esci

        --->| """))

        if scelta not in [1, 2, 3, 4, 5, 6 ,7]:
            print("Errore! Inserire un numero tra 1 e 7")

    except ValueError:
        print("Errore! Inserire un numero intero")

    #inserimento nuovo libro
    if scelta == 1:
        print("Inserisci nuovo libro")
        titolo, autore, anno, pagine, editore, genere = aggiungiLibro()
        libro_nuovo = L.Libro(titolo, autore, anno, pagine, editore, genere)
        lista_libri.append(libro_nuovo)
        print("Libro inserito con successo!")

    #modifica dati
    elif scelta == 2:
        titolo = input("Inserisci il titolo del libro da modificare: ")
        trovato = False

        for libro in lista_libri:
            if libro.titolo == titolo:
                opzioni = ["titolo", "autore", "anno", "pagine", "editore", "genere"]
                for i in range(len(opzioni)):
                    print(f"[ {i+1} ] {opzioni[i]}")

                try:
                    scelta_modifica = int(input("Inserisci il numero corrispondente: "))
                    if scelta_modifica not in [1, 2, 3, 4, 5, 6]:
                        print("Errore! Inserire un numero tra 1 e 6")

                    if scelta_modifica == 1:
                        titolo = input("Inserisci il nuovo titolo: ")

                    elif scelta_modifica == 2:
                        autore = input("Inserisci il nuovo autore: ")

                    elif scelta_modifica == 3:
                        try:
                            anno = int(input("Inserisci il nuovo anno di pubblicazione: "))
                            if anno < 0:
                                print("Errore! Inserire un numero positivo")
                            else:
                                print("Errore! Inserire un numero positivo")
                        except ValueError:
                            print("Errore! Inserire un numero intero")

                    elif scelta_modifica == 4:
                        try:
                            pagine = int(input("Inserisci il nuovo numero di pagine: "))
                            if pagine < 0:
                                print("Errore! Inserire un numero positivo")
                            else:
                                print("Errore! Inserire un numero positivo")
                        except ValueError:
                            print("Errore! Inserire un numero intero")

                    elif scelta_modifica == 5:
                        editore = input("Inserisci il nuovo editore: ")

                    elif scelta_modifica == 6:
                        genere = input("Inserisci il nuovo genere: ")
                    
                    libro.modifica(titolo, autore, anno, pagine, editore, genere)
                    trovato = True
                except ValueError:
                    print("Errore! Inserire un numero intero")
        if not trovato:
            print(f"Il libro {titolo} non esiste")

    #visualizza dati libro
    elif scelta == 3:
        titolo = input("Inserisci il titolo del libro da visualizzare: ")
        trovato = False
        for libro in lista_libri:
            if libro.titolo == titolo:
                libro.visualizza()
                trovato = True
        if not trovato:
            print(f"Il libro {titolo} non esiste")

    #visualizza tutti i libri
    elif scelta == 4:
        if lista_libri:
            for libro in lista_libri:
                libro.visualizza()
        else:
            print("Nessun libro presente")

    #prestito libro
    elif scelta == 5:
        titolo = input("Inserisci il titolo del libro da mettere in prestito: ")
        domanda = ""
        while domanda not in ["si", "no"]:
            try:
                domanda = input("Il libro è in prestito? (si/no): ").lower()
                if domanda not in ["si", "no"]:
                    print("Errore! Inserire si o no")
            except ValueError:
                print("Errore! Inserire si o no")

        trovato = False
        for libro in lista_libri:
            if libro.titolo == titolo:
                libro.prestito(domanda)
                trovato = True
        if not trovato:
            print(f"Il libro {titolo} non esiste")

    #restituzione libro
    elif scelta == 6:
        titolo = input("Inserisci il titolo del libro da restituire: ")
        domanda = ""
        while domanda not in ["si", "no"]:
            try:
                domanda = input("Il libro è stato restituito? (si/no): ").lower()
                if domanda not in ["si", "no"]:
                    print("Errore! Inserire si o no")
            except ValueError:
                print("Errore! Inserire si o no")
        trovato = False
        for libro in lista_libri:
            if libro.titolo == titolo:
                libro.restituisci(domanda)
                trovato = True
        if not trovato:
            print(f"Il libro {titolo} non esiste")

    #uscita
    elif scelta == 7:
        print("Grazie per aver utilizzato il programma!")
