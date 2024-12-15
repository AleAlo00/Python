#importare file libreria
import ClassiAzienda as CA
import datetime
import re

def controllo_input(domanda,lista_opzioni,valore):
    controllo = True
    while controllo:
        try:
            if valore == 1:
                scelta = int(input(domanda))
            elif valore == 2:
                scelta = input(domanda).capitalize()
            if scelta not in lista_opzioni:
                print("Errore! Scelta non valida")
            else:
                controllo = False
            
        except ValueError:
            print("Errore! Scelta non valida")
    return scelta
        

def inserisci_dipendente():
    #Inserimento dati
    nome = input("Nome -->| ")
    cognome = input("Cognome -->| ")
    età = controllo_input("Età -->| ", range(0, 100), 1)
    Sesso = controllo_input("Sesso (M / F) -->| ", ["M", "F"], 2)
    id = input("ID (Es: 001A) -->| ")
    Esperienza = controllo_input("Esperienza (Bassa / Media / Alta) -->| ", ["Bassa", "Media", "Alta"], 2)
    return nome, cognome, età, Sesso, id, Esperienza


def inserisci_progetto():
    #Inserimento dati
    Codice = input("Codice (Es: 0001A) -->| ")
    Descrizione = input("Descrizione -->| ")
    data_inizio = controlla_data("Data inizio (gg/mm/aaaa) -->| ")
    data_fine = controlla_data("Data fine (gg/mm/aaaa) -->| ")
    return Codice, Descrizione, data_inizio, data_fine


def ricerca(ricercato, lista_dipendenti, attributo):
    trovato = False
    for dipendente in lista_dipendenti:
        valore_attributo = getattr(dipendente, attributo)
        
        if attributo == "età":
            valore_attributo = int(valore_attributo)
        if valore_attributo == ricercato:
            trovato = True
            dipendente.visualizza()
    if not trovato:
        print("Dipendente non trovato")


def controlla_data(stringa):
    giusta = False
    anno = datetime.datetime.now().year
    while not giusta:
        try:
            Data = input(stringa)

            if not re.match(r"\d{2}/\d{2}/\d{4}", Data):
                print("La data inserita non è valida. Formato data errato")
            else:
                giorno,mese,anno = Data.split("/")
                giorno,mese,anno = int(giorno),int(mese),int(anno)
                if mese < 1 or mese > 12:
                    print("La data inserita non è valida. Il mese è errato")
                else:
                    # Controlla l'anno
                    if anno < 1800 or anno > 2100:
                        print("La data inserita non è valida. L'anno è errato")
                    else:
                        # Controlla il giorno in base al mese
                        if (mese == 4 or mese == 6 or mese == 9 or mese == 11) and (giorno < 1 or giorno > 30):
                            print("La data inserita non è valida. Il giorno è errato, non esiste nel mese")
                        elif mese == 2:  # Febbraio
                            # Controlla se l'anno è bisestile
                            if (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0):
                                if giorno < 1 or giorno > 29:
                                    print("La data inserita non è valida. Il giorno è errato, il mese è febbraio di anno bisestile.")
                                else:
                                    print("La data inserita è corretta.")
                                    data = f"{giorno}/{mese}/{anno}"
                                    giusta = True
                                    return data
                            else:
                                if giorno < 1 or giorno > 28:
                                    print("La data inserita non è valida. Il giorno è errato, il mese è febbraio di anno non bisestile.")
                                else:
                                    print("La data inserita è corretta.")
                                    data = f"{giorno}/{mese}/{anno}"
                                    giusta = True
                                    return data
                        elif giorno < 1 or giorno > 31:
                            print("La data inserita non è valida. Il giorno è errato.")
                        else:
                            print("La data inserita è corretta.")
                            data = f"{giorno}/{mese}/{anno}"
                            giusta = True
                            return data
        except ValueError:
            print("La data inserita non è valida. Formato data errato")

                



#creazione lista dipendenti e progetti
lista_dipendenti = []
lista_progetti = []

#Creazione file dipendenti e progetti
fileD = "Dipendenti.txt"
puntaD = open(fileD, "a")
puntaD.close()
fileP = "Progetti.txt"
puntaP = open(fileP, "a")
puntaP.close()

