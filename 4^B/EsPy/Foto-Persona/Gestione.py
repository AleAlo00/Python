# Importazione delle classi
import Classi as c 

def GestionePersona():
    nome = input("Inserisci il nome -->| ")
    cognome = input("Inserisci il cognome -->| ")
    data_nascita = input("Inserisci la data di nascita -->| ")
    indirizzo = input("Inserisci l'indirizzo -->| ")
    telefono = input("Inserisci il telefono -->| ")
    cf = input("Inserisci il codice fiscale -->| ")
    return nome, cognome, data_nascita, indirizzo, telefono, cf

def GestioneFoto():
    descrizione = input("Inserisci la descrizione della foto -->| ")
    luogo = input("Inserisci il luogo della foto -->| ")
    data = input("Inserisci la data della foto -->| ")
    amici = input("Inserisci gli amici nella foto separati da - -->| ")
    return descrizione, luogo, data, amici

# Creazione delle liste
lista_persone = []
lista_foto = []
codice = 0  # Codice per le foto

# Creazione dei file
fileP = "Persone.txt"
fileF = "Foto.txt"
puntaP = open(fileP, "a")
puntaF = open(fileF, "a")
puntaP.close()
puntaF.close()

# Lettura dei file
puntaP = open(fileP, "r")
puntaF = open(fileF, "r")

# Creazione delle liste
lista_recordP = puntaP.readlines()
lista_recordF = puntaF.readlines()

# Chiusura dei file
puntaP.close()
puntaF.close()

# Conversione dei record in oggetti
for recordP in lista_recordP:
    nome, cognome, data_nascita, indirizzo, telefono, cf, eol = recordP.split(",")
    istanza_persona = c.Persona(nome, cognome, data_nascita, indirizzo, telefono, cf)
    lista_persone.append(istanza_persona)

for recordF in lista_recordF:
    luogo, data, descrizione, amici_str, codice, eol = recordF.split(",")
    istanza_foto = c.Foto(luogo, data, descrizione, amici_str, codice)
    if amici_str.strip():
        persone = [amico.strip() for amico in amici_str.split('-') if amico.strip()]
        istanza_foto.amici = persone
    lista_foto.append(istanza_foto)

# Menu principale
scelta = 0
while scelta != 6:
    print("""\n
    [ 1 ] Gestione Persona
    [ 2 ] Inserisci Foto
    [ 3 ] Modifica Foto
    [ 4 ] Gestione Foto
    [ 5 ] Cerca amici in una foto
    [ 6 ] Salva ed esci
    """)

    try:
        scelta = int(input("\nScegli un'opzione -->| "))
        if scelta not in [1, 2, 3, 4, 5, 6]:
            print("Scelta non valida")
    except ValueError:
        print("Scelta non valida")

    if scelta == 1:
        # Gestione Persona
        opzione = 0
        while opzione != 4:
            print("""\n
            [ 1 ] Inserisci Persona
            [ 2 ] Modifica Persona
            [ 3 ] Visualizza Persone
            [ 4 ] Esci
            """)
            try:
                opzione = int(input("\nScegli un'opzione -->| "))
                if opzione not in [1, 2, 3, 4]:
                    print("Scelta non valida")
            except ValueError:
                print("Scelta non valida")

            if opzione == 1:
                # Inserisci Persona
                nome, cognome, data_nascita, indirizzo, telefono, cf = GestionePersona()
                persona = c.Persona(nome, cognome, data_nascita, indirizzo, telefono, cf)
                lista_persone.append(persona)

            elif opzione == 2:
                # Modifica Persona
                trova = False
                cf = input("Inserisci il codice fiscale della persona da modificare -->| ")
                for persona in lista_persone:
                    if persona.cf == cf:
                        trova = True
                        nome, cognome, data_nascita, indirizzo, telefono, cf = GestionePersona()
                        persona.modifica(nome, cognome, data_nascita, indirizzo, telefono, cf)
                if not trova:
                    print("Persona non trovata")

            elif opzione == 3:
                # Visualizza Persone
                print("\n<~~~~~~~~~~~~~~Persone~~~~~~~~~~~~~~>")
                for persona in lista_persone:
                    persona.visualizza()

            puntaP = open(fileP, "w")
            for persona in lista_persone:
                recordP = f"{persona.nome},{persona.cognome},{persona.data_nascita},{persona.indirizzo},{persona.telefono},{persona.cf},\n"
                puntaP.write(recordP)
            puntaP.close()

    elif scelta == 2:
        # Inserisci Foto
        descrizione, luogo, data, amici = GestioneFoto()
        amici_lista = [amico.strip() for amico in amici.split('-') if amico.strip()]
        codice += 1
        codice = str(codice)
        foto = c.Foto(luogo, data, descrizione, amici_lista, codice)
        lista_foto.append(foto)

    elif scelta == 3:
        # Modifica Foto
        trova = False
        codice_foto = int(input("Inserisci il codice della foto da modificare -->| "))
        for foto in lista_foto:
            if foto.codice == codice_foto:
                trova = True
                descrizione, luogo, data, nome_foto, amici = GestioneFoto()
                amici_lista = [amico.strip() for amico in amici.split('-') if amico.strip()]
                foto.modifica(descrizione, luogo, data, nome_foto, amici_lista)
        if not trova:
            print("Foto non trovata")

    elif scelta == 4:
        opzione = 0
        while opzione != 5:
            print("""\n
            [ 1 ] Ricerca Foto per Luogo
            [ 2 ] Ricera Foto per Data
            [ 3 ] Visualizza tutte le Foto
            [ 4 ] Esci
            """)
            try:
                opzione = int(input("\nScegli un'opzione -->| "))
                if opzione not in [1, 2, 3, 4]:
                    print("Scelta non valida")
            except ValueError:
                print("Scelta non valida")

            if opzione == 1:
                # Ricerca Foto per Luogo
                trova = False
                cerca_luogo = input("Inserisci il luogo della foto da cercare -->| ")
                for foto in lista_foto:
                    if foto.luogo == cerca_luogo:
                        trova = True
                        foto.visualizza()
                if not trova:
                    print("Foto non trovata")
            
            elif opzione == 2:
                # Ricerca Foto per Data
                trova = False
                cerca_data = input("Inserisci la data della foto da cercare -->| ")
                for foto in lista_foto:
                    if foto.data == cerca_data:
                        trova = True
                        foto.visualizza()
                if not trova:
                    print("Foto non trovata")

            
            elif opzione == 3:
                # Visualizza Foto
                print("\n<~~~~~~~~~~~~~~Foto~~~~~~~~~~~~~~>")
                for foto in lista_foto:
                    foto.visualizza()

    elif scelta == 5:
        # Cerca amici in una foto
        trova = False
        cerca_amico = input("Inserisci il cf dell'amico da cercare -->| ")
        for foto in lista_foto:
            if cerca_amico in foto.amici:
                trova = True
                foto.visualizza()
        if not trova:
            print("Amico non trovato")

    elif scelta == 6:
        print("Salvataggio in corso...")

    # Salva i dati delle foto
    puntaF = open(fileF, "w")
    for foto in lista_foto:
        amici_str = "-".join(amico for amico in foto.amici)
        recordF = f"{foto.luogo},{foto.data},{foto.descrizione},{amici_str},{foto.codice},\n"
        puntaF.write(recordF)
    puntaF.close()
