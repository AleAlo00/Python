#Libreria per la ricerca avanzata

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