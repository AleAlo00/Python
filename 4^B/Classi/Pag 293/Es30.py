from VeicoloClasseLibreria import Veicolo

class Automobile(Veicolo):
    modello = ""
    marca = ""
    anno = 0
    colore = ""
    tipo = ""

    def __init__(self, modello, marca, anno, colore, tipo):
        super().__init__(modello, marca, anno, colore)  # Inizializza gli attributi della classe base
        self.tipo = tipo  # Attributo specifico dell'automobile

    def modifica(self, modello, marca, anno, colore, tipo):
        super().modifica(modello, marca, anno,colore)
        if tipo != "":
            self.tipo = tipo

    def visualizza(self):
        super().visualizza()  # Visualizza gli attributi della classe base
        print(f"Tipo: {self.tipo}")

class Autobus(Veicolo):
    modello = ""
    marca = ""
    anno = 0
    colore = ""
    capacita_passeggeri = 0

    def __init__(self, modello, marca, anno, colore, capacita_passeggeri):
        super().__init__(modello, marca, anno,colore)  # Inizializza gli attributi della classe base
        self.capacita_passeggeri = capacita_passeggeri  # Attributo specifico dell'autobus
    
    def modifica(self, modello, marca, anno, colore, capacita_passeggeri):
        super().modifica(modello, marca, anno, colore)
        if capacita_passeggeri != 0:
            self.capacita_passeggeri = capacita_passeggeri

    def visualizza(self):
        super().visualizza()  # Visualizza gli attributi della classe base
        print(f"Capacità Passeggeri: {self.capacita_passeggeri}")


# Funzione per aggiungere un veicolo
def aggiungi_veicolo():
    print("\nScegli il tipo di veicolo da aggiungere:")
    print("[ 1 ] Automobile")
    print("[ 2 ] Autobus")
    tipo = int(input("Scelta: "))

    modello = input("Inserisci il modello del veicolo: ")
    marca = input("Inserisci la marca del veicolo: ")
    anno = int(input("Inserisci l'anno di fabbricazione del veicolo: "))
    colore = input("Inserisci il colore del veicolo: ")

    if tipo == 1:  # Automobile
        tipo_auto = input("Inserisci il tipo di automobile : ")
        return Automobile(modello, marca, anno, colore, tipo_auto)
    elif tipo == 2:  # Autobus
        capacita_passeggeri = int(input("Inserisci la capacità di passeggeri dell'autobus: "))
        return Autobus(modello, marca, anno, colore, capacita_passeggeri)
    else:
        print("Scelta non valida!")
        return None


# Main
lista_veicoli = []  # Lista per contenere solo veicoli

scelta = 0
while scelta != 6:
    try:
        scelta = int(input("""
        <~~~~~~~~~~~~~~~~~~~~~~~~~~~ Gestione Veicoli ~~~~~~~~~~~~~~~~~~~~~~~~~~~>
        Scegli un'operazione:
                [ 1 ] Inserisci nuovo veicolo
                [ 2 ] Modifica veicolo
                [ 3 ] Visualizza veicolo
                [ 4 ] Visualizza tutti i veicoli
                [ 5 ] Esci

        --->| """))

        if scelta not in range(1, 6):
            print("Errore! Inserire un numero tra 1 e 5")

    except ValueError:
        print("Errore! Inserire un numero intero")

    # Inserimento nuovo veicolo
    if scelta == 1:
        veicolo_nuovo = aggiungi_veicolo()
        if veicolo_nuovo:
            lista_veicoli.append(veicolo_nuovo)
            print("Veicolo aggiunto con successo!")

    # Modifica veicolo
    elif scelta == 2:
        modello = input("Inserisci il modello del veicolo da modificare: ")
        trovato = False
        for veicolo in lista_veicoli:
            if veicolo.modello == modello:
                nuovo_modello = input("Inserisci il nuovo modello (premi invio per mantenere quello attuale): ")
                nuova_marca = input("Inserisci la nuova marca (premi invio per mantenere quella attuale): ")
                nuovo_anno = input("Inserisci il nuovo anno (premi invio per mantenere quello attuale): ")
                nuovo_colore = input("Inserisci il nuovo colore (premi invio per mantenere quello attuale): ")
                
                if nuovo_modello: veicolo.modello = nuovo_modello
                if nuova_marca: veicolo.marca = nuova_marca
                if nuovo_anno: veicolo.anno = int(nuovo_anno)
                if nuovo_colore: veicolo.colore = nuovo_colore
                
                if isinstance(veicolo, Automobile):
                    nuovo_tipo = input("Inserisci il nuovo tipo di automobile (premi invio per mantenere quello attuale): ")
                    if nuovo_tipo: veicolo.tipo = nuovo_tipo
                elif isinstance(veicolo, Autobus):
                    nuova_capacita = input("Inserisci la nuova capacità di passeggeri (premi invio per mantenere quella attuale): ")
                    if nuova_capacita: veicolo.capacita_passeggeri = int(nuova_capacita)
                
                print("Veicolo modificato con successo!")
                trovato = True
                break
        
        if not trovato:
            print(f"Veicolo con modello '{modello}' non trovato.")

    # Visualizza un veicolo
    elif scelta == 3:
        modello = input("Inserisci il modello del veicolo da visualizzare: ")
        trovato = False
        for veicolo in lista_veicoli:
            if veicolo.modello == modello:
                veicolo.visualizza()
                trovato = True
                break
        if not trovato:
            print(f"Veicolo con modello '{modello}' non trovato.")

    # Visualizza tutti i veicoli
    elif scelta == 4:
        if lista_veicoli:
            print("Veicoli presenti:\n")
            for veicolo in lista_veicoli:
                veicolo.visualizza()
        else:
            print("Nessun veicolo presente.")

    # Esci
    elif scelta == 5:
        print("Grazie per aver utilizzato il programma!")
