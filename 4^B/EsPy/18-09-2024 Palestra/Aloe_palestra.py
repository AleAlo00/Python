import LibreriaCreazioneFileAloeA as lcf

def InserisciCorso(lista):
    scelta = "si"
    while scelta == "si":
        Denominazione = input("Inserisci la denominazione del corso : ").lower()

        is_valid = False
        while not is_valid:
            try:
                Anno = int(input("Inserisci l'anno del corso: "))
                if Anno < 2022:
                    print("L'anno deve essere maggiore del 2022.")
                else:
                    is_valid = True  
            except ValueError:
                print("L'anno deve essere un numero.")

        is_valid_posti = False
        while not is_valid_posti:
            try:
                NumeroPosti = int(input("Inserisci il numero massimo di posti per il corso: "))
                if NumeroPosti < 0:
                    print("Il numero massimo di posti deve essere maggiore di 0.")
                else:
                    is_valid_posti = True
            except ValueError:
                print("Il numero massimo di posti deve essere un numero.")


        NumeroIscritti = 0

        corsi = f"{Denominazione},{Anno},{NumeroPosti},{NumeroIscritti},\n"
        lista.append(corsi)

        scelta = input("Vuoi inserire un altro corso? si/no: ").lower()
        while scelta not in ["si", "no"]:
            scelta = input("Vuoi inserire un altro corso? si/no: ").lower()

    return lista

def Iscrizionecorsi(lista):
    corsi_disponibili = []

    for corsi in lista:
        denominazione_corso, anno_fondazione, numero_posti, numero_iscritti, eol = corsi.split(",")
        anno_fondazione = int(anno_fondazione)
        numero_iscritti = int(numero_iscritti)
        numero_posti = int(numero_posti)
        posti_liberi = numero_posti - numero_iscritti

        if posti_liberi > 0 and anno_fondazione > 2023:
            corsi_disponibili.append(corsi)

    if len(corsi_disponibili) == 0:
        print("Non ci sono corsi disponibili.")
        return lista

    print("Seleziona un corso dal seguente elenco:")
    for index, corsi in enumerate(corsi_disponibili):
        denominazione_corso, anno_fondazione, numero_posti, numero_iscritti, eol = corsi.split(",")
        posti_liberi = int(numero_posti) - int(numero_iscritti)
        print(f"{index + 1}. {denominazione_corso} (Anno: {anno_fondazione}, Posti liberi: {posti_liberi})")

    try:
        scelta = int(input("Inserisci il numero del corso a cui vuoi iscriverti: ")) - 1
        if scelta < 0 or scelta >= len(corsi_disponibili):
            print("Scelta non valida.")
            return lista
    except ValueError:
        print("Inserisci un numero valido.")
        return lista

    numero_iscritti_da_aggiungere = int(input("Inserisci il numero di persone da iscrivere: "))
    denominazione_corso, anno_fondazione, numero_posti, numero_iscritti, eol = corsi_disponibili[scelta].split(",")
    
    numero_posti = int(numero_posti)
    numero_iscritti = int(numero_iscritti)

    posti_disponibili = numero_posti - numero_iscritti

    if numero_iscritti_da_aggiungere <= posti_disponibili:
        numero_iscritti += numero_iscritti_da_aggiungere
        lista[lista.index(corsi_disponibili[scelta])] = f"{denominazione_corso},{anno_fondazione},{numero_posti},{numero_iscritti},\n"
        print(f"{numero_iscritti_da_aggiungere} persone iscritte con successo al corso {denominazione_corso}.")
    else:
        print(f"ATTENZIONE! Non è possibile eseguire l'iscrizione per il corso {denominazione_corso}. Posti disponibili: {posti_disponibili}.")

    return lista

def VisualizzaPalestre(lista):
    print("Corsi con posti disponibili:\n")
    for corsi in lista:
        Denominazione, Anno, NumeroPosti, NumeroIscritti, eol = corsi.split(",")
        NumeroPosti = int(NumeroPosti)
        NumeroIscritti = int(NumeroIscritti)
        Anno = int(Anno)

        posti_liberi = NumeroPosti - NumeroIscritti
        if posti_liberi > 0 and Anno > 2023:
            print(f"Denominazione: {Denominazione}\nPosti Liberi: {posti_liberi}\n")

percorso = "Aloe_corsi.txt"
punta = lcf.RiempireFileTesto(percorso)

# Lettura dei corsi dal file
lista_corsi = lcf.LetturaFileTesto(percorso).readlines()

scelta = 0
while scelta != 4:
    print("""
    Corsi   
    1. Inserisci corsi
    2. Iscrizione ai corsi
    3. Visualizza corsi con posti disponibili
    4. Salva ed Esci
          """)
    try:
        scelta = int(input("Inserisci la tua scelta: "))
    except ValueError:
        print("Inserire un numero valido.")

    if scelta == 1:
        lista_corsi = InserisciCorso(lista_corsi)
    
    elif scelta == 2:
        print("Iscrivi ai corsi")
        lista_corsi = Iscrizionecorsi(lista_corsi)

    elif scelta == 3:
        VisualizzaPalestre(lista_corsi)

    elif scelta == 4:
        with open(percorso, 'w') as punta:
            punta.writelines(lista_corsi)
        print("Salvataggio effettuato")
        print("Grazie per aver usato i corsi🏋️‍♂️")
        
    else:
        print("Scelta non valida")
