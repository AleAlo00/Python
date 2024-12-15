#import file classe Libro
import ClasseLibro as L


#main
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

#creazione oggetto libro
libro_nuovo = L.Libro(titolo, autore, anno, pagine, editore, genere)

#menu

scelta = 0
while scelta != 5:
    try:
        scelta = int(input("""
        <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Opzioni Libro ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
        Scegli un'operazione:
                [ 1 ] Modifica dati
                [ 2 ] Visualizza dati
                [ 3 ] Prestito
                [ 4 ] Restituzione
                [ 5 ] Esci
                           

        --->| """))

        if scelta not in [1, 2, 3, 4, 5]:
            print("Errore! Inserire un numero tra 1 e 5")

    except ValueError:
        print("Errore! Inserire un numero intero")

    #modifica dati
    if scelta == 1:
        print("Modifica dati libro")
        lista_opzioni = ["titolo", "autore", "anno", "pagine", "editore", "genere"]
        print("Scegli cosa modificare: ")
        for i in range(len(lista_opzioni)):
            print(f"[ {i+1} ] {lista_opzioni[i]}")

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
                except ValueError:
                    print("Errore! Inserire un numero intero")

            elif scelta_modifica == 4:
                try:
                    pagine = int(input("Inserisci il nuovo numero di pagine: "))
                    if pagine < 0:
                        print("Errore! Inserire un numero positivo")
                except ValueError:
                    print("Errore! Inserire un numero intero")

            elif scelta_modifica == 5:
                editore = input("Inserisci il nuovo editore: ")

            elif scelta_modifica == 6:
                genere = input("Inserisci il nuovo genere: ")

            libro_nuovo.modifica(titolo, autore, anno, pagine, editore, genere)

        except ValueError:
            print("Errore! Inserire un numero intero")

    #visualizza dati
    elif scelta == 2:
        print("Visualizza dati libro")
        libro_nuovo.visualizza()

    #prestito
    elif scelta == 3:

        print("Prestito libro")
        domanda_prestito = ""
        while domanda_prestito != "si" and domanda_prestito != "no":
            try:
                domanda_prestito = input("Il libro è in prestito (si/no): ").lower()

                if domanda_prestito not in ["si", "no"]:
                    print("Errore! Inserire si o no")

                elif domanda_prestito == "si":
                    libro_nuovo.prestito(domanda_prestito)
                    

                elif domanda_prestito == "no":
                    libro_nuovo.prestito(domanda_prestito)

                

            except ValueError:  
                print("Errore! Inserire si o no")

        print("Libro in prestito")


    #restituzione
    elif scelta == 4:
        print("Restituzione libro")
        domanda_restituzione = ""
        while domanda_restituzione != "si" and domanda_restituzione != "no":
            try:
                domanda_restituzione = input("Il libro è stato restituito? (si/no): ").lower()

                if domanda_restituzione not in ["si", "no"]:
                    print("Errore! Inserire si o no")

                elif domanda_restituzione == "si":
                    libro_nuovo.restituisci(domanda_restituzione)

                elif domanda_restituzione == "no":
                    libro_nuovo.restituisci(domanda_restituzione)

            except ValueError:
                print("Errore! Inserire si o no")
                
        print("Libro restituito")
        
    elif scelta == 5:
        print("Uscita in corso...")
        print("Grazie per aver utilizzato il programma!")

    else:
        print("Errore! Inserire un numero tra 1 e 5")