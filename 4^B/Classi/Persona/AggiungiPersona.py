import ClassPersona as P

#main
#input
nome = input("\nInserisci il nome: \n --->| ")
cognome = input("\nInserisci il cognome: \n --->| ")
data_nascita = input("\nInserisci la data di nascita: \n --->| ")
indirizzo = input("\nInserisci l'indirizzo: \n --->| ")
telefono = input("\nInserisci il telefono: \n --->| ")
#istanza
persona = P.Persona(nome, cognome, data_nascita, indirizzo, telefono)

scelta = 0
while scelta != 4:
    #menu
    try:
        scelta = int(input("""
        <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Opzioni Persona ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
        Scegli un'operazione:
        
            [ 1 ] Modifica
            [ 2 ] Visualizza
            [ 3 ] Aggiungi professione
            [ 4 ] Esci
            
        --->| """))

        if scelta not in [1, 2, 3, 4]:
            print("Errore: Scelta non valida")
    except ValueError:
        print("Errore: Inserisci un numero valido")


    
    #modifica
    if scelta == 1:
        nome = input("\nInserisci il nome: \n --->| ")
        cognome = input("\nInserisci il cognome: \n --->| ")
        data_nascita = input("\nInserisci la data di nascita: \n --->| ")
        indirizzo = input("\nInserisci l'indirizzo: \n --->| ")
        telefono = input("\nInserisci il telefono: \n --->| ")
        persona.modifica(nome, cognome, data_nascita, indirizzo, telefono)
    #visualizza
    elif scelta == 2:
        persona.visualizza()
    #aggiungi professione
    elif scelta == 3:
        professione = input("\nInserisci la professione: \n --->| ")
        persona.setProfessione(professione)
    #esci
    elif scelta == 4:
        print("\nArrivederci\n")
    #errore
    else:
        print("\nErrore: Scelta non valida\n")

