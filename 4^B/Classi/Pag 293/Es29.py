from LibroClasseLibreria import Libro

class Rivista(Libro):
    def __init__(self, titolo, autore,casa_editrice, prezzo, numero_pagine, periodicità):
        super().__init__(titolo, autore, casa_editrice, prezzo,numero_pagine)  # Attributi ereditati dalla classe Libro
        self.periodicità = periodicità  # Attributo specifico della rivista

    def modifica(self, titolo, autore, casa_editrice, numero_pagine, periodicità):
        super().modifica(titolo, autore, casa_editrice, numero_pagine)
        if periodicità != "":
            self.periodicità = periodicità
        

    def visualizza(self):
        super().visualizza()
        print(f"Periodicità: {self.periodicità}")

    def modifica_periodicità(self, nuova_periodicità):
        self.periodicità = nuova_periodicità

def aggiungi_rivista():
    titolo = input("\nInserisci il titolo della rivista: ")
    autore = input("Inserisci l'autore della rivista: ")
    giusto = False
    while not giusto:
        try:
            prezzo = input("Inserisci il prezzo della rivista: ")
            # Controllo se il prezzo è un numero valido
            prezzo = float(prezzo)
            giusto = True
        except ValueError:
            print("Errore! Inserire un prezzo valido (esempio: 10.50).")
    
    giusto = False
    while not giusto:
        try:
            periodicità = input("Inserisci la periodicità della rivista (settimanale/mensile/trimestrale): ")
            if periodicità not in ["settimanale", "mensile", "trimestrale"]:
                print("Errore! Inserire una periodicità valida.")
            else:
                giusto = True
        except ValueError:
            print("Errore! Inserire una periodicità valida.")
    
    casa_editrice = input("Inserisci la casa editrice della rivista: ")
    numero_pagine = int(input("Inserisci il numero di pagine della rivista: "))
    return Rivista(titolo, autore, casa_editrice, prezzo,numero_pagine, periodicità)


# Main
lista_riviste = []  # Lista per contenere solo riviste

scelta = 0
while scelta != 6:
    try:
        scelta = int(input("""
        <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Gestione Riviste ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
        Scegli un'operazione:
                [ 1 ] Inserisci nuova rivista
                [ 2 ] Modifica periodicità
                [ 3 ] Visualizza rivista
                [ 4 ] Visualizza tutte le riviste
                [ 5 ] Esci

        --->| """))

        if scelta not in range(1, 6):
            print("Errore! Inserire un numero tra 1 e 5")

    except ValueError:
        print("Errore! Inserire un numero intero")

    # Inserimento nuova rivista
    if scelta == 1:
        rivista_nuova = aggiungi_rivista()
        lista_riviste.append(rivista_nuova)
        print("Rivista aggiunta con successo!")

    # Modifica periodicità
    elif scelta == 2:
        titolo = input("Inserisci il titolo della rivista da modificare: ")
        trovato = False
        for rivista in lista_riviste:
            if rivista.titolo == titolo:
                nuova_periodicità = input("Inserisci la nuova periodicità (settimanale/mensile/trimestrale) : ")
                rivista.modifica_periodicità(nuova_periodicità)
                print("Periodicità modificata con successo!")
                trovato = True
        if not trovato:
            print(f"La rivista '{titolo}' non esiste.")

    # Visualizza una rivista
    elif scelta == 3:
        titolo = input("Inserisci il titolo della rivista da visualizzare: ")
        trovato = False
        for rivista in lista_riviste:
            if rivista.titolo == titolo:
                rivista.visualizza()
                trovato = True
        if not trovato:
            print(f"La rivista '{titolo}' non esiste.")

    # Visualizza tutte le riviste
    elif scelta == 4:
        if lista_riviste:
            print("\n<~~~ Elenco Riviste ~~~>")
            for rivista in lista_riviste:
                rivista.visualizza()

        else:
            print("Nessuna rivista presente.")

    # Esci
    elif scelta == 5:
        print("Grazie per aver utilizzato il programma!")
