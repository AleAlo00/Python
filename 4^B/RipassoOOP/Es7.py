"""
7)
Implementa un main che permetta la gestione delle classe realizzate negli esercizi 4, 5 e 6.
"""


from Es4 import Cane, Gatto
from Es6 import Anatra

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

animali = []

scelta = 0
while scelta != 6:
    print("\nMenu:")
    print("1. Aggiungi cane")
    print("2. Aggiungi gatto")
    print("3. Aggiungi anatra")
    print("4. Modifica animale")
    print("5. Visualizza animali")
    print("6. Esci")
    scelta = controllo_input("Scegli un'opzione -->| ", [1, 2, 3, 4, 5, 6])

    if scelta == 1:
        nome = input("Inserisci il nome del cane -->| ")
        eta = int(input("Inserisci l'età del cane -->| "))
        razza = input("Inserisci la razza del cane -->| ")
        colore = input("Inserisci il colore del cane -->| ")
        cane = Cane(nome, eta, razza, colore)
        animali.append(cane)

    elif scelta == 2:
        nome = input("Inserisci il nome del gatto -->| ")
        eta = int(input("Inserisci l'età del gatto -->| "))
        razza = input("Inserisci la razza del gatto -->| ")
        colore = input("Inserisci il colore del gatto -->| ")
        gatto = Gatto(nome, eta, razza, colore)
        animali.append(gatto)

    elif scelta == 3:
        nome = input("Inserisci il nome dell'anatra -->| ")
        eta = int(input("Inserisci l'età dell'anatra -->| "))
        colore = input("Inserisci il colore dell'anatra -->| ")
        tipo = input("Inserisci il tipo dell'anatra -->| ")
        muove = input("Inserisci come si muove l'anatra -->| ")
        anatra = Anatra(nome, eta, colore, tipo, muove)
        animali.append(anatra)

    elif scelta == 4:
        nome = input("Inserisci il nome dell'animale da modificare -->| ")
        animale_trovato = ""
        for animale in animali:
            if animale.nome == nome:
                animale_trovato = animale

        if animale_trovato:
            if isinstance(animale_trovato, Cane):
                nuovo_nome = input("Inserisci il nuovo nome del cane -->| ")
                nuova_eta = int(input("Inserisci la nuova età del cane -->| "))
                nuova_razza = input("Inserisci la nuova razza del cane -->| ")
                nuovo_colore = input("Inserisci il nuovo colore del cane -->| ")
                animale_trovato.modifica(nuovo_nome, nuova_eta, nuova_razza, nuovo_colore)

            elif isinstance(animale_trovato, Gatto):
                nuovo_nome = input("Inserisci il nuovo nome del gatto -->| ")
                nuova_eta = int(input("Inserisci la nuova età del gatto -->| "))
                nuova_razza = input("Inserisci la nuova razza del gatto -->| ")
                nuovo_colore = input("Inserisci il nuovo colore del gatto -->| ")
                animale_trovato.modifica(nuovo_nome, nuova_eta, nuova_razza, nuovo_colore)

            elif isinstance(animale_trovato, Anatra):
                nuovo_nome = input("Inserisci il nuovo nome dell'anatra -->| ")
                nuova_eta = int(input("Inserisci la nuova età dell'anatra -->| "))
                nuovo_colore = input("Inserisci il nuovo colore dell'anatra -->| ")
                nuovo_tipo = input("Inserisci il nuovo tipo dell'anatra -->| ")
                nuovo_muove = input("Inserisci come si muove la nuova anatra -->| ")
                animale_trovato.modifica(nuovo_nome, nuova_eta, nuovo_colore, nuovo_tipo, nuovo_muove)
        else:
            print("Animale non trovato.")

    elif scelta == 5:
        if animali:
            for animale in animali:
                animale.visualizza()
        else:
            print("Nessun animale presente.")

    elif scelta == 6:
        print("Arrivederci!")
