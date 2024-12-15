#import file classe persona_atleta 
import ClassAtleta as A 


# Main
# Input dati atleta
nome = input("\nInserisci il nome: \n --->| ")
cognome = input("\nInserisci il cognome: \n --->| ")
sport = input("\nInserisci lo sport: \n --->| ")


# Istanza dell'atleta
persona_atleta = A.Atleta(nome, cognome, sport)

scelta = 0
while scelta != 5:
    # Menu
    try:
        scelta = int(input("""
        <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Opzioni Atleta ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
        Scegli un'operazione:
        
            [ 1 ] Modifica dati
            [ 2 ] Visualizza dati
            [ 3 ] Gestione visita medica
            [ 4 ] Assegna squadra
            [ 5 ] Esci
            
        --->| """))

        if scelta not in [1, 2, 3, 4, 5]:
            print("Errore: Scelta non valida")
    except ValueError:
        print("Errore: Inserisci un numero valido")

    # Modifica dati atleta
    if scelta == 1:
        nome = input("\nInserisci il nome: \n --->| (Enter per annullare)")
        cognome = input("\nInserisci il cognome: \n --->|  (Enter per annullare)")
        sport = input("\nInserisci lo sport: \n --->|  (Enter per annullare)")
        persona_atleta.modifica(nome, cognome, sport)

    # Visualizza dati atleta
    elif scelta == 2:
        persona_atleta.visualizza()

    # Effettua visita medica
    elif scelta == 3:
        domanda_visita = ""
        while domanda_visita != "si" and domanda_visita != "no":
            try:
                domanda_visita = input("\nHai effettuato la visita medica? (si/no): \n --->| ").lower()

                if domanda_visita not in ["si", "no"]:
                    print("Errore: Inserisci si o no")

                elif domanda_visita == "si":
                    persona_atleta.effettua_visita(domanda_visita)
                    print("\nVisita medica effettuata\n")
                
                elif domanda_visita == "no":
                    persona_atleta.effettua_visita(domanda_visita)
                    print("\nEffettua la visita medica prima di continuare\n")
                    

            except ValueError:
                print("Errore: Inserisci si o no")


    elif scelta == 4:
        squadra = input("\nInserisci la squadra in cui giochi: \n --->| ")
        persona_atleta.assegna_squadra(squadra)


    # Esci
    elif scelta == 5:
        print("\nArrivederci\n")

