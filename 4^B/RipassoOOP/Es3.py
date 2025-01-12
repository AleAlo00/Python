"""
3)
Una bottiglietta d’acqua può essere riempita 50 volte prima che la plastica inizi a degradarsi. 
Implementa una classe Bottiglietta che possiede un contatore privato. 
Decrementa il contatore ogni volta che il metodo riempi viene invocato.
 Solleva un’eccezione se il metodo
viene invocato quando il contatore è zero.
"""

class Bottiglietta(object):
    #attributo di classe
    __contatore = 50

    def __init__(self):
        self.__contatore = 50

    def riempi(self):
        if self.__contatore == 0:
            raise ValueError("Il contatore è a zero.")  
        self.__contatore -= 1

    def mostra_contatore(self):
        if self.__contatore == 0:
            print("Il contatore è a zero.")
        elif self.__contatore > 5:
            print("Il contatore è sopra la metà.")
        elif self.__contatore < 5:
            print("Il contatore è sotto la metà.")


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


istanza_bottiglietta = Bottiglietta()

scelta = 0
while scelta != 3:
    print("\nMenu:")
    print("1. Riempi bottiglietta")
    print("2. Mostra contatore")
    print("3. Esci")
    scelta = controllo_input("Scegli un'opzione: ", [1, 2, 3])

    if scelta == 1:
        try:
            istanza_bottiglietta.riempi()
        except ValueError as errore:
            print(errore)

    elif scelta == 2:
        istanza_bottiglietta.mostra_contatore()

    elif scelta == 3:
        print("Arrivederci!")
        