#Letture file dipendenti e progetti
puntaD = open(fileD, "r")
puntaP = open(fileP, "r")   

#Creazione lista record dipendenti e progetti
lista_recordD = puntaD.readlines()
lista_recordP = puntaP.readlines()

#Chiusura file
puntaD.close()
puntaP.close()

#Record dipendenti e progetti
for recordD in lista_recordD:
    nome, cognome, età, Sesso, id, Esperienza, Disponibilità_str, CodiceProgetto, eol = recordD.split(",")
    if Disponibilità_str == "True":
        Disponibilità = True
    else:
        Disponibilità = False
    istanza_dipendente = CA.Dipendente(nome, cognome, età, Sesso, id, Esperienza)
    istanza_dipendente.Disponibilità = Disponibilità
    if CodiceProgetto.strip():
        istanza_dipendente.Codice_Progetto = CodiceProgetto
    lista_dipendenti.append(istanza_dipendente)

for recordP in lista_recordP:
    Codice, Descrizione, data_inizio, data_fine, dipendenti_str, eol = recordP.split(",")
    istanza_progetto = CA.Progetto(Codice, Descrizione, data_inizio, data_fine)
    if dipendenti_str.strip():  
        persone = []
        dipendenti_elenco = dipendenti_str.split('-')  
        for dipendente in dipendenti_elenco:
            dipendente = dipendente.strip()  
            if dipendente:  
                persone.append(dipendente)
        istanza_progetto.Dipendenti = persone 

    lista_progetti.append(istanza_progetto)

