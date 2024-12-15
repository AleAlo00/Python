#import file classe Data
import ClasseData as D
from datetime import date

def richiestaData():
    prova = False
    while not prova:
        data_input = input("\nInserisci la data di nascita (gg/mm/aaaa): -->| ")
        try:
            giorno, mese, anno = data_input.split('/')  # Separa i valori
            giorno = int(giorno)  # Converte il giorno in intero
            mese = int(mese)      # Converte il mese in intero
            anno = int(anno)      # Converte l'anno in intero
            prova = True
            return giorno, mese, anno
        except ValueError:
            print("Formato non valido. Assicurati di inserire la data nel formato gg/mm/aaaa.")

# main
giorno, mese, anno = richiestaData()

# Crea Data iniziale
data_nascita = D.Data(giorno, mese, anno)

valore_valido = data_nascita.validita()  # Controlla la validità della data

while not valore_valido:  # Continua finché la data non è valida
    print("\nData non valida")
    giorno, mese, anno = richiestaData()
    # Ricalcola la validità della data
    valore_valido = data_nascita.validita()

if data_nascita.controllo_data():
    print("\nL'anno è bisestile")
else:
    print("\nL'anno non è bisestile")

if valore_valido:
    print("\nData valida")
    data_nascita.visualizza_data()
