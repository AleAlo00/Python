"""
9)
I prodotti venduti in un grande magazzino sono organizzati per reparti.
Usa la classe Prodotto che è già presente nella tua libreria di classi e aggiornala inserendo il nuovo attributo che indica il reparto dove è possibile trovare il prodotto. 
Inserisci quindi un metodo che consente la gestione di questo attributo e realizza il diagramma UML della classe.
Scrivi uno script Python che usa la classe Prodotto e tramite un menu permette di:
1. creare nuove istanze della classe Prodotto;
2. modificare i dati di un’istanza;
3. ricercare i prodotti presenti in uno specifico reparto.
Utilizza una lista per la gestione delle istanze multiple della classe Prodotto.
Salva i dati su file di testo.
"""



class Prodotto(object):
    
    nome = ""
    prezzo = 0
    reparto = ""
    descrizione = ""
    codice = 0
    disponibilita = 0

    def __init__(self, nome, prezzo, reparto, descrizione, codice, disponibilita):
        self.nome = nome
        self.prezzo = prezzo
        self.reparto = reparto
        self.descrizione = descrizione
        self.codice = codice
        self.disponibilita = disponibilita

    def modifica(self, nome, prezzo, reparto, descrizione, codice, disponibilita):

        if nome != "":
            self.nome = nome
        if prezzo != 0:
            self.prezzo = prezzo
        if reparto != "":
            self.reparto = reparto
        if descrizione != "":
            self.descrizione = descrizione
        if codice != 0:
            self.codice = codice
        if disponibilita != 0:
            self.disponibilita = disponibilita


    def visualizza(self):
        print(f"Nome : {self.nome} \nPrezzo : {self.prezzo} \nReparto : {self.reparto} \nDescrizione : {self.descrizione} \nCodice : {self.codice} \nDisponibilita : {self.disponibilita}")

        
def controllo_input(stringa, valori_validi):
    corretto = False
    while corretto == False:
        try:
            risposta = int(input(stringa))
            if risposta in valori_validi:
                corretto = True
                return risposta
            else:
                print("Valore non valido. Riprova.")
        except ValueError:
            print("Inserisci un numero valido.")

prodotti = []
scelta = 0

while scelta != 4:
    print("1. Crea nuovo prodotto")
    print("2. Modifica prodotto")
    print("3. Visualizza prodotti per reparto")
    print("4. Salva ed esci")
    scelta = controllo_input("Scegli un'opzione -->|  ", [1, 2, 3, 4])

    if scelta == 1:
        nome = input("Inserisci il nome del prodotto --> ")
        prezzo = controllo_input("Inserisci il prezzo del prodotto -->|  ",range(0, 1000))
        reparto = input("Inserisci il reparto del prodotto -->|  ")
        descrizione = input("Inserisci la descrizione del prodotto -->|  ")
        codice = controllo_input("Inserisci il codice del prodotto -->|  ", range(0, 1000))
        disponibilita = controllo_input("Inserisci la disponibilita del prodotto -->|  ", range(0, 1000))
        prodotto = Prodotto(nome, prezzo, reparto, descrizione, codice, disponibilita)
        prodotti.append(prodotto)

    elif scelta == 2:
        codice = controllo_input("Inserisci il codice del prodotto da modificare -->|  ", range(0, 1000))
        for prodotto in prodotti:
            if prodotto.codice == codice:
                nome = input("Inserisci il nome del prodotto -->|  ")
                prezzo = controllo_input("Inserisci il prezzo del prodotto -->|  ", range(0, 1000))
                reparto = input("Inserisci il reparto del prodotto -->|  ")
                descrizione = input("Inserisci la descrizione del prodotto -->|  ")
                codice = controllo_input("Inserisci il codice del prodotto -->|  ", range(0, 1000))
                disponibilita = controllo_input("Inserisci la disponibilita del prodotto -->|  ", range(0, 1000))
                prodotto.modifica(nome, prezzo, reparto, descrizione, codice, disponibilita)
                
        else:
            print("Prodotto non trovato")

    elif scelta == 3:
        reparto = input("Inserisci il reparto da cercare -->|  ")
        for prodotto in prodotti:
            if prodotto.reparto == reparto:
                prodotto.visualizza()
        else:
            print("Reparto non trovato")

    elif scelta == 4:
        with open("prodotti.txt", "w") as file:
            for prodotto in prodotti:
                file.write(f"{prodotto.nome},{prodotto.prezzo},{prodotto.reparto},{prodotto.descrizione},{prodotto.codice},{prodotto.disponibilita},\n")
        print("Salvataggio completato")
    