#Menu principale
scelta = 0
while scelta != 7:
    print("\n<~~~~~~~~~~~Menu~~~~~~~~~~~>")
    print("""
    [ 1 ] Gestione Dipendenti
    [ 2 ] Gestione Progetti
    [ 3 ] Assegnazione dei progetti ai dipendenti
    [ 4 ] Ricerca di dipendenti
    [ 5 ] Ricerca di progetti
    [ 6 ] Ricerca di dipendenti che lavoro a progetti specifici 
    [ 7 ] Salva ed Esci
    """)

    scelta = controllo_input("Scegli un'opzione -->|  ", [1, 2, 3, 4, 5, 6, 7], 1)

    #Scelta 1
    #Gestione Dipendenti
    if scelta == 1:
        sceltaD = 0
        while sceltaD != 4:
            print("\n<~~~~~~~~~~~Gestione Dipendenti~~~~~~~~~~~>")
            print("""
            [ 1 ] Aggiungi Dipendente
            [ 2 ] Modifica Dipendente
            [ 3 ] Visualizza Dipendenti
            [ 4 ] Esci
            """)
        
            sceltaD = controllo_input("Scegli un'opzione -->|  ", [1, 2, 3, 4], 1)

            #Scelta 1.1
            #Aggiungi Dipendente
            if sceltaD == 1:
                nome, cognome, età, Sesso, id, Esperienza = inserisci_dipendente()
                istanza_dipendente = CA.Dipendente(nome, cognome, età, Sesso, id, Esperienza)
                lista_dipendenti.append(istanza_dipendente)
            
            #Scelta 1.2
            #Modifica Dipendente
            elif sceltaD == 2:
                print("\n<~~~~~~~~~~~Modifica Dipendente~~~~~~~~~~~>")
                trovato = False
                id = input("Inserisci l'ID del dipendente da modificare -->| ")
                for dipendente in lista_dipendenti:
                    if dipendente.ID == id:
                        trovato = True
                        nome, cognome, età, Sesso, id, Esperienza = inserisci_dipendente()
                        dipendente.modifica(nome, cognome, età, Sesso, id, Esperienza)
                if not trovato:
                    print("Dipendente non trovato")
                
            #Scelta 1.3
            #Visualizza Dipendenti
            elif sceltaD == 3:
                print("\n<~~~~~~~~~~~Dipendenti~~~~~~~~~~~>")
                for dipendente in lista_dipendenti:
                    dipendente.visualizza()

            #Scelta 1.4
            #Esci
            elif sceltaD == 4:
                print("Uscita in corso...")


    #Scelta 2
    #Gestione Progetti
    elif scelta == 2:
        sceltaP = 0
        while sceltaP != 4:
            print("\n<~~~~~~~~~~~Gestione Progetti~~~~~~~~~~~>")
            print("""
            [ 1 ] Aggiungi Progetto
            [ 2 ] Modifica Progetto
            [ 3 ] Visualizza Progetti
            [ 4 ] Esci
            """)
        
            sceltaP = controllo_input("Scegli un'opzione -->|  ", [1, 2, 3, 4], 1)

            #Scelta 2.1
            #Aggiungi Progetto
            if sceltaP == 1:
                Codice, Descrizione, data_inizio, data_fine = inserisci_progetto()
                istanza_progetto = CA.Progetto(Codice, Descrizione, data_inizio, data_fine)
                lista_progetti.append(istanza_progetto)
            
            #Scelta 2.2
            #Modifica Progetto
            elif sceltaP == 2:
                print("\n<~~~~~~~~~~~Modifica Progetto~~~~~~~~~~~>")
                trovato = False
                Codice = input("Inserisci il codice del progetto da modificare -->| ")
                for progetto in lista_progetti:
                    if progetto.Codice == Codice:
                        trovato = True
                        Codice, Descrizione, data_inizio, data_fine = inserisci_progetto()
                        progetto.modifica(Codice, Descrizione, data_inizio, data_fine)
                if not trovato:
                    print("Progetto non trovato")
                
            #Scelta 2.3
            #Visualizza Progetti
            elif sceltaP == 3:
                print("\n<~~~~~~~~~~~Progetti~~~~~~~~~~~>")
                for progetto in lista_progetti:
                    progetto.visualizza()

            #Scelta 2.4
            #Esci
            elif sceltaP == 4:
                print("Uscita in corso...")

        

    # Scelta 3
    # Assegnazione dei progetti ai dipendenti
    elif scelta == 3:
        print("\n<~~~~~~~~~~~Progetti~~~~~~~~~~~>")
        for i, progetto in enumerate(lista_progetti):
            print(f"{i}. Codice: {progetto.Codice} - Descrizione: {progetto.Descrizione}")

        print("\n<~~~~~~~~~~~Dipendenti~~~~~~~~~~~>")
        for i, dipendente in enumerate(lista_dipendenti):
            if dipendente.Disponibilità == True:
                Disponibilità = "Disponibile"
                print(f"{i}. ID: {dipendente.ID} - Nome: {dipendente.nome} {dipendente.cognome} - Disponibile: {Disponibilità}")
            

        print("\n<~~~~~~~~~~~Assegnazione Progetti~~~~~~~~~~~>")
        id_input = input("Inserisci gli ID dei dipendenti separati da '-' (es: 001A-002B) -->| ")
        Codice = input("Inserisci il codice del progetto -->| ")

        id_input = [id.strip() for id in id_input.split('-') if id.strip()]
        progetto_trovato = False   
        dipendent_trovato = False
        for progetto in lista_progetti:
            if progetto.Codice == Codice:
                for dipendente in lista_dipendenti:
                    if dipendente.ID in id_input:
                        progetto_trovato = True
                        dipendent_trovato = True
                        progetto.assegna_dipendente(dipendente.ID,dipendente)
                        dipendente.cambia_disponibilità()
                        print(f"Progetto {progetto.Codice} assegnato a {dipendente.ID}")

                        
        if not progetto_trovato:
            print("Progetto non trovato")
        if not dipendent_trovato:
            print("Dipendente non trovato")


    # Scelta 4
    # Ricerca di dipendenti
    elif scelta == 4:
        sceltaR = 0
        while sceltaR != 5:
            print("\n<~~~~~~~~~~~Ricerca Dipendenti~~~~~~~~~~~>")
            print("""
            [ 1 ] Ricerca per ID
            [ 2 ] Ricerca per Nome
            [ 3 ] Ricerca per Età
            [ 4 ] Ricerca per Esperienza
            [ 5 ] Esci
            """)
        
            sceltaR = controllo_input("Scegli un'opzione -->|  ", [1, 2, 3, 4, 5], 1)

            #Scelta 4.1
            #Ricerca per ID
            if sceltaR == 1:
                id_cercato = input("Inserisci l'ID del dipendente da cercare (Es: 001A) -->| ")
                ricerca(id_cercato, lista_dipendenti, "ID")

            #Scelta 4.2
            #Ricerca per Nome
            elif sceltaR == 2:
                nome = input("Inserisci il nome del dipendente da cercare -->| ")
                ricerca(nome, lista_dipendenti, "nome")
            
            #Scelta 4.3
            #Ricerca per Età
            elif sceltaR == 3:
                età = controllo_input("Inserisci l'età del dipendente da cercare -->| ", range(0, 100), 1)
                ricerca(età, lista_dipendenti, "età")
            
            #Scelta 4.4
            #Ricerca per Esperienza
            elif sceltaR == 4:
                Esperienza = controllo_input("Inserisci l'esperienza del dipendente da cercare (Bassa / Media / Alta) -->| ", ["Bassa", "Media", "Alta"], 2)
                ricerca(Esperienza, lista_dipendenti, "Esperienza")

            #Scelta 4.5
            #Esci
            elif sceltaR == 5:
                print("Uscita in corso...")
    
    
    # Scelta 5
    # Ricerca di progetti
    elif scelta == 5:
        sceltaR = 0
        while sceltaR != 4:
            print("\n<~~~~~~~~~~~Ricerca Progetti~~~~~~~~~~~>")
            print("""
            [ 1 ] Ricerca per Codice
            [ 2 ] Ricerca per Data inizio
            [ 3 ] Ricerca per Data fine
            [ 4 ] Esci
            """)
        
            sceltaR = controllo_input("Scegli un'opzione -->|  ", [1, 2, 3, 4], 1)

            #Scelta 5.1
            #Ricerca per Codice
            if sceltaR == 1:
                Codice = input("Inserisci il codice del progetto da cercare (Es: 0001A) -->| ")
                trovato = False
                for progetto in lista_progetti:
                    if progetto.Codice == Codice:
                        trovato = True
                        progetto.visualizza()
                if not trovato:
                    print("Progetto non trovato")

            #Scelta 5.2
            #Ricerca per Data inizio
            if sceltaR == 2:
                data_inizio = controlla_data("Inserisci la data di inizio del progetto (gg/mm/aaaa) -->| ")
                trovato = False
                for progetto in lista_progetti:
                    if progetto.data_inizio == data_inizio:
                        trovato = True
                        progetto.visualizza()
                if not trovato:
                    print("Progetto non trovato")

            #Scelta 5.3
            #Ricerca per Data fine
            if sceltaR == 3:
                data_fine = controlla_data("Inserisci la data di fine del progetto (gg/mm/aaaa) -->| ")
                trovato = False
                for progetto in lista_progetti:
                    if progetto.data_fine == data_fine:
                        trovato = True
                        progetto.visualizza()
                if not trovato:
                    print("Progetto non trovato")
            
            #Scelta 5.4
            #Esci
            elif sceltaR == 4:
                print("Uscita in corso...")
    
    
    # Scelta 6
    # Ricerca di dipendenti che lavoro a progetti specifici
    elif scelta == 6:
        print("\n<~~~~~~~~~~~Progetti~~~~~~~~~~~>")
        for i, progetto in enumerate(lista_progetti):
            print(f"{i}. Codice: {progetto.Codice} - Descrizione: {progetto.Descrizione}")

        Codice = input("Inserisci il codice del progetto da cercare -->| ")
        trovato = False
        for progetto in lista_progetti:
            if progetto.Codice == Codice:
                trovato = True
                for dipendente in lista_dipendenti:
                    if dipendente.ID in progetto.Dipendenti:
                        dipendente.visualizza()
        if not trovato:
            print("Progetto non trovato")
    
    # Scelta 7
    # Salva ed Esci  
    elif scelta == 7:
        print("Salvataggio in corso...")
        puntaD = open(fileD, "w")
        for dipendente in lista_dipendenti:
            puntaD.write(f"{dipendente.nome},{dipendente.cognome},{dipendente.età},{dipendente.Sesso},{dipendente.ID},{dipendente.Esperienza},{dipendente.Disponibilità},{dipendente.Codice_Progetto},\n")
        puntaD.close()

        puntaP = open(fileP, "w")
        for progetto in lista_progetti:
            progetto.Dipendenti = "-".join(progetto.Dipendenti)
            puntaP.write(f"{progetto.Codice},{progetto.Descrizione},{progetto.data_inizio},{progetto.data_fine},{progetto.Dipendenti},\n")
        puntaP.close()
